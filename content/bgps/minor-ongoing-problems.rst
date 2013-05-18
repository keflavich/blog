[minor] Ongoing problems...
###########################
:date: 2011-07-10 19:41
:author: Adam (noreply@blogger.com)
:tags: googlepost, problems, pipeline, minor
:slug: minor-ongoing-problems

Since I have many tasks running in parallel, I need to summarize them
sometimes...

#. There are many "bad" observations that haven't been placed in "bad"
   directories. A list of the error messages generated is here: `Making
   Infiles wiki`_
#. There may be streaking in the BGPS ds2 images of l030 and l032. Still
   trying to re-run cleanly to find out
#. There may be unflagged high-points in l030 and l032. Also under
   examination
#. Simulations have been generating bulk-offset outputs; my suspicion
   was that the relative scales were being set incorrectly because astro
   dominated atmo, so I bumped up the atmo scale. The tests have run but
   I haven't examined the outputs
#. V1 sims have shown streaking, possibly because of the previous
   bullet, but certainly (in part) because cross-scans haven't worked

.. raw:: html

   </p>

.. _Making Infiles wiki: http://code.google.com/p/bgpspipeline/wiki/MakingInfiles
