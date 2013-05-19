Progress, but still ds1-ds5 issues
##################################
:date: 2011-03-30 02:47
:author: Adam (noreply@blogger.com)
:tags: googlepost, downsampling, calibration, pipeline
:slug: progress-but-still-ds1-ds5-issues

ds1 and ds5 agree pretty well with the recent upgrades to delining and
deconvolution. However, there are still counterexamples, e.g.
101208\_o13, in which ds5 < ds1:

.. image:: http://4.bp.blogspot.com/-fIJHF_x5mBI/TZI0cryJfbI/AAAAAAAAGDI/GsNfLRGNZAk/s200/101208_o13_raw_ds1.nc_indiv13pca.png

.. image:: http://2.bp.blogspot.com/-QRhiz8W9RDc/TZI0dGUR4UI/AAAAAAAAGDQ/WC8eLQd6_Z0/s200/101208_o13_raw_ds5.nc_indiv13pca.png

The 'fitted' values agree better than the 'measured' values now that
NANs are treated properly.
Spent a few hours today trying to figure out if weighting can explain
the difference between ds1 and ds5; it appears to make up for most of it
so I'm doing some more experiments. Why is there so much parameter
space? Why can't weighting just work? It doesn't....
also wasted a few hours trying to write a python drizzling algorithm,
which unfortunately is impossible so I had to resort to an inefficient
for loop.
Finally got some minor results. It really looks like there is a trend
pushing up the recovered flux (i.e. higher volts/Jy) for ds5 over ds1.
There is a discrepancy between map types for ds1 but not for ds5, which
is actually backwards from what I would have expected, since ds1 will
get better-sampled maps.

.. image:: http://2.bp.blogspot.com/-ARaSL7ZdDmc/TZKRcE01DnI/AAAAAAAAGDY/YMZRpRo53Hw/s320/uranus_dcfluxes_dec2010_nomask_ds1_13pca_fits_map10.png
.. image:: http://3.bp.blogspot.com/-pWtggp0vSP4/TZKRcwZ_SrI/AAAAAAAAGDg/IqVHQSprkL8/s320/uranus_dcfluxes_dec2010_nomask_ds5_13pca_fits_map10.png

Luckily, the difference between peak fitting and "measuring" results in
very small (insignificant) changes to the calibration curve (recall
fitting is direct gaussian fitting; 'measuring' is using the
gaussian-fit width and total flux in an ellipse to infer a peak assuming
a point source):

.. image:: http://2.bp.blogspot.com/-E-FDTTj-4Ik/TZKVyUA8zBI/AAAAAAAAGDo/9NGubgLWBvo/s320/uranus_dcfluxes_dec2010_nomask_ds5_13pca_fits_map10.png
.. image:: http://3.bp.blogspot.com/-GdyxFnmwQ7g/TZKVykSg57I/AAAAAAAAGDw/PPVXtfAxW0s/s320/uranus_dcfluxes_dec2010_nomask_ds5_13pca_map10.png

Since this work has all been done for the 'bootstrapping' observations
that are supposed to tell us if different map sizes are compatible, I
have included the map sizes in the diagrams now. However, to really
understand the ds1/ds5 difference, there are much better data sets,
which I'm now reprocessing using the new and improved methods.
(the Whole BGPS is also processing with the new methods in the
background, though since the methods are being updated live there may be
more changes and it will have to be re-run.... initial looks at W5 are
BAD but L030 is GOOD (bordering on amazing))

.. _|image6|: http://4.bp.blogspot.com/-fIJHF_x5mBI/TZI0cryJfbI/AAAAAAAAGDI/GsNfLRGNZAk/s1600/101208_o13_raw_ds1.nc_indiv13pca.png
.. _|image7|: http://2.bp.blogspot.com/-QRhiz8W9RDc/TZI0dGUR4UI/AAAAAAAAGDQ/WC8eLQd6_Z0/s1600/101208_o13_raw_ds5.nc_indiv13pca.png
.. _|image8|: http://2.bp.blogspot.com/-ARaSL7ZdDmc/TZKRcE01DnI/AAAAAAAAGDY/YMZRpRo53Hw/s1600/uranus_dcfluxes_dec2010_nomask_ds1_13pca_fits_map10.png
.. _|image9|: http://3.bp.blogspot.com/-pWtggp0vSP4/TZKRcwZ_SrI/AAAAAAAAGDg/IqVHQSprkL8/s1600/uranus_dcfluxes_dec2010_nomask_ds5_13pca_fits_map10.png
.. _|image10|: http://2.bp.blogspot.com/-E-FDTTj-4Ik/TZKVyUA8zBI/AAAAAAAAGDo/9NGubgLWBvo/s1600/uranus_dcfluxes_dec2010_nomask_ds5_13pca_fits_map10.png
.. _|image11|: http://3.bp.blogspot.com/-GdyxFnmwQ7g/TZKVykSg57I/AAAAAAAAGDw/PPVXtfAxW0s/s1600/uranus_dcfluxes_dec2010_nomask_ds5_13pca_map10.png

