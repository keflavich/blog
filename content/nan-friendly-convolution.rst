NaN-friendly convolution
########################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, python, code

NaN-friendly convolution is important for, e.g., masked data sets in
which you want to interpolate across the masked region.
Astropy has gained this functionality with pull request 155:
`https://github.com/astropy/astropy/pull/155
`_\ but this is a "direct" convolution parallel to IDL's 'convol'
routine.
My FFT-based version now works in N dimensions and is a little cleaner:
`http://code.google.com/p/agpy/source/browse/trunk/AG\_fft\_tools/convolve\_nd.py
`_
I'm still working on writing unit tests, and I'm really not sure what
the "correct" behavior at the edges is for the different cases... right
now, it seems counterintuitive to me, but the code is doing what I
expect it to.
Also, Boxcar kernels always result in shifts for me... they're never
supposed to. This is a bug.
Currently, other links to these codes:
`http://stackoverflow.com/questions/1100100/fft-based-2d-convolution-and-correlation-in-python/8454010#8454010`_

.. _`https://github.com/astropy/astropy/pull/155
`: https://github.com/astropy/astropy/pull/155
.. _`http://code.google.com/p/agpy/source/browse/trunk/AG\_fft\_tools/convolve\_nd.py
`: http://code.google.com/p/agpy/source/browse/trunk/AG_fft_tools/convolve_nd.py
.. _`http://stackoverflow.com/questions/1100100/fft-based-2d-convolution-and-correlation-in-python/8454010#8454010`: http://stackoverflow.com/questions/1100100/fft-based-2d-convolution-and-correlation-in-python/8454010#8454010
