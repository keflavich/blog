Disagreement over definition of l,b coordinates
###############################################
:date: 2008-09-10 22:43
:author: Adam (noreply@blogger.com)
:tags: googlepost, projection
:slug: disagreement-over-definition-of-lb-coordinates

DS9 does something intuitive: cd0\_0 and cd1\_1 multiplied by the x,y
pixel difference gets you the new l,b coordinate. I think this is very
likely to be correct on the galactic plane. IDL does something
different. I don't know why different, or really how - it's buried
somewhere in wcsxy2sph - but it's definitely different. Which is right?
