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

.. image:: |static|/images/w51/cvel_jump.png
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

EDIT: Dirk replied to the helpdesk ticket, suggesting::

    Concerning cvel: try to process one SPW at a time. Otherwise cvel will
    _combine_ the SPWs and if they are not observed at the same time, this will
    lead to problems.

So I've now `split the cvel into two commands
<https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/2d15ce46f9ecd75d70ab7ac4ee8f91b272139d9e/script_12m/split_for_localtests.py#L8>`_.
I also added `outframe='bary'` because otherwise it's not obvious that the
frequency command is doing anything
sensible or useful.  That's actually probably why I was getting non-overlapping
segments before - it tried converting to barycentric, but maybe too late in the
process (i.e., it tried selecting in topo, then converting to bary for output).
I also added a phasecenter, because it was automatically selecting pointing 24
as the phasecenter for cvel before.

This led to a new error::

    2015-11-03 14:38:27     WARN    cvel::SubMS::convertGridPars     *** Requested new channel width is smaller than smallest original channel width
    2015-11-03 14:38:27     WARN    cvel::SubMS::convertGridPars+        which is 488319 Hz

which I've fixed by setting the output width to be 0.5 MHz, just a simple round
number greater than the input even accounting for shift.  Unfortunately, this
seems to have produced a dramatically larger output MS, which cannot be
correct.... ahhh, it turns out that was temporary, once regridding was complete,
it turned small again.
