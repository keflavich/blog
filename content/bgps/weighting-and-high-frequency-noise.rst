Weighting and high-frequency noise
##################################
:date: 2008-11-15 00:41
:author: Adam (noreply@blogger.com)
:tags: googlepost, weighting
:slug: weighting-and-high-frequency-noise

.. image:: http://1.bp.blogspot.com/_lsgW26mWZnU/SR4DzVCz1WI/AAAAAAAADfk/cJ70OPeqEzg/s400/psds.png
Image of PSDs (with no normalization) of the raw (blue), delined and
exponential and polynomial subtracted (white), the noise timestream
(yellow), and the data (cyan).
The good: It looks like all of the powerline noise got into the noise
timestream and almost none in the data.
The bad: weighting is based on the noise timestream so it's possible
that the weights aren't quite right as a result
The weird: the data PSD. What's up with that? Apparently I'm
preferentially subtracting certain scales but I don't know why, unless
deconvolution is at fault.
Edit/Update: The deconvolution is definitely at fault. Here's the same
scan done without deconvolution:
.. image:: http://3.bp.blogspot.com/_lsgW26mWZnU/SR4ZM6FPfrI/AAAAAAAADf0/baHOQwedeqs/s400/psds2.png
It should have been obvious; the cyan in the first plot is the PSD of
the deconvolution straight up, and that should have no high-frequency
structure...

.. _|image2|: http://1.bp.blogspot.com/_lsgW26mWZnU/SR4DzVCz1WI/AAAAAAAADfk/cJ70OPeqEzg/s1600-h/psds.png
.. _|image3|: http://3.bp.blogspot.com/_lsgW26mWZnU/SR4ZM6FPfrI/AAAAAAAADf0/baHOQwedeqs/s1600-h/psds2.png

