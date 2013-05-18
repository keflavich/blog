What about the effects on the map?  Unfortunately,...
#####################################################
:date: 2011-02-02 02:12
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#comment
:slug: what-about-the-effects-on-the-map-unfortunately

What about the effects on the map? Unfortunately, in the tests I've run,
delining actually INCREASES the noise in the map! How is this possible?
My only hypothesis is that PCA cleaning does an excellent job of
removing the line noise, but when it is replaced with truly uncorrelated
gaussian noise, the PCA cleaning no longer removes that component.
But we don't want PCA cleaning to grab instrumental correlated noise; we
want it to be limited to atmospheric noise. So ideally we want to
completely remove the line noise without adding noise to the image...
maybe the line regions should just be set to zero after all....
