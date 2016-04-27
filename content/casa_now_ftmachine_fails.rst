CASA simulated imaging: now FTMachine is whining
################################################
:date: 2016-04-26 15:12
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa, clean, simulation


`A few days ago <|filename|/casa_simulation_debugging.rst>`__
I apparently got my broken simulator working again.  Today, in my first
attempt to repeat those results, I... have broken it again.::

    WARN	FTMachine::initMaps	No overlap in frequency between image channels and selected data found for this FTMachine
    WARN	FTMachine::initMaps+	 Check your data selection and image parameters if you end up with a blank image

This warning is not a simple warning, it means nothing is being done.  My
images are empty, pure noise (which, interestingly enough, is far from
gaussian).

I have encountered these errors `before
<|filename|/separating_line_and_continuum.rst>`, but unfortunately did not
resolve the issue.

Turns out, the difference was the .ms file I used,
``continuum_7m12m_noflag.ms``, which works, vs the useful one,
``w51_contvis_selfcal_3.ms``, which doesn't.

Checking out their headers, the continuum image does overlap with the
data but the selfcal version doesn't.  Wonderful.  Now I'll bet it's only
populating one channel at a time when I invert too...

This leads me to try::

    split(vis='w51_contvis_selfcal_3.ms', outputvis='simulation_continuum.ms', datacolumn='data', width=100)

then use (borrowed from `this tool
<https://github.com/radio-astro-tools/sandbox/blob/master/casa_7m12m_tools/weight_density_uv_plot.py>`__)::

    mymsmd = msmdtool()
    mymsmd.open(vis)

    reffreq = "{value}{unit}".format(**mymsmd.reffreq(spw)['m0'])

to get the frequency to write into the header each time.

At a glance, just changing the frequency of the FITS file to match the first
SPW seems to work.  However, I haven't yet examined whether the other SPWs
are populated.

This assumption proved wrong.  No, it simply doesn't work.  The warnings went away,
but the output images are empty.  Also, the noise went up, which I don't understand.

Imaging just spw1 kind of worked, but resulted in an image with the wrong
resolution by factors of many.

Trying to loop over all spws failed miserably, resulting in *nothing* being done by
predict and *no warning* being given.

OK, finally, solution is to make sure CDELT is large enough to cover *all* SPWs.


Another important note: Jy/beam and Jy/pixel inputs into CASA result in identical images.
In both cases, they are wrong images: they correspond to multiplying the input data by
factors of at least 100.  Therefore, my conclusion now is that I have to divide everything
by some fact, which I *sincerely* hope is ppbeam, to correct the data.


It looked vaguely like the divide-by-ppbeam trick worked, but my tests kept coming up funny
because the *original* images were scaled down.  So I tried unscaling them.  Somehow,
without changing anything about the headers, I landed on another failed predict error::

    2016-04-27 19:14:42	SEVERE	Simulator::createSkyEquation() (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Simulator.cc, line 2200)	Caught exception: (/Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Simulator.cc : 2266) Failed AlwaysAssert spectralIndex>=0
    2016-04-27 19:14:42	SEVERE	Simulator::predict() (file /Users/rpmbuild/gradle/workdir/casasources/release-4_5/code/synthesis/MeasurementEquations/Simulator.cc, line 2118)	Failed to create SkyEquation

Spectral Index?  I encountered this `previously
<|filename|/casa_simulating.rst>`__, but didn't record any solution.
After checking the header, it appears that my files are *now* missing axes 3 and 4.
I didn't make any changes that should cause this; the axes are just not being added
on importfits despite being forcibly added in the command.

The problem is unfortunately not in the FITS part, but again in the CASA part.
Re-importing the FITS file to .image without forcing ``defaultaxes`` again just
broke it.
