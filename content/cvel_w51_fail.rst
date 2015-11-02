CVEL errors
###########
:date: 2015-11-02 20:50
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa, cvel

I'm trying to get a good image of the W51 main sources that have line forests.
MFS clean does a pretty good job, but is very limited in dynamic range
presumably because the spectral lines manifest as amplitude errors.

I tried splitting the data to merge my two spectral windows using `cvel`
(`code <https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/4c29c8dc763e3f994279d50db72b9a0dfc2a35b7/script_12m/split_for_localtests.py#L8>`_),
but I see thousands of errors like this::

    2015-11-02 19:52:15     WARN    SubMS::combineSpws()    Averaging failed for the following channel/correllation pairs from output row 44432 up to 44459. Corresponding visibilities will be flagged:
    2015-11-02 19:52:15     WARN    SubMS::combineSpws()+   (60, 0) (60, 1) (1804, 0) (1804, 1) (1998, 0) (1998, 1)

and when I image the cube, there is a jump at one channel that occurs because
the resolution suddenly changes either because SPW3 (the lo-res SPW) is not
included or because the hi-res one suddenly is.

.. image:: |filename|/images/w51/cvel_jump.png
   :width: 400px

It doesn't look like there's any obvious workaround at the moment, but I'll
probably try sending another helpdesk ticket about this.


My best idea for getting a decent continuum out now is something like this:

 * image the whole cube in frequency
 * determine channels that can approximate the bright continuum
 * use those to uvcontsub the data
 * image the uvcontsub'd cube
 * uvsub the imaged spectral line cube from the original data
 * re-image the now-continuum-only cube using mfs
