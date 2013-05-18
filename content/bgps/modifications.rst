Modifications
#############
:date: 2008-08-19 18:07
:author: Adam (noreply@blogger.com)
:tags: googlepost, pipeline
:slug: modifications

Things that have been changed in the past 24 hours that are very
significant:

#. In apply\_pointing\_model, the signs of FAZO and FZAO have been
   swapped. I BELIEVE this is correct but somehow things aren't working
   out still.
#. In do\_the\_pointing I have changed from "eq2hor" and "hor2eq" to
   "my\_eq2hor" and "my\_hor2eq". These implement two major changes:

   #. The LST is passed as a parameter rather than calculated within the
      ASTROLIB code
   #. The conversion is calculated with BOTH hadec2altaz and getaltaz
      (and similar for the opposite transformation) and compared for
      error checking purposes. If they differ by more than one
      arcsecond, the code will spit out an error message and use
      getaltaz.

.. raw:: html

   </p>

