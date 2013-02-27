Research Idea: Stacking Finders
###############################
:date: 2012-09-20 20:07
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, research ideas, observing

.. raw:: html

   <div dir="ltr" style="text-align: left;">

Idea: Stack all of the finders from spectroscopic observations.  Finder
images tend to be on lower-quality CCDs with no filter, but they
frequently produce very deep observations.  For example, the open K-band
finder on TripleSpec (though it's technically not a CCD).

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

In order to stack them, you would need to mask out the bad pixels
(already done) and compute astrometic solutions for the CCD.  Un-warping
the images will take some work, but there should be plenty of
information available from thousands of observations of different fields
to make this computation nearly ideal.  Similarly, it should be possible
to calibrate different pixels on the imager based on response to 2MASS
standards.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Applications?  Very deep imaging of spectroscopic targets.  Short- and
long-term variability (typical finder cadence is ~a few seconds).  Deep
imaging around stars and galaxies of interest - probably far deeper than
you could get with classical observing requests.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

This project should be achievable by a motivated undergraduate, but I
think the tools for astrometric solutions need to be in place first.
 Astrometry.net is a great tool for this, but I think operates on
spatial scales that are too large.  Once basic astrometric solutions are
available (e.g., pointing center for the image), I think IRAF tools
could be automated to compute the complete solution, which would then be
applied to all images.  

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Calibration might end up being the most challenging component, since
there is variable atmospheric emission (absorption) that is not filtered
by the finder.  Depending on the application, though, large calibration
errors may be acceptable.  i.e., for deep nebular observations,
morphology will be more important than absolute brightness, since the
line responsible for the brightness cannot be directly determined.
 Whereas, for variability, calibration is important, but it can be
computed directly from other stars in the field.

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </p>

