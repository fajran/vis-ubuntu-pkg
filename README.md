Ubuntu Repository - Total Packages and Sizes
============================================

This Git repository contains scripts I use to gather and visualize the Ubuntu
repositories in terms of total packages and their total size.

Check the GitHub page for the result - <http://fajran.github.ioo/vis-ubuntu-pkg>.

[How?](http://fajran.web.id/2013/05/ubuntu-repository-total-packages-and-sizes.html)
----

I took the package index files (a.k.a. `Packages` file) and counted the number
of packages inside. I also summed the size of each packages to get the size of
the repository. The files are from the "at-release" repository which means I
excluded the `-updates` and `-security` repositories. The at-release repository
is presumably frozen and therefore the size won’t change anymore, where the
latest two repositories are for the updates, which by definition are always
updated.  Well.. except when the release is not supported anymore.

