Converting a FITS cube to a CASA Image
======================================
:author: Adam Ginsburg <adam.g.ginsburg@gmail.com>
:tags: W51, GBT
:date: 2013-12-18 15:15

If you want to perform analysis on a FITS file in CASA, you first need to
import it into `.image` format.

    importfits('file.fits','file.image')

If this works, great!  You can move on.  CASA will treat NaN values in an image
as 'masked'.

Dealing with Errors
-------------------

There may be issues with FITS headers.  CASA respects a large number of header
keys (reference_).

There are many ways to edit a FITS header.  One of the most straightforward to
use is edhead_.  Otherwise, one can use CASA's imhead_

============ ============ ===========
CASA Keyword FITS keyword Description
------------ ------------ -----------
beammaj      BMAJ         Major axis of the clean beam
beammin      BMIN         Minor axis of the clean beam
beampa       BPA          Position angle of the clean beam
bunit        BUNIT        Brightness unit (K, Jy/beam, etc)
cdeltn       CDELTn       Pixel size, nth axis  (max n is 4)
crpixn       CRPIXn       Pixel coordinate of reference point, nth axis
crvaln       CRVALn       Pixel location of reference point, nth axis
ctypen       CTYPEn       Axis name, nth axis.  For FITS, this includes the projection
cunitn       CUNITn       Pixel units, nth axis
datamax      DATAMAX      Maximum pixel value in image
datamin      DATAMIN      Minimum pixel value in image
date-obs     DATE-OBS     Date of the observation
equinox      EQUINOX      Reference frame for directional coordinates
imtype       -            Image type: intensity, 
minpos       -            Position of the minimum value (world unit)
minpixpos    -            Same in pixel (array)
maxpos       -            Position of the maximum value (world unit)
maxpixpos    -            Same in pixel (array)
object       OBJECT       Source name
observer     OBSERVER     Observer name
projection   CTYPEn       Image projection ('SIN','TAN', or 'ZEA')
reffreqtype  -            Reference frame for the spectral coordinates
restfreq     RESTFREQ     Rest Frequency
shape        NAXISn       Number of pixels along each axis
telescope    TELESCOP     Telescope name
============ ============ ===========


What does it mean if you get this sort of error?

    CASA <1>: importfits('file.fits','file.image')
    2013-12-18 13:06:18     WARN    importfits::FITSCoordinateUtil::fromFITSHeader  The wcs function failures are too severe to continue ...
    2013-12-18 13:06:18     WARN    importfits::ImageFITSConverterImpl::FITSToImage (file /var/rpmbuild/BUILD/casapy-stable/casapy-stable-42.0.26945/casacore/images/Images/ImageFITSConverter.tcc, line 71)       No proper coordinate system defined in FITS file. Using dummy linear system instead.

First, go to the `casapy-yyyymmdd-hhmmss.log` file and look at the errors.

    2013-12-18 13:06:18     INFO    importfits::FITSCoordinateUtil::fromFITSHeader  celfix incurred the error Inconsistent or unrecognized coordinate axis types
    2013-12-18 13:06:18     INFO    importfits::FITSCoordinateUtil::fromFITSHeader  spcfix incurred the error Inconsistent or unrecognized coordinate axis types
    2013-12-18 13:06:18     INFO    importfits::FITSCoordinateUtil::fromFITSHeader  cylfix incurred the error Inconsistent or unrecognized coordinate axis types
    
In my case, the error turned out to be that `CTYPE3` was set to `RADI-LSR`,
while it should be `VELO-LSR` to be recognized by the CASA system.  The
velocity convention is, unfortunately, lost.
    

.. _reference: http://www.eso.org/projects/alma/arc/tw/pub/External/EUARCCASATutorialJan2012/ImageAnalysis-CASA.pdf
.. _edhead: http://tdc-www.harvard.edu/wcstools/edhead.html
.. _imhead: http://casaguides.nrao.edu/index.php?title=Imhead
