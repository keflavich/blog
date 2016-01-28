CASA Selfcal: Good & Awful
##########################
:date: 2016-01-28 09:20
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: clean, selfcal


Self-calibration is necessary for some images to get a decent dynamic range or
to see anything at all in the images.  So, I did some tests using self-cal on
the central field of Sgr B2 (`source
<https://github.com/keflavich/SgrB2_ALMA_3mm_Mosaic/blob/master/script_12m_te/selfcal_centralfield.py>`_)
and it worked great:

.. image:: |filename|/images/casa/sgrb2_selfcal_good.png
   :width: 600px

That image is actually from `self-calibrating the whole field
<https://github.com/keflavich/SgrB2_ALMA_3mm_Mosaic/blob/master/script_12m_te/selfcal_continuum.py>`_,
which also worked great.  Except, it deleted all the flux outside of the bright regions:

.. image:: |filename|/images/casa/sgrb2_selfcal_bad.png
   :width: 600px

This is extremely, amazingly, terribly awful.  It is just deleting flux!  I had
previously thought that the ``applyonly`` option would only apply solutions
that it actually found, but that appears not to bt true.  Instead, it seems
that even phase solutions with *no* signal are being applied, which effectively
removes everything from the image.  I could have understood if this was happening
to amplitude self-calibration, but I can't understand how it is happening with
phase self-cal.
