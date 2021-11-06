CASA Cross-Calibration Application
##################################
:date: 2019-08-22 13:06 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: tags

On several independent occasions, I've had data where the continuum is bright
enough to self-calibrate, but the lines aren't.  In these cases, I want to apply
the continuum-derived selfcal solutions to the line data.

In all of these cases, I have several independent execution blocks that I've
split and downsampled before combining to make the continuum image.

I got stuck trying to make this happen, but we reconvened on the topic in early
2021, and Manuel Fernandez and Roberto Galvan-Madrid and I came up with this
tool to match spectral windows in a concatenated data set to the appropriate
windows in the original:
https://github.com/ALMA-IMF/reduction/blob/master/misc/applycal_tests.py
