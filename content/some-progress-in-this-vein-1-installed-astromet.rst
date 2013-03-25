Attempts to install astrometry.net (comment on problems-with-index-files-generation)
####################################################################################
:date: 2012-11-04 17:26
:author: Adam (noreply@blogger.com)
:tags: comment

Some progress in this vein:
1. installed astrometry.net (but without some graphical extras)
2. figured out how to create indexes! Finders are ~5x5', so based on
`this post`_ I want to use ~2-3' healpixes.
3. I also should be using denser catalogs than the all-sky USNO B1,
especially for infrared targets.
So, here's a sample build command (using a CDS-based FITS table, but
modified by me using atpy):
build-index -v -i OMC1\_optical\_phot\_DaRio.fits -o
OMC1\_optical\_phot\_DaRio\_astrometryindex -N 1758

.. _this post: http://forum.astrometry.net/index.php?p=/discussion/2/problems-with-index-files-generation/p1
