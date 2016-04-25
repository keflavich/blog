More CASA simulation & debugging
################################
:date: 2016-04-24 22:57 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, ALMA, simulation, debuggin

(this post written from snowy-ish ALMA; `just cloudy at the OSF though <https://goo.gl/photos/z3fUkCT6VVRzt8EW6>`__)

I'm tryin to repeat an experiment very similar to 
`previous <|filename|/casa_simulating.rst>`__
`simulation work <|filename|/simulated_imaging.rst>`__
in order to quantify my completeness and largest angular scales
by injecting synthetic signal into the real UV data.


However, as you might expect, it doesn't work as it did last time, even
when I (afaict) copy and paste the code directly.

Here's the new error::

    2016-04-25 02:57:21	SEVERE	Simulator::createSkyEquation() (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Simulator.cc, line 2200)	Caught exception: Transformations to/from frame "Undefined" are not possible.
    2016-04-25 02:57:21	SEVERE	Simulator::predict() (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Simulator.cc, line 2118)	Failed to create SkyEquation
    Result of predict: False

It's strange because there is nothing obviously undefined.

I'm comparing 2 FITS files that should behave identically.
The good header lacks these keywords that the bad header has::

    ['PV2_1',
     'PV2_2',
     'OBSERVER',
     'DATE-OBS',
     'OBSRA',
     'OBSDEC',
     'OBSGEO-X',
     'OBSGEO-Y',
     'OBSGEO-Z']

while the good header has these and the bad lacks them::

    ['PC03_01',
     'PC04_01',
     'PC03_02',
     'PC04_02',
     'PC01_03',
     'PC02_03',
     'PC03_03',
     'PC04_03',
     'PC01_04',
     'PC02_04',
     'PC03_04',
     'PC04_04',
     'CREATOR',
     'INSTRUME',
     'BAND',
     'PROPOSAL',
     'PRTITLE',
     'OBSID001',
     'OBSID002',
     'HISTORY']

The only significant difference is the ``PC`` values, unless CASA
is doing something with the observatory location information.

The only difference in common keywords is numerical, which seems
very unlikely to cause this issue.


I cannot discern any useful difference between these two CASA .image headers::

    2016-04-25 03:08:55 INFO imhead	##########################################
    2016-04-25 03:08:55 INFO imhead	##### Begin Task: imhead             #####
    2016-04-25 03:08:55 INFO imhead	imhead(imagename="../perseus_synth/perseus_250_to_w51.image",mode="summary",hdkey="",hdvalue="",verbose=True)
    2016-04-25 03:08:55 INFO ImageAnalysis	   
    2016-04-25 03:08:55 INFO ImageAnalysis	Image name       : perseus_250_to_w51.image
    2016-04-25 03:08:55 INFO ImageAnalysis	Object name      : perseus 04
    2016-04-25 03:08:55 INFO ImageAnalysis	Image type       : PagedImage
    2016-04-25 03:08:55 INFO ImageAnalysis	Image quantity   : Intensity
    2016-04-25 03:08:55 INFO ImageAnalysis	Pixel mask(s)    : mask0
    2016-04-25 03:08:55 INFO ImageAnalysis	Region(s)        : None
    2016-04-25 03:08:55 INFO ImageAnalysis	Image units      : Jy/pixel
    2016-04-25 03:08:55 INFO ImageAnalysis	Restoring Beam   : 0.465804 arcsec, 0.465804 arcsec, 0 deg
    2016-04-25 03:08:55 INFO ImageAnalysis	   
    2016-04-25 03:08:55 INFO ImageAnalysis	Direction reference : J2000
    2016-04-25 03:08:55 INFO ImageAnalysis	Spectral  reference : Undefined
    2016-04-25 03:08:55 INFO ImageAnalysis	Velocity  type      : RADIO
    2016-04-25 03:08:55 INFO ImageAnalysis	Rest frequency      : 2.33947e+11 Hz
    2016-04-25 03:08:55 INFO ImageAnalysis	Telescope           : Herschel
    2016-04-25 03:08:55 INFO ImageAnalysis	Observer            : UNKNOWN
    2016-04-25 03:08:55 INFO ImageAnalysis	Date observation    : UNKNOWN
    2016-04-25 03:08:55 INFO ImageAnalysis	   
    2016-04-25 03:08:55 INFO ImageAnalysis	Axis Coord Type      Name             Proj Shape Tile   Coord value at pixel    Coord incr Units
    2016-04-25 03:08:55 INFO ImageAnalysis	------------------------------------------------------------------------------------------------ 
    2016-04-25 03:08:55 INFO ImageAnalysis	0    0     Direction Right Ascension   TAN  2370  158  19:23:41.765  1099.00 -1.552680e-01 arcsec
    2016-04-25 03:08:55 INFO ImageAnalysis	1    0     Direction Declination       TAN  2500  250 +14.30.45.850  1552.00  1.552680e-01 arcsec
    2016-04-25 03:08:55 INFO ImageAnalysis	2    2     Spectral  Frequency                 1    1   2.33947e+11     0.00  1.000000e+09 Hz
    2016-04-25 03:08:55 INFO ImageAnalysis	                     Velocity                                     0     0.00 -1.281456e+03 km/s
    2016-04-25 03:08:55 INFO ImageAnalysis	3    1     Stokes    Stokes                    1    1             I
    2016-04-25 03:08:55 INFO imhead	##### End Task: imhead               #####
    2016-04-25 03:08:55 INFO imhead	##########################################
    2016-04-25 03:09:07 INFO imhead	   
    2016-04-25 03:09:07 INFO imhead	##########################################
    2016-04-25 03:09:07 INFO imhead	##### Begin Task: imhead             #####
    2016-04-25 03:09:07 INFO imhead	imhead(imagename="../simulations/simimage_firsttest.image",mode="summary",hdkey="",hdvalue="",verbose=False)
    2016-04-25 03:09:07 INFO ImageAnalysis	   
    2016-04-25 03:09:07 INFO ImageAnalysis	Image name       : simimage_firsttest.image
    2016-04-25 03:09:07 INFO ImageAnalysis	Object name      :  
    2016-04-25 03:09:07 INFO ImageAnalysis	Image type       : PagedImage
    2016-04-25 03:09:07 INFO ImageAnalysis	Image quantity   : Intensity
    2016-04-25 03:09:07 INFO ImageAnalysis	Pixel mask(s)    : None
    2016-04-25 03:09:07 INFO ImageAnalysis	Region(s)        : None
    2016-04-25 03:09:07 INFO ImageAnalysis	Image units      : Jy/beam
    2016-04-25 03:09:07 INFO ImageAnalysis	Restoring Beam   : 0.21023 arcsec, 0.192666 arcsec, 79.8538 deg
    2016-04-25 03:09:07 INFO ImageAnalysis	   
    2016-04-25 03:09:07 INFO ImageAnalysis	Direction reference : J2000
    2016-04-25 03:09:07 INFO ImageAnalysis	Spectral  reference : Undefined
    2016-04-25 03:09:07 INFO ImageAnalysis	Velocity  type      : RADIO
    2016-04-25 03:09:07 INFO ImageAnalysis	Rest frequency      : 2.33947e+11 Hz
    2016-04-25 03:09:07 INFO ImageAnalysis	Pointing center     :  19:23:41.629000  +14.30.42.380000
    2016-04-25 03:09:07 INFO ImageAnalysis	Telescope           : ALMA
    2016-04-25 03:09:07 INFO ImageAnalysis	Observer            : keflavich
    2016-04-25 03:09:07 INFO ImageAnalysis	Date observation    : 2015/04/23/09:47:44
    2016-04-25 03:09:07 INFO ImageAnalysis	Telescope position: [2.22514e+06m, -5.44031e+06m, -2.48103e+06m] (ITRF)
    2016-04-25 03:09:07 INFO ImageAnalysis	   
    2016-04-25 03:09:07 INFO ImageAnalysis	Axis Coord Type      Name             Proj Shape Tile   Coord value at pixel    Coord incr Units
    2016-04-25 03:09:07 INFO ImageAnalysis	------------------------------------------------------------------------------------------------ 
    2016-04-25 03:09:07 INFO ImageAnalysis	0    0     Direction Right Ascension   TAN  3072  192  19:23:41.629  1536.00 -5.000000e-02 arcsec
    2016-04-25 03:09:07 INFO ImageAnalysis	1    0     Direction Declination       TAN  3072  192 +14.30.42.380  1536.00  5.000000e-02 arcsec
    2016-04-25 03:09:07 INFO ImageAnalysis	2    1     Stokes    Stokes                    1    1             I
    2016-04-25 03:09:07 INFO ImageAnalysis	3    2     Spectral  Frequency                 1    1   2.33947e+11     0.00  1.000000e+09 Hz
    2016-04-25 03:09:07 INFO ImageAnalysis	                     Velocity                                     0     0.00 -1.281456e+03 km/s
    2016-04-25 03:09:07 INFO imhead	##### End Task: imhead               #####
    2016-04-25 03:09:07 INFO imhead	##########################################

if anything, the ALMA file includes *extra* data. Removing this data has no
effect.

The only really substantial difference left is the order of the axes, which
is *not what I put in* for the ALMA data: it puts Stokes as 2 instead of 3
despite the fact that ``CTYPE4='STOKES'`` and ``CTYPE3='FREQ'``.

By doing a round trip FITS->image->FITS->image, I was able to fix the order,
but that is not the underlying problem, apparently.

Could the missing pixel mask be at fault?  It doesn't jive at all with the
error message, so I doubt it.  ``OBSDATE`` is not the problem.


Turns out, the error is that ALMA is the telescope.  I added the header entry::

    ffile[0].header['TELESCOP'] = 'NotReal'

and it Just Worked.  It is approaching the end of my shift, so I think it is
now acceptable to say "what kind of !#$@#$!@% up #@$$@% is that?!".
