Minor mystery resolved: Perseus cal curve
#########################################
:date: 2010-06-07 22:32
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, perseus, calibration
:slug: minor-mystery-resolved-perseus-cal-curve

When I started working on the Perseus data again, I decided to use the
Enoch 2006 calibration curve directly. However, it has a very different
form than all other epochs. The reason, as revealed below, is that it
was not forced through 0,0. Additionally, all of the BGPS data was
observed with mean DC ~ 2-3 V, while the Perseus data was observed with
mean DC 4-5 V, so the relevant regime is in a very different location.
The reference DC bias was much lower, ~2.15 V vs. 4.6 V in the 2005-2007
BGPS and 2.6 V in the 2009 BGPS.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_

.. raw:: html

   </div>

.. raw:: html

   </p>

.. _|image1|: http://3.bp.blogspot.com/_lsgW26mWZnU/TA1yfdAS7BI/AAAAAAAAFtU/XvYiDQKi-cM/s1600/CalCurveComparison.png

.. |image0| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TA1yfdAS7BI/AAAAAAAAFtU/XvYiDQKi-cM/s320/CalCurveComparison.png
.. |image1| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TA1yfdAS7BI/AAAAAAAAFtU/XvYiDQKi-cM/s320/CalCurveComparison.png
