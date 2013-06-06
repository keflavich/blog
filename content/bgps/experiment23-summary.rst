BGPS Point Source Recovery - Experiment 23 results
##################################################
:date: 2013-05-20 14:45
:author: Adam (keflavich@gmail.com)
:tags: bgps, simulations, pointsource, bolocat

Experiment 23, run in mid-May 2013, created power-law synthetic astrophysical
sky maps with added point sources in order to examine the pipeline + bolocat's
ability to recover point source flux densities accurately.

For the purpose of the BGPS v2 paper, this data is incorporated into Section
5.3: the angular transfer function and comparison with other data sets.

The parameter space explored includes 3 steps in power-spectrum background,
$\\alpha_{ps}=1,1.5,2$, which is the major parameter being explored.  A
background with $\\alpha_{ps}=2$ is approximately what we measure in both HiGal
and the reproduced regions of the BGPS power-spectrum, so it's probably the
most realistic, but it is also very bad for the pipeline: most of the power is
on the largest angular scales.  $\\alpha_{ps}=1$, on the other hand,
beautifully creates point-source-like structures.

These two images show the results of $\\alpha_{ps}=2$ and $\\alpha_{ps}=1$
skies respectively with faint point sources on top.  The point sources are more
pointy and stick out more in the $\\alpha_{ps}=1$ situation, but the
$\\alpha_{ps}=1$ map also looks more generally point-like, so there is greater
confusion.  If you believe that there are genuine point sources in the 1.1 mm
maps, the $\\alpha_{ps}=1$ would actually be very difficult to deal with since
many extracted sources would actually be part of the background.

.. image:: |filename|/bgps/images/bgps-point-source-recovery/exp23_faint_ds2_astrosky_arrang45_atmotest_amp5.0E-05_sky-2.0_seed00_peak5.0E-03_smooth_withptsrc_label_compare.png
    :width: 800px

.. image:: |filename|/bgps/images/bgps-point-source-recovery/exp23_faint_ds2_astrosky_arrang45_atmotest_amp5.0E-05_sky-1.0_seed00_peak5.0E-03_smooth_withptsrc_label_compare.png
    :width: 800px


We also explored two different sets of source brightnesses, 0.1-1 and 1-10
Jy/beam, uniformly distributed.  We picked a high source density, 500 in a
512x512 pixel map, to get decent source extraction statistics - the crowding is
still fairly low and does not significantly affect the extracted source
properties (only a few source overlap with others).  The bright sources are
obviously better-recovered than the faint, with good recovery for all of the
backgrounds explored.  The faint sources, on the other hand, were fairly
sensitive to the background.

The background levels used were $\\sim1,2,10$ Jy/beam at the peak for the
$\\alpha=2$ maps (they were lower for the other power-laws, so those will be
ignored from now on).  As described in the paper, the faint source recovery was
good for the low peak backgrounds, but recovery was essentially nonexistent for
the 10 Jy/beam background - point sources were not detected at all.

Despite the relative simplicity of this experiment, the data took 51 GB of
storage and took about half a day to run.  

In principle, one would like to examine a range of different source
distributions (power-law flux distribution, upper/lower limits, sizes) on a
range of different power-spectrum backgrounds - for the purpose of the v2
paper, this approach would be thoroughly excessive.  However, I expect Tim will
be taking this sort of approach for the next paper.
