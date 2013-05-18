Direct comparison of column-density power spectra
#################################################
:date: 2011-06-29 04:43
:author: Adam (noreply@blogger.com)
:tags: googlepost, analysis
:slug: direct-comparison-of-column-density-power-spectra

I've multiplied the 13CO integrated data cube, the Herschel 500
micron\*, and the BGPS v1.0 and v2.0 by the appropriate conversion
factor to get the maps into units of column density assuming T=20K and
some opacity for the dust maps. BGPS v1 has been multiplied by the 1.5
"correction" factor.
\* The Herschel maps are arbitrarily scaled; I didn't derive an actual
column conversion but just guess-and-checked once or twice until I got
something pretty close.
The power spectra look pretty outstanding:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image1|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image2|`_

.. raw:: html

   </div>

The bumps and wiggles in the 50-200" range are quite well-matched in
Herschel and Bolocam. Some map edge effects are visible in the Herschel
maps, resulting in multi-frequency bumps at small spatial scales. The
Herschel noise floor is also quite evidently lower. Also noteworthy is
that BGPS v1 (scaled up by 1.5) matches the others "pretty well" but is
a worse match, in general, to the Herschel data than is the BGPS v2.
Here are some zoomed-in plots on the inverse scale:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image3|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image4|`_

.. raw:: html

   </div>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image5|`_

.. raw:: html

   </div>

And finally, the 13CO data is totally unrepresentative of the dust data.
There is very little agreement on any scale. This may imply that the
13CO and/or dust temperature is too high, as a decreased T\_D or T\_ex
will decrease 13CO column and increase dust column. However, it also
raises a question - on what scales should dust and CO agree?
This is getting into some real science, perhaps. The shapes of the CO
and dust power spectra disagree: the CO is pretty well-fit by a power
law, while the dust is not. What hypotheses can explain this?

#. There is a systematic temperature difference / preference in which CO
   or dust is hotter on the largest scales.
   -Dust is probably warmer on larger scales, however CO should be less
   abundant / more readily dissociated on these largest, most diffuse
   scales. CO shouldn't exist (or at least, should be underabundant) in
   regions with high temperature. Maybe? This probably needs to be
   quantified.
#. There is a systematic dust opacity difference on large scales
   resulting in lower dust emission.
    -This is almost certainly true: the dust population increases in
   opacity with age, following OH94. Dust on the largest spatial scales
   should not have coagulated / collected ice, leading to a lower
   opacity on the largest scales
    -This may also be true even though CO is present: dust coagulation
   is less efficient than CO formation at n~10^3-10^4 (I think - again,
   off the cuff, but consistent with OH94)
#. The CO overestimates all scales, either because of incorrect bulk
   abundance or temperature considerations.
    This is problematic..... if you drop the CO values at all scales, it
   becomes deficient in the 50-200 arcsecond range, where the dust
   measurements agree quite well
#. There is a preferred distance in both images
    -It is not clear that the observed effects would occur because of
   this
    -It is also quite evident from other analyses that there IS a
   preferred velocity, at least, and it completely dominates all others
   and has the same shape as the integrated power spectrum. So a
   distance effect is most likely ruled out.

.. raw:: html

   </p>

.. _|image6|: http://4.bp.blogspot.com/--uPAgTvMjkk/TgqcjV9uvhI/AAAAAAAAGO4/cOe1iLuF-H0/s1600/powerspectrum_comparison_512_0x1.png
.. _|image7|: http://3.bp.blogspot.com/-1Lupi5MSVpk/TgqcjsPwKFI/AAAAAAAAGPA/D9oNXIHdRtE/s1600/powerspectrum_comparison_512_1x1.png
.. _|image8|: http://2.bp.blogspot.com/-P2pC9RDKUic/TgqckFwVQUI/AAAAAAAAGPI/FU8cUUZe7bc/s1600/powerspectrum_comparison_512_2x1.png
.. _|image9|: http://3.bp.blogspot.com/-ldoGiyzeb2w/TgqhYPqerHI/AAAAAAAAGPQ/E1BFNEhcadw/s1600/powerspectrum_comparison_512_0x1.png
.. _|image10|: http://3.bp.blogspot.com/-algBRWCXB9E/TgqhYgcwsPI/AAAAAAAAGPY/eSbDDcAYvCk/s1600/powerspectrum_comparison_512_1x1.png
.. _|image11|: http://4.bp.blogspot.com/-36H34cVnAPM/TgqhY7f4kAI/AAAAAAAAGPg/HUWvO9nZwuE/s1600/powerspectrum_comparison_512_2x1.png

.. |image0| image:: http://4.bp.blogspot.com/--uPAgTvMjkk/TgqcjV9uvhI/AAAAAAAAGO4/cOe1iLuF-H0/s320/powerspectrum_comparison_512_0x1.png
.. |image1| image:: http://3.bp.blogspot.com/-1Lupi5MSVpk/TgqcjsPwKFI/AAAAAAAAGPA/D9oNXIHdRtE/s320/powerspectrum_comparison_512_1x1.png
.. |image2| image:: http://2.bp.blogspot.com/-P2pC9RDKUic/TgqckFwVQUI/AAAAAAAAGPI/FU8cUUZe7bc/s320/powerspectrum_comparison_512_2x1.png
.. |image3| image:: http://3.bp.blogspot.com/-ldoGiyzeb2w/TgqhYPqerHI/AAAAAAAAGPQ/E1BFNEhcadw/s320/powerspectrum_comparison_512_0x1.png
.. |image4| image:: http://3.bp.blogspot.com/-algBRWCXB9E/TgqhYgcwsPI/AAAAAAAAGPY/eSbDDcAYvCk/s320/powerspectrum_comparison_512_1x1.png
.. |image5| image:: http://4.bp.blogspot.com/-36H34cVnAPM/TgqhY7f4kAI/AAAAAAAAGPg/HUWvO9nZwuE/s320/powerspectrum_comparison_512_2x1.png
.. |image6| image:: http://4.bp.blogspot.com/--uPAgTvMjkk/TgqcjV9uvhI/AAAAAAAAGO4/cOe1iLuF-H0/s320/powerspectrum_comparison_512_0x1.png
.. |image7| image:: http://3.bp.blogspot.com/-1Lupi5MSVpk/TgqcjsPwKFI/AAAAAAAAGPA/D9oNXIHdRtE/s320/powerspectrum_comparison_512_1x1.png
.. |image8| image:: http://2.bp.blogspot.com/-P2pC9RDKUic/TgqckFwVQUI/AAAAAAAAGPI/FU8cUUZe7bc/s320/powerspectrum_comparison_512_2x1.png
.. |image9| image:: http://3.bp.blogspot.com/-ldoGiyzeb2w/TgqhYPqerHI/AAAAAAAAGPQ/E1BFNEhcadw/s320/powerspectrum_comparison_512_0x1.png
.. |image10| image:: http://3.bp.blogspot.com/-algBRWCXB9E/TgqhYgcwsPI/AAAAAAAAGPY/eSbDDcAYvCk/s320/powerspectrum_comparison_512_1x1.png
.. |image11| image:: http://4.bp.blogspot.com/-36H34cVnAPM/TgqhY7f4kAI/AAAAAAAAGPg/HUWvO9nZwuE/s320/powerspectrum_comparison_512_2x1.png
