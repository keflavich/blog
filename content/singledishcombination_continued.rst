Single Dish Combination Continued
#################################
:date: 2016-06-02 16:59
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, data

Continuing from yesterday, I've done some more analysis of my HC3N data on
different scales.  The first critical note is that there appears to be
disagreement between the 7m and 12m data.
In principle, smoothing the 12m data to the 7m resolution should at most
recover the 7m brightness; instead it seems that the 12m data significantly
overpredict the 7m brightness.

.. image:: |static|/images/sgrb2/array_imagecomparison.png
   :width: 600px

This discrepancy is also evident in the power spectra, where there appears to be missing flux
on 20-100 arcsecond scales.

.. image:: |static|/images/sgrb2/array_pspeccomparison.png
   :width: 600px

So maybe it's just that the 7m data are bad?


I discussed the image combination process with Baobab, and he suggested that it
may not be the flux calibration of the images (their absolute scaling) but the
relative weights used to combine them.  The default weights, and pretty much
all variants I had experimented with, use the single-dish beam as the starting
point: you weight the interferometer data by (1-SDbeam) in the fourier domain. 

It turns out that, while this weighting scheme is the obvious thing to do
because the single-dish beam is well-characterized, it may not be the best.
The interferometer data may lose sensitivity on larger scales much faster than
(1-SDbeam) would suggest.

Carrying the single-dish weight down to smaller angular scales does a better
job of ensuring there are no negatives, but is it really "right"?
Unfortunately, there's no good answer to this; the process is essentially the
same as modifying the Briggs parameter when weighting intereferometric clean
data.  You just have to choose a scale, or a weighting function, and go with
it.  As long as the weights are conservative (i.e., sum to 1), the resulting
image should in some sense be correct.

.. image:: |static|/images/sgrb2/combination_weighting_scales.png
   :width: 600px

In that figure, the weighting scheme for the large angular scale data was set
to a series of different Gaussians.  The resolution of the 7m+TP data is
(theoretically) 24x11 arcseconds, but preserving the large angular scales below
the major beam axis seems to do a better job of preserving the image's
positivity.

The effect is more pronounced if we just combine the 12m+TP data, ignoring the
7m data (which might be wrong anyway).  For weighting FWHM above 30 arcseconds,
the interferometric data dominates the map.

.. image:: |static|/images/sgrb2/combination_weighting_scales_no7m.png
   :width: 600px
