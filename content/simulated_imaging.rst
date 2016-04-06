Simulated Observations of Perseus in W51
########################################
:date: 2016-02-27 10:40
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, ALMA

The W51 and Sgr B2 ALMA mosaics contain ~50 and ~150 pointlike sources,
respectively.  However, they have pretty miserable high-noise regions
such that determining completeness is a serious challenge.

To determine completeness in a means comparable to other observations,
I have therefore been using the Gould's Belt Survey Perseus data
as an input to do synthetic observations.

It turns out this is technically challenging because CASA does some 
`strange things <{filename}/casa_simulating.rst>`_ when importing files.

I finally got a `version
<https://github.com/keflavich/W51_ALMA_2013.1.00308.S/commit/b046ff5c82992ef44a1dbaac303fcc6497511142>`__
working.

Important details when reading in a FITS file:

 * The header *must* be fully populated with a 4-dimensional WCS.  If stokes or
   frequency are missing, CASA will choke with uninformative errors such as:

   2016-02-26 11:25:24	SEVERE	Simulator::createSkyEquation() (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Simulator.cc, line 2200)	Caught exception: (/Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Simulator.cc : 2266) Failed AlwaysAssert spectralIndex>=0
   2016-02-26 11:25:24	SEVERE	Simulator::predict() (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Simulator.cc, line 2118)	Failed to create SkyEquation

   and

   2016-02-26 11:27:36	SEVERE	Simulator::predict() (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Simulator.cc, line 2118)	Caught exception: (/Users/rpmbuild/gradle/workdir/casasources/release-4_5/casacore/coordinates/Coordinates/CoordinateSystem.cc : 793) Failed AlwaysAssert which < nCoordinates() && coordinates_p[which]->type() == Coordinate::STOKES
 * Flux units should be in Jy/beam.  Other flux units *may* be acceptable (e.g.,
   MJy/sr, Jy/pixel), but their behavior is not entirely predictable.  I did not
   get out the expected values when I used MJy/sr as input, but I did not pursue
   further why this happened.  Using Jy/beam, and ensuring that the units were correctly
   set to Jy/beam in the file (by scaling them in the FITS image before importing),
   I got the expected results.
 * CASA apparently does not read beam information from headers.  You need to include the
   beam information when doing importfits, e.g.:

      beam=["{0}deg".format(hdr['BMAJ']),
            "{0}deg".format(hdr['BMIN']),
            "{0}deg".format(hdr['BPA'])]

 * CASA will happily read a FITS file into a ``.image`` that cannot be used by
   other casa routines.  You will not get an exception until you try a later
   step.

Once the FITS image is read into a CASA ``.image``, *if* it has the CASA-expected
units and dimensions, you can use ``sm.predict`` to fourier transform the data
and sample it onto the UV grid in your ``.ms`` file:: 

    sm.openfromms("file.ms")
    sm.setvp() # "set voltage pattern": not clear if this is needed
    success = sm.predict("myfile.image")
    sm.done()
    sm.close()

This (seems to) populate the *data* column, not the model column as I had
originally expected.  Therefore, be warned!  DO NOT DO THIS TO YOUR ORIGINAL
DATA!  It will probably overwrite it.

Once your ``.ms`` file is populated, you can clean it as normal.  Some
examples:

.. image:: |filename|/images/casa/perseus_in_w51_imaging.png
   :width: 600px
