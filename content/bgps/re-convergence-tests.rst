Re: Convergence Tests
#####################
:date: 2008-08-23 17:03
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, mapping
:slug: re-convergence-tests

Made a little code to check out convergence, but frankly it's pretty
easy to just build a mapcube and plot lines in the iteration axis. The
code is in bgps\_pipeline/postproc/compareiters.pro, and it is not a
single program.
Comparing deconvolution to no deconvolution, deconvolution is a lot
better. Without it, there are much more substantial negative regions. In
the GC, my test region, the noise-dominated areas were about the same,
though the no-deconvolve map had a little bit more large scale
structure. The signal-dominated regions were very nearly uniformly
brighter. The deconvolved map was ~3 Jy brighter in SGR B2, or 4%.
