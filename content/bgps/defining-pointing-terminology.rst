Defining Pointing Terminology
#############################
:date: 2008-07-30 21:50
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, documentation, pointing
:slug: defining-pointing-terminology

There has been a lot of confusion about pointing terminology.

.. raw:: html

   <ul>

.. raw:: html

   <li>

CSO pointing model: the telescope pointing model used and written as a
black box

.. raw:: html

   </li>

-  has already been corrected for aberration/nutation
-  is in current epoch coordinates (e.g. J2007.34)

.. raw:: html

   <li>

Instrument-specific correction to pointing model

.. raw:: html

   </li>

-  ??? also referred to as 't terms'
-  is offset between CSO pointing model and real locations
-  should be a function of alt (and maybe az)
-  is recorded in "RPC" files
-  is in units of distance on the sky: delta-RA and delta-DEC, or
   delta-ALT and delta-AZ will be in the same units, while if they were
   in coordinate units delta-RA and delta-AZ would have to be scaled by
   1/cos(DEC) or 1/cos(ALT) respectively

.. raw:: html

   <li>

FAZO and FZAO: Fixed Azimuth Offset and Fixed Zenith Angle Offset

-  these are ambiguously defined in the pipeline code
-  ???? FAZO/FZAO include both the functional instrument specific
   pointing offset and any manual changes made at the telescope [manual
   only relevant to 2007 observations]
-  ???? or are these JUST fixed offsets, and the instrument specific
   corrections are not included? Either way, how can I separate out
   manually-applied fixed offsets from fitted-model offsets?

.. raw:: html

   </li>

.. raw:: html

   </ul>

.. raw:: html

   </p>

