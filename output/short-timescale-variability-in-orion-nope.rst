Short timescale variability in Orion?  Nope.
############################################
:date: 2012-11-19 17:07
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post

.. raw:: html

   <div dir="ltr" style="text-align: left;">

I attempted to use TripleSpec finder / guider images to search for
variability  on short (~5s) timescales in the Orion Nebula region.  This
project was an offshoot of the related
`http://adamginsburg.blogspot.com/2012/10/using-guider-images-to-achieve.html`_.
 I successfully matched the images using a particular catalog & the
ever-cool \ `astrometry.net`_\ with a great deal of assistance from
`Dustin Lang`_ and some from `David Hogg`_.  I'll post details of that
process later; it proved challenging but will DEFINITELY be useful again
in the future.  Short story: I had to build my own indices, then fit
twice - once for the first match, once after distortion was applied to
re-extract the sources in the right location.
Conveniently, one of the products output by the astrometry.net code is
ra,dec locations and fluxes (background subtracted) for all of the
identified sources.  So, I used a simple script to match all sources
within 2" of a known source from my input catalog and generate
timestream data.  It took about an hour of processing (nested for loops
- awful, but the only obvious choice at first.  Half of the time was
probably file IO anyway).
I now had a few hundred timestreams of Orion stars.  At this point, I
hadn't done any kind of quality control, which was obviously a problem
because the Trapezium and neighbors were clearly saturated.  Also, there
are known hot pixels that will drive some stars into weird behavior.
 But I ignored all of that.  All I did for quality control was reject
stars with more than about 5% missing data.
I elected to go straight for PCA analysis.  I assumed the primary
component (the most correlated component) would be from the atmosphere,
which is almost certainly true.  Subtracting that off (shown in the
notebook linked below) left some clearly correlated components left over
- some of these are instrumental, others are correlated backgrounds,
others are correlated saturation levels.  I don't honestly know what all
of the components are, but I DO know that correlated components are very
unlikely to be intrinsic phenomena - stellar brightness isn't
correlated.
So I tried to cut out ALL correlated components.  However, I think in
the process I probably removed any useful information - even
un-correlated signal should probably have a high amplitude (if it's
interesting...) that will get removed through the process I used.
 Nonetheless, I probably have some upper limits on the 5s scale
variability of these stars in K-band.  Not enough to do anything like
asteroseismology, but it was worth a day's effort.
Here's the ipython notebook (gist & nbviewer) for those interested:
`https://gist.github.com/4109329`_
`http://nbviewer.ipython.org/4109329/`_

.. raw:: html

   </div>

.. raw:: html

   </p>

.. _`http://adamginsburg.blogspot.com/2012/10/using-guider-images-to-achieve.html`: http://adamginsburg.blogspot.com/2012/10/using-guider-images-to-achieve.html
.. _astrometry.net: http://astrometry.net/
.. _Dustin Lang: http://www.astro.princeton.edu/~dstn/
.. _David Hogg: http://hoggresearch.blogspot.com/2012/10/time-for-astrometrynet-to-rise-again.html
.. _`https://gist.github.com/4109329`: https://gist.github.com/4109329
.. _`http://nbviewer.ipython.org/4109329/`: http://nbviewer.ipython.org/4109329/
