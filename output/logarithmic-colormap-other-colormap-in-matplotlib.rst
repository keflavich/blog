Logarithmic Colormap / Other Colormap in Matplotlib
###################################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, matplotlib, python

This is kind of a pain to find out:
``from matplotlib.colors import LogNormim = imshow(.... cmap=... , norm=LogNorm(vmin=clevs[0], vmax=clevs[-1])) ``
It also works for contours, and can be particularly useful if you only
want to display contours at a few levels, but you want the colormap to
start at a different point. e.g.:
``contour(xx,levels=[2,3,4,5,6,7,8,9,10],norm=matplotlib.colors.Normalize(vmin=0,vmax=10))``
will start at light blue instead of dark blue in the default colormap
