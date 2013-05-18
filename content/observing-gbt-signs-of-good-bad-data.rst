Observing @ GBT: Signs of good & bad data
#########################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, GBT



So far, all of the observations for the H\ :sub:`2`\ CO densitometry
project have been performed at the Green Bank Telescope. During a 10-day
long observing trip here, I've learned a lot about diagnosing bad data.




.. image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TGyf_Sx-Z-I/AAAAAAAAFzw/1wCgkpI11WI/s400/session92_if0_feed0_trec.png


This first image shows TSYS vs Airmass for good data. The high outliers
are just sources with continuum in them - the continuum is the source of
the extra signal, not atmosphere.  The receiver temperature is a nice
20.6 K, and you get about 5 K extra per airmass, suggesting a zenith
optical depth of 0.018 assuming a round atmospheric temperature of 300K.






.. image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TGyer8CZzVI/AAAAAAAAFzI/zoU1K0cIu7Q/s400/session04_if0_feed0_trec.png


In the same style plot, there is a set of observations with low system
temperatures: that stuff is good. There is also a set with clearly
rising system temperatures, even at constant elevation. These data are
bad. During this observation, the "blowers" that are meant to keep dew
off of the receivers failed. Dew buildup on the receiver covers lead to
higher optical depths and therefore system temperatures.








.. image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TGyf9RwmbRI/AAAAAAAAFzo/n0gyG81oOns/s400/session91_if0_feed0_trec.png


Finally, this data set was totally useless. Ku-band is not particularly
sensitive to water in the atmosphere... but it's still not a good idea
to observe during a rain storm.  Note that the fitted receiver
temperature TREC is nonsensical.


.. _|image3|: http://2.bp.blogspot.com/_lsgW26mWZnU/TGyf_Sx-Z-I/AAAAAAAAFzw/1wCgkpI11WI/s1600/session92_if0_feed0_trec.png
.. _|image4|: http://3.bp.blogspot.com/_lsgW26mWZnU/TGyer8CZzVI/AAAAAAAAFzI/zoU1K0cIu7Q/s1600/session04_if0_feed0_trec.png
.. _|image5|: http://2.bp.blogspot.com/_lsgW26mWZnU/TGyf9RwmbRI/AAAAAAAAFzo/n0gyG81oOns/s1600/session91_if0_feed0_trec.png

.. |image3| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TGyf_Sx-Z-I/AAAAAAAAFzw/1wCgkpI11WI/s400/session92_if0_feed0_trec.png
.. |image4| image:: http://3.bp.blogspot.com/_lsgW26mWZnU/TGyer8CZzVI/AAAAAAAAFzI/zoU1K0cIu7Q/s400/session04_if0_feed0_trec.png
.. |image5| image:: http://2.bp.blogspot.com/_lsgW26mWZnU/TGyf9RwmbRI/AAAAAAAAFzo/n0gyG81oOns/s400/session91_if0_feed0_trec.png
