Making maps faster
##################
:date: 2011-02-07 04:39
:author: Adam (noreply@blogger.com)
:tags: googlepost, mapping, pipeline
:slug: making-maps-faster

The fundamental problem at this point is making the pipeline run faster.
At current speeds, with undownsampled data, it may take ~days to process
a single map. Ideas for faster processing:

#. Find out how long it takes to converge to 1%, 5%.... If it only
   requires 10 iterations, that's a factor of 2 savings over current
   strategies.
#. Use downsampled data of some sort if possible. Does DS2 match DS1?
   How do we measure it? Flux-flux comparison and PSF point-source size
   measurements are the most important. Need to automate PSF
   comparison....
#. Can we use median-combined individual images as a 0th order model? I
   bet the answer is 'yes' and will probably increase the speed of
   convergence by a large amount. Tests to run? This is probably needed
   if we are to split up the 'super-fields' into smaller sub-fields,
   otherwise overlapping data will be used less effectively.
#. Find some way to keep bgps.raw, bgps.ra, bgps.dec, and other items
   that are only used once on the HD during the iterative process. Is
   there any way to separate out data in a struct in this manner?

.. raw:: html

   </p>

