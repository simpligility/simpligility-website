# Notes: Maven blog post

Working file for this post. Collect ideas, shape an outline, and track open
items here. The article itself lives in `post.md`.

## Ideas



## Title suggestions

* Sooo many Maven dependencies! &mdash; matches Manfred mentors episode 13
* So many dependencies needed!


## Draft outline

- Introduce https://github.com/simpligility/maven-build-requirements and talk about the mind blowing expansion between dependencies needed for a project vs what you need for building a project
- Context it as analysis to figure out what is needed for building stuff for Chainguard Libraries themselves and then also figuring out what is even necessary so customers can rely on Chainguard Libraries and build only using it ideally
- I built the tool for figuring that out better since there is no existing Maven plugin or tool that does that
- The aim was to use this also for my talk at Open Source Summit 2026 about Maven, see the event log for details
- It was mostly a side note in that talk, that I did together with Adam Kaplan from Red Hat / IBM
- I later recorded Manfred mentors 13 - https://www.youtube.com/watch?v=-JuCNsyQXIg that demos it in much more details
- I also recently did Learning Lab about Chainguard Libraries for Java that has some cool demo projects - see https://edu.chainguard.dev/software-security/learning-labs/ll202607/
- last but not least - Adam Kaplan now joined Chainguard

## Status and open items

- [x] Decide the angle: the gap between runtime dependencies and build
  requirements, framed around maven-build-requirements and Chainguard Libraries
- [x] Draft the outline
- [x] Rename the folder slug to match the angle
- [x] Turn the skeleton in `post.md` into full prose
- [x] Add a main image: the dependency hairball generated in `assets/`, showing
  the 652 build artifacts fanning out from the 7 declared dependencies
- [x] Upload `assets/build-requirements.png` to WordPress: now at
  `/wp-content/uploads/2026/08/build-requirements.png`, to be set as the post's
  featured image
- [x] Convert the post to HTML for WordPress: see `post.html`
- [x] Once the post is live, add a link to it from the source repo README
  https://github.com/simpligility/maven-build-requirements
- [x] Once the post is live, add a link to it from Manfred mentors episode 13:
  updated the YouTube video description
- [x] Add a link to Manfred mentors episode 13 from the source repo README
  https://github.com/simpligility/maven-build-requirements
- [x] Upstream the graph tooling into
  https://github.com/simpligility/maven-build-requirements: done in
  https://github.com/simpligility/maven-build-requirements/pull/2, which adds
  `graph/build-graph.py` and `graph/render.sh`, wires graph generation into
  `analyze-test-projects.sh`, and documents the flow in the README. The `assets/`
  copies here stay as the post's source of truth for the hero image

No code blocks are planned for this post, so there is nothing to convert for
syntax highlighting.
