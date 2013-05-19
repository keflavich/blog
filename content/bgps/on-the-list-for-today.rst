On the list for today....
#########################
:date: 2008-08-23 13:42
:author: Adam (noreply@blogger.com)
:tags: googlepost, pipeline
:slug: on-the-list-for-today

Since my gigantic mapping run is still going, I'm going to work
primarily on developing code for testing the maps, and determining
important information about the mapper.
The data paper will require an iteration-to-convergence figure, or at
least an estimate of degree of convergence.

#. Need to develop code to show iteration-to-convergence

   #. need it for both NxNpca and ascending/descending
   #. have to use region files? make some sort of region reader?
   #. pick demonstration sources

#. Compare N\ :sub:`pca` results for bright, faint sources
#. Compare iterating with/without deconvolution
#. Compare median/average/baseline sky subtraction
#. Analyze efficiency...
#. Try to figure out what's causing huge offsets. Is it Galactic
   Coordinate mapping?

::

    -bash-3.00$ less /scratch/adam_work/logs/log_082208_domemiter.log | grep WholeWhole observation took 5122.6795 sec.Whole observation took 4774.3424 sec.Whole observation took 2687.7761 sec.Whole observation took 2102.5577 sec.Whole observation took 3247.5344 sec.Whole observation took 5515.2907 sec.Whole observation took 2877.6389 sec.Whole observation took 2757.0235 sec.Whole observation took 1453.0918 sec.Whole observation took 1459.7892 sec.Whole observation took 1381.3762 sec.Whole observation took 1443.1440 sec.Whole observation took 614.39645 sec.Whole observation took 2001.6709 sec.Whole observation took 1817.1512 sec.Whole observation took 1879.1385 sec.

Note that the longest set there - 5515s = 1.53 hours - was 40
iterations!

