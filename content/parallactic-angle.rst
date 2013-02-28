Parallactic Angle
#################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, astronomy

So it turns out parallactic angle and field rotation are essentially the
same thing. While working on the data pipeline for the Bolocam Galactic
Plane Survey, I've needed to deal with this. The parallactic angle is
dependent on the alt/az, and therefore the time, of the observation. So
using an RA/Dec in J2000 coordinates to get alt/az isn't going to work,
because my observations weren't in 2000.0.... my best hope is that the
PA in the NCDF files is actually the correct parallactic angle.
YARGH!
