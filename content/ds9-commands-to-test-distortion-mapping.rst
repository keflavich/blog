ds9 commands to test distortion mapping
#######################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, ds9, bgps

.. raw:: html

   <p>

trying to figure out whether I'm screwing something up in the distortion
map phase... the -scale limits command here is new and useful

::

    ds9 testfields_*pix5*_map0.fits -cmap sls -scale limits 0 .005 -zoom 4 -match frames wcs -match scales -match colorbars &ds9 testfields_*pix15*_map0.fits -cmap sls -scale limits 0 .003 -zoom 4 -match frames wcs -match scales -match colorbars &ds9 testfields_*pix10*_map0.fits -cmap sls -scale limits 0 .004 -zoom 4 -match frames wcs -match scales -match colorbars &

