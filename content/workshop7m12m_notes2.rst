Retrieving and Selecting Data in CASA
#####################################
:date: 2016-02-24 13:44
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, ALMA


I learned a few important things at the 7m+12m workshop in Garching:

1. ``clean`` treats input models in Jy/beam and Jy/pixel qualitatively (not
   just quantitatively) differently.  Jy/pixel images are taken to be model
   images exactly, where Jy/beam are... somehow interpreted differently, maybe
   as clean component assemblies.  I don't know the details, but this is a
   major caution.

2. The ``tbtool`` is not very good for extracting data for plotting.  The flags
   are not guaranteed to be in a sane shape, which will lead to crashes if you
   try ``tb.getcolumn('FLAG')``.  ``ms.msselect``, however, allows you access
   to most of the normal selection routines used in ``clean``, ``split``, etc.
   It is tricky, though, because ``ms.select`` does *not* allow you access to 
   the same selection.  Also, while ``spw``-based selection normally allows you
   to select channels, in ``ms.msselect`` it does not: instead you must use
   ``ms.selectchannel``.  See `this example
   <https://github.com/radio-astro-tools/sandbox/blob/master/casa_7m12m_tools/weight_density_uv_plot.py>`__.

   Details about the selection are at this URL, but the documentation is
   incomplete and, in places, incorrect:

   http://www.aoc.nrao.edu/~sbhatnag/misc/msselection/FrequencySelection.html

   (for example, ``chanspec`` is not valid in ``msselect``, or at least
   it doesn't do anything)
