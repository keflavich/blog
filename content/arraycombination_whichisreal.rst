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
