CASA clean errors related to channels
#####################################
:date: 2015-10-28 16:51
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: clean, casa


When cleaning my ALMA data, especially when trying to `image the full cube (all
channels)
<https://github.com/keflavich/SgrB2_ALMA_3mm_Mosaic/blob/master/script_12m/scriptForImaging.py#L120>`_
when there are multiple SBs
with slightly different frequencies, I see this error frequently:

    No valid data, skip CLEANing this channel

It seems that the channel really is being skipped in many cases.  In the Sgr B2
cube, this wasn't a problem because I unintentionally cleaned only one of the
observations.  For the W51 and Orion data, I tried to `include all of the data
<https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/master/script_12m/scriptForImaging_fullcube.py>`_,
but that is causing problems.  Perhaps CASA does not work at all when 'channel'
is specified and the channels aren't aligned?  Or maybe it only accepts channels
when all channels exist?

I've now redone the 'full cube' imaging to separately image the two SBs in W51.
I'll see if that works...

Nope, the resulting error is much worse::

    Log:
    2015-10-28 15:49:01     INFO    imager::clean() Fitted beam used in restoration: 1.07809 by 0.913862 (arcsec) at pa -63.3899 (deg)
    2015-10-28 15:49:01     INFO    imager::iClean()        Restoring Image(s) with the clean-beam
    2015-10-28 15:49:02     SEVERE  clean::::       An error occurred running task clean.

    Terminal:
    *** Error ***  The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
    2015-10-28 15:49:02     SEVERE  clean::::       An error occurred running task clean.

This is an indication of a major underlying python bug.
