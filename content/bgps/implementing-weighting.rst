Implementing weighting
######################
:date: 2008-11-09 04:56
:author: Adam (noreply@blogger.com)
:tags: googlepost, weighting
:slug: implementing-weighting

Not as easy as it ought to be.
I think I need to do a few things:
1. check and make sure there are no more of those !@#$!@#$#@% different
sized array subtractions/multiplications. 'weight' and
'best\_astro\_model' need to have the same size & shape in mem\_iter\_pc
2. I guess just check and make sure stuff works. The weighted mean I'm
using appears to be right: sum(weight \* value) / sum(weight)
I hate making lists that end up being two items....
