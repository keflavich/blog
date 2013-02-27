FITS manipuation with imagemagick, gimp, etc.
#############################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, photo, unix

It is possible to convert .fits files to .png, .jpg, etc:
`` convert -normalize a.fits a.png ``
To get things to come out nicely, you have to do the scaling essentially
by hand in python/idl/iraf. DS9 is only useful for finding out what
scaling you want to use; past that it's pretty much not useable.
To make colors look nice in the GIMP, use solid background layers with
your image as the alpha mask. Then put your image in with itself as an
alpha mask so you can easily control the whiteness (saturation) of the
color you've selected.
I'll be blogging about this more as I prep my next entry for the NRAO
photo contest.
