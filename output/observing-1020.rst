Observing 10/20
###############
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, python, observing

I don't have a better place to post this one, so here it is:
`http://sites.google.com/site/iras05358/figure-discussion/figures/iras05358\_triple\_17.29.png?attredirects=0
`_
My automated fitter (`Gaussfitting Cube Collapser`_) has come a long
way. I now adaptively choose to fit 1, 2, or 3 Gaussian components to
output to a data cube.
The purpose of that code is primarily to find a two-dimensional way to
display information about the 3D structure, specifically about the
presence/absence of outflows. Outflows will inevitably be confused with
multiple velocity components, but they are also likely to be convolved
with them.

.. _`http://sites.google.com/site/iras05358/figure-discussion/figures/iras05358\_triple\_17.29.png?attredirects=0
`: http://sites.google.com/site/iras05358/figure-discussion/figures/iras05358_triple_17.29.png?attredirects=0
.. _Gaussfitting Cube Collapser: http://casa.colorado.edu/~ginsbura/pygausscollapse.htm
