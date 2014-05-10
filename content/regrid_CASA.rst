Regrid an image (or cube) using CASA
====================================
:author: Adam Ginsburg <adam.g.ginsburg@gmail.com>
:tags: W51, GBT
:date: 2013-12-18 17:52

In order to regrid an image, you need some target reprojection.  The simplest way to acquire such a reprojection
is by extracting it from another image, e.g. a `FITS image`_

(I use `>>>` to indicate the `CASA <#>:` prompt here because it allows you to copy & paste the code into CASA)

.. code-block:: python

   >>> header = imregrid(imagename='file.image', template='get')

This header will be a python dictionary with two keys, `csys`, which specifies
the coordinate system, and `shap`, which gives the shape.

If you want to write up your own FITS header and you don't have a FITS file
with those exact coordinates, you can use the header_to_template_ convenience
tool in casa_tools_.

.. code-block:: python

    >>> from casa_tools import header_to_template
    >>> from astropy.io import fits
    >>> fits_header = fits.Header.fromtextfile('my_header.hdr')
    >>> header = header_to_template(fits_header)

In order to regrid the file, you then need to pass in the image name and template to imregrid.

.. code-block:: python

    >>> imregrid(imagename='file.image',
    ...          template=header,
    ...          output='file_regrid.image')

If your input image's header did not include a 'telescope' keyword, CASA will complain:

    2013-12-18 16:46:33	SEVERE	imregrid::ImageRegrid::regrid (file /opt/casa/release-4_1_0-release-1/darwin64/include/casacore/images/Images/ImageRegrid.tcc, line 118)	Cannot find the observatory name UNKNOWN in the CASA

You can add the keyword to the header yourself:

.. code-block:: python

    >>> imhead('file.image',
    ...        mode='put',
    ...        hdkey='telescope',
    ...        hdvalue='Arecibo')

References
----------

 * `Sebastian Muller's presentation`_ (page 16)
 * `imregrid docs`_ 


.. _Sebastian Muller's Presentation: http://www.eso.org/projects/alma/arc/tw/pub/External/EUARCCASATutorialJan2012/ImageAnalysis-CASA.pdf
.. _imregrid docs: http://casa.nrao.edu/docs/casaref/image.regrid.html
.. _FITS image: casaguides.nrao.edu/index.php?title=FITStoImage
.. _casa_tools: https://github.com/keflavich/casa_tools
.. _header_to_template: https://github.com/keflavich/casa_tools/blob/master/casa_tools/header_to_template.py#L11
