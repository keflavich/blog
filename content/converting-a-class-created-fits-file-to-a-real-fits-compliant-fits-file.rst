Converting a CLASS-created .fits file to a real (FITS-compliant) FITS file
##########################################################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost

This post is to remind me, the next time I go looking, how the hell to
convert from a GILDAS CLASS fits spectrum (created by
``fits write blah.fits /mode spectrum``) to a FITS-compliant spectrum.
First, remember the FITS-WCS spectral definitions:
http://www.aanda.org/index.php?option=com\_article&access=bibcode&Itemid=129&bibcode=2006A%2526A...446..747GFUL
And the peculiar CLASS definitions:
http://iram.fr/IRAMFR/GILDAS/doc/html/class-html/node84.html
Key points:
CLASS stores the CDELT parameter as DELTAV in m/s instead of km/s and
the velocity offset of the spectral frame in VELO-LSR also in m/s.
Things to set:
CTYPE = VRAD
SPECSYS = SOURCE
SSYSSRC = LSRK
VELOSYS = frame velocity (VELO-LSR or CRVAL1)
This information is subject to change...
