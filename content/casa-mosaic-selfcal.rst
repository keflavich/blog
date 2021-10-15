Self-calibration of Sgr B2 Mosaic
#################################
:date: 2015-10-14 14:30
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, ALMA, Sgr B2

The Sgr B2 ALMA data from project 2013.1.00269.S has imaging problems around
the brightest sources, especially Sgr B2 M.
Crystal Brogan & Todd Hunter gave some useful advice, essentially the following:

 * the line forest is causing trouble, so line-containing regions of the spectrum
   must be excluded when mapping
 * there is some nasty curvature in the spectral baseline that needs to be removed
   probably by flagging out some of the data
 * Self-calibration is needed to exceed a dynamic range ~100

Todd developed a `fitcontinuum.py` script to address the first point, but I ended up
doing this custom (script__) because of the problem introduced by the second point.

__ https://github.com/keflavich/SgrB2_ALMA_3mm_Mosaic/blob/master/script_12m/test_split_spw1.py

To exclude the lines, I had to use *frequency-based* selection, not channel based, because my
spectral windows from different dates were offset by 10 MHz.  The approach to use in CASA is
ugly: you flag the line-containing data, then split (and in splitting, average) the continuum
into another MS.  From there, a phase-only selfcal is straigtforward (script__).

__ https://github.com/keflavich/SgrB2_ALMA_3mm_Mosaic/blob/master/script_12m/selfcal_spw1_center.py

.. image:: |static|/images/sgrb2/selfcal_compare.png
   :width: 800px
