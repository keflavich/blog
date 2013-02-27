Making a postscript plot of a gigantic fits image
#################################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, idl

``    map = readfits('MOSAIC.fits',hdr)    crpix1 = sxpar(hdr,'CRPIX1')    crpix2 = sxpar(hdr,'CRPIX2')    crval1 = sxpar(hdr,'CRVAL1')    crval2 = sxpar(hdr,'CRVAL2')    cd1_1 = sxpar(hdr,'CD1_1')    cd2_2 = sxpar(hdr,'CD2_2')       x = lindgen(n_e(map[*,0]))    y = lindgen(n_e(map[0,*]))    l = (x-crpix1)*cd1_1+crval1-360    b = (y-crpix2)*cd2_2+crval2    imdisp,map,/axis,xrange=[max(l),min(l)],yrange=[min(b),max(b)],range=[-1,8]``
This code makes use of `imdisp.pro`_.

.. _imdisp.pro: http://cimss.ssec.wisc.edu/~gumley/idl/imdisp.pro
