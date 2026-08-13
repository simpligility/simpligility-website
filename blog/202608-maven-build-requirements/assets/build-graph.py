#!/usr/bin/env python3
"""Generate a category-colored dependency hairball for the Maven build
requirements post.

Reads the maven-build-requirements results file for a project and emits a
Graphviz DOT graph: the project sits at the center, one hub per requirement
category fans out from it, and every required artifact hangs off its category
hub as a leaf. Nodes are colored by category so the small set of declared
project dependencies is visually swamped by the plugin-dependency mass.

The edges are category membership, not Maven resolution edges. The flat
coordinate list carries no parent/child relationships, so no dependency arrows
are implied.
"""

import re
import sys
from pathlib import Path

# Section header in the results file -> (key, label, fill color).
# Order here is the order hubs are emitted. The plugin trio wears a warm
# palette as the hero of the image; everything else is muted cool so the eye
# lands on the plugin mass.
CATEGORIES = [
    ("Resolved dependencies:", ("projdep", "Project dependencies", "#3b82a6")),
    ("Parent POMs:", ("projparent", "Project parent POMs", "#6ba3bf")),
    ("Plugins:", ("plugin", "Plugins", "#f59e0b")),
    ("Plugin parent POMs:", ("pluginparent", "Plugin parent POMs", "#fbbf24")),
    ("Plugin dependencies:", ("plugindep", "Plugin dependencies", "#ea580c")),
    ("Extensions:", ("ext", "Extensions", "#94a3b8")),
    ("Extension parent POMs:", ("extparent", "Extension parent POMs", "#94a3b8")),
    ("Extension dependencies:", ("extdep", "Extension dependencies", "#64748b")),
    ("Maven distribution:", ("mvndist", "Maven distribution", "#cbd5e1")),
]
HEADERS = {h: meta for h, meta in CATEGORIES}

# The three plugin categories are kept together in one invisible cluster.
PLUGIN_KEYS = {"plugin", "pluginparent", "plugindep"}

# A coordinate line is indented and looks like group:artifact:type:version.
COORD = re.compile(r"^\s+(\S+:\S+:.+)$")


def parse(results_path):
    """Return an ordered list of (key, label, color, [coords])."""
    buckets = {key: [] for _, (key, _, _) in CATEGORIES}
    current = None
    for raw in results_path.read_text().splitlines():
        line = raw.rstrip()
        if line in HEADERS:
            current = HEADERS[line][0]
            continue
        if line.startswith("=") or line == "":
            # A rule or blank line closes the current section.
            if line.startswith("="):
                current = None
            continue
        m = COORD.match(raw)
        if current and m:
            buckets[current].append(m.group(1).strip())
        elif not m and current and line and not line.startswith(" "):
            # A new unindented, non-header line ends the section.
            current = None
    return [(key, label, color, buckets[key])
            for _, (key, label, color) in CATEGORIES]


# Colors for the two halves of the project dependency set, split out of the
# resolved list using the declared dependencies from the pom.
DECLARED_COLOR = "#0e7490"    # what you actually wrote in the pom
TRANSITIVE_COLOR = "#7db3c4"  # everything the declared set drags in


def esc(text):
    return text.replace("\\", "\\\\").replace('"', '\\"')


def ga(coord):
    """group:artifact key from a group:artifact:type:version coordinate."""
    return ":".join(coord.split(":")[:2])


def parse_declared(pom_path):
    """Direct dependency group:artifact keys from the project's own pom."""
    import xml.etree.ElementTree as ET

    text = pom_path.read_text()
    # Drop the default namespace so tag lookups stay simple.
    text = re.sub(r'\sxmlns="[^"]+"', "", text, count=1)
    root = ET.fromstring(text)
    declared = set()
    deps = root.find("dependencies")  # project-level, not build/plugins
    if deps is not None:
        for dep in deps.findall("dependency"):
            g = (dep.findtext("groupId") or "").strip()
            a = (dep.findtext("artifactId") or "").strip()
            if g and a:
                declared.add(f"{g}:{a}")
    return declared


def text_on(hex_color):
    """Pick black or white label text for readable contrast on a fill."""
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return "#000000" if (0.299 * r + 0.587 * g + 0.114 * b) > 150 else "#ffffff"


def build_specs(categories, declared):
    """Turn parsed categories into hub specs, splitting project dependencies
    into declared and transitive, and tagging the plugin trio for clustering."""
    specs = []
    for key, label, color, coords in categories:
        if not coords:
            continue
        if key == "projdep":
            decl = [c for c in coords if ga(c) in declared]
            trans = [c for c in coords if ga(c) not in declared]
            specs.append(dict(key="declared", label="Declared dependencies",
                              color=DECLARED_COLOR, coords=decl, cluster=None))
            specs.append(dict(key="transdep", label="Transitive dependencies",
                              color=TRANSITIVE_COLOR, coords=trans, cluster=None))
        else:
            specs.append(dict(key=key, label=label, color=color, coords=coords,
                              cluster="plugins" if key in PLUGIN_KEYS else None))
    return specs


def hub_width(n):
    """Hub circle width with area roughly proportional to artifact count."""
    return round(0.45 + 0.12 * (n ** 0.5), 2)


def node_lines(spec, indent):
    """Hub node plus its leaf nodes for one spec."""
    pad = " " * indent
    out = []
    hub = f"hub_{spec['key']}"
    fill = spec["color"]
    out.append(
        f'{pad}{hub} [label="{esc(spec["label"])}\\n{len(spec["coords"])}", '
        f'shape=circle, width={hub_width(len(spec["coords"]))}, fontsize=12, '
        f'fillcolor="{fill}", fontcolor="{text_on(fill)}", penwidth=1.5, '
        f'color="#ffffff"];')
    for i, coord in enumerate(spec["coords"]):
        node = f'{spec["key"]}_{i}'
        out.append(
            f'{pad}{node} [label="", shape=circle, fixedsize=true, width=0.15, '
            f'fillcolor="{fill}", tooltip="{esc(coord)}"];')
    return out


def emit_dot(project, specs, out_path):
    total = sum(len(s["coords"]) for s in specs)

    lines = ["digraph build_requirements {"]
    lines.append('  graph [bgcolor="#ffffff", overlap=false, sep="+8", '
                 'splines=false, K=1.1];')
    lines.append('  node [style=filled, penwidth=0, fontname="Helvetica-Bold"];')
    lines.append('  edge [color="#d4d4d4", penwidth=0.3, arrowhead=none];')

    lines.append(
        f'  root [label="{esc(project)}\\n{total} artifacts", shape=doublecircle, '
        f'width=1.5, fontsize=18, fillcolor="#111111", fontcolor="#ffffff"];')

    for spec in specs:
        lines.extend(node_lines(spec, indent=2))

    # Edges: project to each hub, hub to each leaf.
    for spec in specs:
        hub = f"hub_{spec['key']}"
        lines.append(f'  root -> {hub} [penwidth=1.4, color="#9e9e9e"];')
        for i in range(len(spec["coords"])):
            lines.append(f'  {hub} -> {spec["key"]}_{i};')

    # Invisible high-weight, short ties pull the three plugin hubs next to
    # each other without a bounding cluster, so their leaves stay organic.
    plugin_hubs = [f"hub_{s['key']}" for s in specs if s["cluster"] == "plugins"]
    for a in plugin_hubs:
        for b in plugin_hubs:
            if a < b:
                lines.append(f'  {a} -> {b} [style=invis, weight=8, len=0.6];')

    lines.append("}")
    out_path.write_text("\n".join(lines) + "\n")
    return total


def main():
    here = Path(__file__).resolve().parent
    project_dir = Path(
        "/Users/manfred.moser/dev/github/simpligility/maven-build-requirements/"
        "src/it/projects/spring-boot-example")
    results_path = (Path(sys.argv[1]) if len(sys.argv) > 1
                    else project_dir / "maven-build-requirements-results.txt")
    pom_path = (Path(sys.argv[2]) if len(sys.argv) > 2
                else project_dir / "pom.xml")
    project = "spring-boot-example"

    categories = parse(results_path)
    declared = parse_declared(pom_path)
    specs = build_specs(categories, declared)
    out_dot = here / "build-requirements.dot"
    total = emit_dot(project, specs, out_dot)

    print(f"Parsed {results_path.name} and {pom_path.name}")
    print(f"  Declared in pom: {len(declared)}")
    for s in specs:
        print(f"  {s['label']:28} {len(s['coords'])}")
    print(f"  {'TOTAL':28} {total}")
    print(f"Wrote {out_dot}")


if __name__ == "__main__":
    main()
