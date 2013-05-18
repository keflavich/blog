New coalignment code
####################
:date: 2012-03-20 15:06
:author: Adam (noreply@blogger.com)
:tags: googlepost
:slug: new-coalignment-code

pixshift has been giving me issues for a long, long time. It finally
came to a head, though, when nothing I did could make l001 "work". It
turns out, when you do cross-correlation analysis, you're really only
interested in the most correlated pixel, NOT the junk around it - the
junk around it only provides a second-order correction.
Well, `cross\_cor\_taylor.pro`_, a tool from the solar physics
community, does exactly that. And it works far, far better than my
hacked-together pixshift code. A lesson I should always take to heart:
don't rewrite code if it's out there. Of course, if I'd known it was out
there, I wouldn't have rewritten it....

.. _cross\_cor\_taylor.pro: http://solarmuri.ssl.berkeley.edu/~welsch/public/software/cross_cor_taylor.pro
