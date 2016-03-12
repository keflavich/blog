Which one is real?
##################
:date: 2016-03-12 10:25
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, clean

I've "successfully" combined 7m and 12m data, and I've also "successfully"
processed 12m data.  In both cases, I've self-calibrated the long-baseline 12m
data.

The question now is: why are these images so different?  There are features
in the 12m-only data that are a factor of ~2 brighter than in the 12m+7m data.
That should not happen.  

This image shows the problem.  7m+12m left, 12m-only right:

.. image:: |filename|/images/w51/7m12m_vs_12m.png
   :width: 600px

Note the sharp features on the left and the small tail (filament) toward the
top right that appear in the 12m but not in the 7m+12m data.

Which features are real?  How do we decide?


I really want to believe the 12m-only data, but I am very worried that it is
artificially enhanced by sidelobes from the e8 filament:

.. image:: |filename|/images/w51/7m12m_vs_12m_zoomout.png
   :width: 600px

There is a ~20-sigma feature between e8 and e2 along the e8 filament axis,
but it is completely absent in the 7m+12m data.  That leads me to believe
that it is not real, but at such high significance that is very worrisome.
I'm also concerned by the loss of the compact source at the bottom of the e8
filament and to the left: these seem unlikely to be affected by the filament.
