PSDs, cross-correlation...
##########################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, python, agpy

scipy is capable of doing fft-base cross-correlation, convolution, etc.,
but it requires the stsci package, which is not generally easy to
install. For that matter, scipy can be a pain some of the time. So agpy
now includes a 2D cross-correlation code and a power spectrum / power
spectral density code. These are pure-numpy codes that should be easy to
use without any other bothersome dependencies.
EDIT: I have them check for scipy (which can cause crashes if you have a
bad scipy install, e.g. 32 bit executables on a 64 bit system) because
scipy uses FFTW and numpy appears not to. Also, this code & related
stuff has been `discussed on astrobetyter`_
`agpy`_
`correlate2d`_
`psds`_

.. _discussed on astrobetyter: http://www.astrobetter.com/fourier-transforms-of-images-in-python/
.. _agpy: http://code.google.com/p/agpy/
.. _correlate2d: http://code.google.com/p/agpy/source/browse/trunk/agpy/correlate2d.py
.. _psds: http://code.google.com/p/agpy/source/browse/trunk/agpy/psds.py
