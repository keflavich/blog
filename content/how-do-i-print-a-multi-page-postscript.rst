How do I print a multi-page postscript?
#######################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, gnuplot, computer, postscript

I want to print a multi-page postscript duplexed and, if possible, two
per page. pstopng, pstopdf, and the variants failed me horribly by
making postscripts that don't fit the bounding box at all. Any ideas?
So far the best I've come up with is switching gnuplot's output to pdf,
which is a workaround rather than a solution, but is useful nonetheless:
``set terminal pdf enhanced dashed``
