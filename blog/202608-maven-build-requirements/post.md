# Sooo many Maven dependencies!

So you know how to read a Maven `pom.xml` for your Java project and locate the
declared `<dependencies>` and even understand their `scope`. Maybe you even know
that you can use `mvn dependency:tree` to list all dependencies and all the
transitive dependencies. Nice, so you know the dependencies of your project.

Or not, did you ever wonder what dependencies you need to actually build that
project? I did, and built a tool that allows you to find out for your project as
well. Try it out, I promise you will be surprised.

<!-- more -->

## Background motivation

Working on [Chainguard Libraries](https://www.chainguard.dev/libraries) as a
Maven committer, Java developer, and community advocate is a wild ride. We have
been building libraries from source for well over a year now and [learned a
lot](https://www.chainguard.dev/unchained/this-shit-is-hard-java-archeology-at-a-massive-scale).
We keep learning new things about old projects, new projects, backporting CVE
fixes, and scanning for malware and grayware, and so on. I showed some of that
again [at the recent learning
lab](https://edu.chainguard.dev/software-security/learning-labs/ll202607/).

Testing projects around the fallback to Maven Central directly and then our
filtered subset and completely removing Maven Central access caused me to look
at a LOT of download logs for my local builds and wiping my cache in
`~/.m2/repository` regularly.

Knowing that Maven downloads not just the project dependencies but also plugins,
plugin dependencies, and a whole lot more from Maven Central got me wondering.
How much more? What specifically is downloaded? All along I was thinking that
in an ideal world we would rebuild all of that from source. But first we would
have to know what artifacts we even need.

## maven-build-requirements

With that motivation I asked on the Maven developer list about anything
existing. Since there was nothing, I wrote the tool. You can find the result in
[maven-build-requirements
repository](https://github.com/simpligility/maven-build-requirements).

Excerpt from the readme that clarifies what is analyzed to be needed as a
dependency:

> The scope is everything needed to build the project from source — not just the
> runtime/compile dependency tree:
>
> * The project's own transitive dependency tree across all reactor modules (the
>   same set mvn dependency:tree would produce).
> * Every plugin used by the build — explicitly declared and implicitly bound to a
>   packaging's default lifecycle via Maven core — together with each plugin's
>   parent POM lineage and full transitive dependency tree.
> * Build extensions from .mvn/extensions.xml, again with parent POMs and
>   transitive dependencies.
> * The project's own parent POM lineage.
> * The Maven binary distribution declared by the project's wrapper.

And the results are astounding.

`quickstart-example`, as a bare-bones Maven project:

* 5 project dependencies
* 0 project parent POMs
* 13 plugins
* 17 plugin parent POMs
* 138 plugin dependencies
* 0 extensions
* 0 extension parent POMs
* 0 extension dependencies
* 1 Maven distribution

That's a total of 174 needed artifacts up from 5 project dependencies!

`multi-module-example`, more real but still super simple:

* 19 project dependencies
* 0 project parent POMs
* 10 plugins
* 24 plugin parent POMs
* 159 plugin dependencies
* 0 extensions
* 0 extension parent POMs
* 0 extension dependencies
* 1 Maven distribution

From 19 dependencies to 213 needed artifacts!

And last still a super simple project, this time using Spring Framework in the
`spring-boot-example`:

* 101 project dependencies
* 2 project parent POMs
* 30 plugins
* 28 plugin parent POMs
* 447 plugin dependencies
* 1 extension
* 2 extension parent POMs
* 40 extension dependencies
* 1 Maven distribution

Again, significantly up to 652 artifacts from 101 project dependencies.

## Open Source Summit

My ask on the Maven dev list also caused some interesting side conversations
with [Tamás Cservenák](https://www.linkedin.com/in/cservenak/) from the great
[Maveniverse](https://github.com/maveniverse) project and [Adam
Kaplan](https://www.linkedin.com/in/adambkaplan/) from Red Hat. Adam and I ended
up presenting *Is Maven safe for production?* at the Open Source Summit NA in
Minneapolis, in which we touched upon the dependencies a bit, and covered a lot
of other interesting aspects of Maven and production builds. [Watch the
recording and check out the slides for more
details](/event-log/#maven-safe-for-production).

## Manfred mentors 13

After the conference I did some final tweaks and clean ups on the project, and
then recorded my live stream episode 13 for Manfred mentors. In that episode I
talk about the project and demo it all.

<!-- WordPress auto-embeds a bare YouTube URL on its own line -->
https://www.youtube.com/watch?v=-JuCNsyQXIg

## Conclusion and final notes

So what can we learn from this insight and the project? Your footprint of
dependencies that you need to build a project from source is much larger than
you think. And what good is your project, if you can't build it securely from
source? It is also much larger than the built-in tools report. Try it on your
own project and [report any findings and
issues](https://github.com/simpligility/maven-build-requirements/issues).

As a result, any effort to "just build everything from sources" is also on a
whole other level of complexity and effort than you would anticipate at first
glance. We are working on that for Chainguard Libraries for Java, and you can
test it out with my example project.

Beyond the maven-build-requirements project, I continue to work on Trino-related
projects, [Manfred mentors](/manfred-mentors/) episodes, and [all sorts of other
hackery](https://github.com/simpligility/contributions). You can even [sponsor
me](/sponsor/).

And one last fun aspect, Adam became a Chainguardian recently, maybe you should
join us too?!
