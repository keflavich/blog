Downsampling has serious negative effects on the data
#####################################################
:date: 2011-01-20 20:16
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, mapping, calibration
:slug: downsampling-has-serious-negative-effects-on-the-data

Background: Downsampling is performed using Old Pipeline code called
``process_ncdf``. All BGPS data was downsampled by a factor of 5
before mapping because of data size concerns. I did this 'blindly'
(i.e., just
accepted that I should) because James said I could.
However, I had previously noted that the pointing files could not be
done with
downsampled data because the beams 'looked funny' or something along
those
lines; it may also have been a simple map sampling issue in which not
all
pixels were filled with a downsampled image.
Anyway, I decided to go back and quantify the effects. The plots below
are from the
single "pointing-style" observation of OMC1 from 2009. The units are
volts. 'ds1' indicates
sampling at 0.02 seconds, 'ds5' indicates sampling every 0.1 seconds.
The scan rate was
120"/s.

--------------

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

`|image0|`_

.. raw:: html

   </div>

The beam sizes were measured from the autocorrelation maps. However,
because there is structure on many scales
in this map, I had to use a rather ad-hoc method to remove the
correlated structure. I fitted a gaussian
to the elliptical northwest-southeast structure, removed it, then fitted
a gaussian to the remaining circular
thing in the center, which is approximately the beam.
If I fit the "beam" gaussian with an ellipse, I get:
Beamsize 1\_1: 36.15,26.23
Beamsize 1\_5: 48.39,30.21
With a circle:
Beamsize 1\_1: 29.51
Beamsize 1\_5: 35.31

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image1|`_

.. raw:: html

   </div>

.. raw:: html

   <center>

The ds1 and ds5 images compared.

.. raw:: html

   </center>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image2|`_

.. raw:: html

   </div>

.. raw:: html

   <center>

The PSDs of the two images (on identical grids). Note that ds5 loses
power at small spatial scales, 50% at 40"!

.. raw:: html

   </center>

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image3|`_

.. raw:: html

   </div>

.. raw:: html

   <center>

The pixel-pixel plot with a fit that shows a 10% overall flux loss
(best-fit).

.. raw:: html

   </center>

.. raw:: html

   </p>

.. _|image4|: http://2.bp.blogspot.com/_lsgW26mWZnU/TTiWWSS-JVI/AAAAAAAAF24/4m2SFfwWkmA/s1600/omc1_dstest_autocorrfits.png
.. _|image5|: http://1.bp.blogspot.com/_lsgW26mWZnU/TTiWWKeGbJI/AAAAAAAAF2w/jOEmOnDa1hw/s1600/omc1_dstest_images.png
.. _|image6|: http://3.bp.blogspot.com/_lsgW26mWZnU/TTiWWlzyWKI/AAAAAAAAF3A/nPCN-C0e3Jo/s1600/omc1_dstest_psds.png
.. _|image7|: http://4.bp.blogspot.com/_lsgW26mWZnU/TTiWWl3j3dI/AAAAAAAAF3I/Ef3WHEv5oXU/s1600/omc1_dstest_pixel-pixel.png

.. |image0| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TTiWWSS-JVI/AAAAAAAAF24/4m2SFfwWkmA/s400/omc1_dstest_autocorrfits.png
.. |image1| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TTiWWKeGbJI/AAAAAAAAF2w/jOEmOnDa1hw/s400/omc1_dstest_images.png
.. |image2| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TTiWWlzyWKI/AAAAAAAAF3A/nPCN-C0e3Jo/s400/omc1_dstest_psds.png
.. |image3| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TTiWWl3j3dI/AAAAAAAAF3I/Ef3WHEv5oXU/s400/omc1_dstest_pixel-pixel.png
.. |image4| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TTiWWSS-JVI/AAAAAAAAF24/4m2SFfwWkmA/s400/omc1_dstest_autocorrfits.png
.. |image5| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TTiWWKeGbJI/AAAAAAAAF2w/jOEmOnDa1hw/s400/omc1_dstest_images.png
.. |image6| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TTiWWlzyWKI/AAAAAAAAF3A/nPCN-C0e3Jo/s400/omc1_dstest_psds.png
.. |image7| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TTiWWl3j3dI/AAAAAAAAF3I/Ef3WHEv5oXU/s400/omc1_dstest_pixel-pixel.png
