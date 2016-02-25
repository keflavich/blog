CASA Simulation
###############
:date: 2016-02-25 10:27
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, ALMA

More frustration with CASA:

 * If you try to load a FITS image into a CASA .image, beware that it is likely
   to have incorrect units.  Round-tripping between .image and .fits doesn't
   work well, because CASA always assumes that CDELT is in radians even when it
   is explicitly set to be degrees.


The simulator gives this error message if I try to load an image:

    sm.setvp()
    sm.predict(perseus_casa_image)

    2016-02-25 09:26:34	SEVERE	Simulator::predict() (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Simulator.cc, line 2118)	Caught exception: TiledShape: #elements in shape and tileShape differ

My best guess is that CASA doesn't understand how to handle 2D images with 3D
headers.  However, the sensible workaround of expanding the image to 3D does
not work.

Re-importing after exporting gets yet another different image.  After
re-importing an image that was exported to FITS, I get a new error:

    Failed AlwaysAssert spectralIndex>=0 2016-02-25 09:37:35

which is rather strange since the spectral index is a physical quantity.

There is also the lovely message:

    2016-02-25 09:55:27 INFO importfits	No usable restoring beam information found.
    
for a header that contains these lines:

    BMAJ    =   1.293900184840E-04
    BMIN    =   1.293900184840E-04
    BPA     =   0.000000000000E+00


The image might finally be right, but now I can't find any way to convert it to
a model.  If I try to ``ft`` the model, I get:

    2016-02-25 10:54:54	SEVERE	ft::imager::ft() (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Imager.cc, line 4488)	Exception: (/Users/rpmbuild/gradle/workdir/casasources/release-4_5/casacore/coordinates/Coordinates/CoordinateSystem.cc : 777) Failed AlwaysAssert which < nCoordinates() && coordinates_p[which]->type() == Coordinate::SPECTRAL

which probably means that CASA doesn't know how to turn a single-band continuum
image into a model for a multi-frequency .ms (which is all .ms's, including
continuum, in the ALMA world).
