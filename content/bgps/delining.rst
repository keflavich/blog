Delining
########
:date: 2011-02-03 04:54
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, pipeline, deline
:slug: delining

Delining refers to the process of removing electronic noise that is
aliased to
particular frequencies by the discrete sampling of the data. Typical
electronic noise is at 60 Hz with some width. It gets aliased to these
frequencies:
``linefreqs = [10.05+findgen(10)*1.2,10.05-((findgen(7)+1))*1.2]``
The 10.05 Hz and 20.10 Hz are the worst in most cases, and they are
wider. For
the above lines, we "remove" a bandwidth of 0.09 Hz by averaging over
the
neighboring 0.5 Hz on either side. For the wider lines, we remove 0.5 Hz
by
averaging over the neighboring 1.5 Hz on either side.
There are a few new things about the delining process that did not exist
in James' old version:

#. The wide-band lines are removed
#. A check is performed before removing the lines - they are only
   removed if the line region mean is
   2-sigma above the average region (as computed via median and mad)
#. The replaced noise is computed via median/mad, and the new noise
   level is set 5x lower than in the
   neighboring region

--------------

Now, some examples:

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

`|image0|`_ `|image1|`_

.. raw:: html

   </div>

The timestream (left) and PSD (right) of a "pretty good" bolometer.
There is a lot of noise in lines, but note that the peak power is 2-3
orders of magnitude below the PSD peak. In this case the "Power" is in
Jy. There is little astrophysical information below ~14" (9 Hz), and
there should be none below 7.2" (17 Hz), but there is plausibly
information at these scales. It therefore makes sense to save as much
information as possible. As can be seen in the delined PSD, the peaks
drop by a substantial fraction, but not all the way - that's because
these lines are wider than typically observed. Unfortunately, I don't
have any really good ideas about how to fix this issue - I think fitting
gaussians to each line, while attractive, is going to be prohibitively
expensive in both programmer and processor time. However... it would be
a very interesting project to undertake. In the timestream, it can be
seen that the RMS drops substantially when the lines are filtered out
(note that the timestream is strongly dominated by large-scale
structure, so 'substantial' is really based on the RMS of the lines
removed).

.. raw:: html

   <div class="separator" style="clear: both; text-align: left;">

`|image2|`_ `|image3|`_

.. raw:: html

   </div>

The next two plots look identical to the previous ones. In principle,
they include the wide-band delining. However, in this case, the
satellite lines to either side of the 10 Hz line are too strong and
prevent identification of the 10 Hz line. This is unfortunate, again,
but no obvious solution presents itself.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image4|`_ `|image5|`_

.. raw:: html

   </div>

Now we come to a truly problematic bolometer. The lines completely
dominate the power spectrum. Narrow line removal fails.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image6|`_ `|image7|`_

.. raw:: html

   </div>

Wide line removal does a much, much better job, dropping the RMS by an
order of magnitude.... but the bolometer probably still needs to be
removed, since the astrophysical signal is 2-3 orders of magnitude below
that.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image8|`_ `|image9|`_

.. raw:: html

   </div>

The 2010 data had much worse line noise and had to be delined. JS
accomplished this by throwing out all data above a certain frequency,
but I prefer the delining approach. It is clearly effective, but again
leaves much to be desired. Should the flagged bandwidth be increased?
What about the extra lines around 18 Hz?

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image10|`_ `|image11|`_

.. raw:: html

   </div>

Again, the wide line flagging fails because of the satellite lines.

.. raw:: html

   </p>

.. _|image12|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUisqDHJ08I/AAAAAAAAF58/BpgnudfdAAw/s1600/deline_timestreams_003.png
.. _|image13|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUisqWN6ueI/AAAAAAAAF6E/yAka7dlomjo/s1600/deline_psds_003.png
.. _|image14|: http://3.bp.blogspot.com/_lsgW26mWZnU/TUisq6D55wI/AAAAAAAAF6M/PZ4hyu5FkZM/s1600/deline_10hz_timestreams_003.png
.. _|image15|: http://3.bp.blogspot.com/_lsgW26mWZnU/TUisrWpL7yI/AAAAAAAAF6U/tSsL5Jc4n-A/s1600/deline_10hz_psds_003.png
.. _|image16|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUixLZbVHPI/AAAAAAAAF6c/xCWLpb9CKX4/s1600/deline_timestreams_004.png
.. _|image17|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUixL8APCQI/AAAAAAAAF6k/j8FyKbgOdDo/s1600/deline_psds_004.png
.. _|image18|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUixMjNxbkI/AAAAAAAAF6s/Hr8ouprcMpY/s1600/deline_10hz_timestreams_004.png
.. _|image19|: http://1.bp.blogspot.com/_lsgW26mWZnU/TUixNMO2NsI/AAAAAAAAF60/ZAsirbb25QY/s1600/deline_10hz_psds_004.png
.. _|image20|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUizkq9x4TI/AAAAAAAAF68/2xYY86d6aTQ/s1600/deline_timestreams_001.png
.. _|image21|: http://2.bp.blogspot.com/_lsgW26mWZnU/TUizlH0XvMI/AAAAAAAAF7E/ptDb5I3os6A/s1600/deline_psds_001.png
.. _|image22|: http://3.bp.blogspot.com/_lsgW26mWZnU/TUizln1mSCI/AAAAAAAAF7M/hTkZRUU3-ck/s1600/deline_10hz_timestreams_001.png
.. _|image23|: http://4.bp.blogspot.com/_lsgW26mWZnU/TUizmdrMkgI/AAAAAAAAF7U/-dlB4u30hBo/s1600/deline_10hz_psds_001.png

.. |image0| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUisqDHJ08I/AAAAAAAAF58/BpgnudfdAAw/s400/deline_timestreams_003.png
.. |image1| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUisqWN6ueI/AAAAAAAAF6E/yAka7dlomjo/s400/deline_psds_003.png
.. |image2| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUisq6D55wI/AAAAAAAAF6M/PZ4hyu5FkZM/s400/deline_10hz_timestreams_003.png
.. |image3| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUisrWpL7yI/AAAAAAAAF6U/tSsL5Jc4n-A/s400/deline_10hz_psds_003.png
.. |image4| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUixLZbVHPI/AAAAAAAAF6c/xCWLpb9CKX4/s400/deline_timestreams_004.png
.. |image5| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUixL8APCQI/AAAAAAAAF6k/j8FyKbgOdDo/s400/deline_psds_004.png
.. |image6| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUixMjNxbkI/AAAAAAAAF6s/Hr8ouprcMpY/s400/deline_10hz_timestreams_004.png
.. |image7| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUixNMO2NsI/AAAAAAAAF60/ZAsirbb25QY/s400/deline_10hz_psds_004.png
.. |image8| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUizkq9x4TI/AAAAAAAAF68/2xYY86d6aTQ/s400/deline_timestreams_001.png
.. |image9| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUizlH0XvMI/AAAAAAAAF7E/ptDb5I3os6A/s400/deline_psds_001.png
.. |image10| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUizln1mSCI/AAAAAAAAF7M/hTkZRUU3-ck/s400/deline_10hz_timestreams_001.png
.. |image11| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUizmdrMkgI/AAAAAAAAF7U/-dlB4u30hBo/s400/deline_10hz_psds_001.png
.. |image12| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUisqDHJ08I/AAAAAAAAF58/BpgnudfdAAw/s400/deline_timestreams_003.png
.. |image13| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUisqWN6ueI/AAAAAAAAF6E/yAka7dlomjo/s400/deline_psds_003.png
.. |image14| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUisq6D55wI/AAAAAAAAF6M/PZ4hyu5FkZM/s400/deline_10hz_timestreams_003.png
.. |image15| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUisrWpL7yI/AAAAAAAAF6U/tSsL5Jc4n-A/s400/deline_10hz_psds_003.png
.. |image16| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUixLZbVHPI/AAAAAAAAF6c/xCWLpb9CKX4/s400/deline_timestreams_004.png
.. |image17| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUixL8APCQI/AAAAAAAAF6k/j8FyKbgOdDo/s400/deline_psds_004.png
.. |image18| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUixMjNxbkI/AAAAAAAAF6s/Hr8ouprcMpY/s400/deline_10hz_timestreams_004.png
.. |image19| image:: http://1.bp.blogspot.com/_lsgW26mWZnU/TUixNMO2NsI/AAAAAAAAF60/ZAsirbb25QY/s400/deline_10hz_psds_004.png
.. |image20| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUizkq9x4TI/AAAAAAAAF68/2xYY86d6aTQ/s400/deline_timestreams_001.png
.. |image21| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TUizlH0XvMI/AAAAAAAAF7E/ptDb5I3os6A/s400/deline_psds_001.png
.. |image22| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TUizln1mSCI/AAAAAAAAF7M/hTkZRUU3-ck/s400/deline_10hz_timestreams_001.png
.. |image23| image:: http://4.bp.blogspot.com/_lsgW26mWZnU/TUizmdrMkgI/AAAAAAAAF7U/-dlB4u30hBo/s400/deline_10hz_psds_001.png
