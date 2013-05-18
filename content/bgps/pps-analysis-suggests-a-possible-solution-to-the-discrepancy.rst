PPS analysis: suggests a possible solution to the discrepancy
#############################################################
:date: 2010-06-21 18:17
:author: Adam (noreply@blogger.com)
:tags: googlepost, analysis, discrepancy
:slug: pps-analysis-suggests-a-possible-solution-to-the-discrepancy

The comparisons I mentioned in the previous post are sort of done.  They
are pretty suggestive of a solution to the "flux recovery problem" we
think must be true.  However, even if it is a solution, it doesn't
really solve the problem completely.
It looks like v1.0 should be scaled up by a factor of 1.3-1.4 (not
1.5).  v2.0 is consistent with the PPS sources to within 5%, and might
even be slightly too high.
The comparison was done by taking the flux in a 60" radius aperture
(equivalent to bolocat 120" diameter apertures) and subtracting off the
background measured in a 120" radius annulus around the source.  Without
the background subtraction, these numbers would look very different: in
the science fields, most of the sources sit on an extended background. 
Even though the "background flux" isn't recovered in the PPS fields, it
should contribute to the source background because it is involved in the
atmosphere subtraction (it's sort of "already subtracted" so you have to
subtract from the science fields).

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_\ `|image1|`_

.. raw:: html

   </div>

Next step: direct comparison between v1.0 and v2.0.  Pixel by pixel,
aperture, and powerspectrum

.. raw:: html

   </p>

.. _|image2|: http://3.bp.blogspot.com/_lsgW26mWZnU/TB-rPT7MLdI/AAAAAAAAFws/7oWTt3FOF-M/s1600/BGPS_correction_factors.png
.. _|image3|: http://2.bp.blogspot.com/_lsgW26mWZnU/TB-rQId8G_I/AAAAAAAAFw0/NUJKQO_5zI4/s1600/BGPS_correction_factor_histograms.png

.. |image0| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TB-rPT7MLdI/AAAAAAAAFws/7oWTt3FOF-M/s320/BGPS_correction_factors.png
.. |image1| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TB-rQId8G_I/AAAAAAAAFw0/NUJKQO_5zI4/s320/BGPS_correction_factor_histograms.png
.. |image2| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TB-rPT7MLdI/AAAAAAAAFws/7oWTt3FOF-M/s320/BGPS_correction_factors.png
.. |image3| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TB-rQId8G_I/AAAAAAAAFw0/NUJKQO_5zI4/s320/BGPS_correction_factor_histograms.png
