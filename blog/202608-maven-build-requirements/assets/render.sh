#!/usr/bin/env bash
# Regenerate the build requirements hairball from the tool output and render it.
#
# The DOT is built by build-graph.py from the spring-boot-example results and
# pom. The PNG is sized to the Twenty Twenty-Five wide content slot, 1340px on
# its binding dimension, with the height following the natural aspect. No retina
# doubling; the SVG is the scalable master and carries a coordinate tooltip per
# node, so anyone needing it sharper can render from that.
set -euo pipefail

cd "$(dirname "$0")"

# Graphviz is installed via Homebrew but its keg is not symlinked onto PATH.
GVBIN="${GVBIN:-/opt/homebrew/Cellar/graphviz/15.1.1/bin}"

python3 build-graph.py

# 13.4in * 100dpi = 1340px on the binding dimension.
"$GVBIN/fdp" -Tsvg build-requirements.dot -o build-requirements.svg
"$GVBIN/fdp" -Tpng -Gdpi=100 -Gsize=13.4,13.4 build-requirements.dot \
    -o build-requirements.png

# The hairball is flat color on white, so a small palette compresses it hard
# with no visible loss. 64 colors takes the 1340px PNG from ~570KB to ~85KB.
if command -v pngquant >/dev/null 2>&1; then
    pngquant --force --skip-if-larger --quality=70-90 --strip \
        --output build-requirements.png build-requirements.png || true
elif command -v magick >/dev/null 2>&1; then
    magick build-requirements.png -colors 64 -strip \
        PNG8:build-requirements.png
fi

if command -v sips >/dev/null 2>&1; then
    sips -g pixelWidth -g pixelHeight build-requirements.png | grep pixel
fi
ls -la build-requirements.png build-requirements.svg
