DS9 - crosshairs on command line
################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, ds9, computer

``ds9 pmm*_map0.fits -zscale -match scales -zoom 4 -match frames wcs -crosshair 17:33:02.7 -13:04:49.5 wcs fk5 -lock crosshairs wcs &``
``ds9 pmp*_map0.fits -zscale -match scales -zoom 4 -match frames wcs -crosshair 17:33:02.7 -13:04:49.5 wcs fk5 -lock crosshairs wcs &``
``ds9 mpp*_map0.fits -zscale -match scales -zoom 4 -match frames wcs -crosshair 17:33:02.7 -13:04:49.5 wcs fk5 -lock crosshairs wcs &``
``ds9 mpm*_map0.fits -zscale -match scales -zoom 4 -match frames wcs -crosshair 17:33:02.7 -13:04:49.5 wcs fk5 -lock crosshairs wcs &``
DS9's crosshairs are extremely useful for checking on WCS coordinate
matching, especially when they can be set precisely using the command
line. I don't know how to set the coordinates exactly interactively...
that may come later.
