Massive upgrades, new strategy?
###############################
:date: 2008-11-18 04:01
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, pipeline
:slug: massive-upgrades-new-strategy

A few major things today:

    #. I renamed 'ts\_to\_map' to 'drizzle' and made 'ts\_to\_map' a wrapper
    that will either median combine by scans (if passed the right keywords,
    i.e. tstomapmedian and scans\_info). This will reject cosmic rays much
    more effectively than previously.
    #. My extensive test runs on the 'weird' fields completed. Conclusions:

      * Deconvolution is DEFINITELY responsibly for the weird fuzzy effects
         seen esp. in l=33, l=2.
      * Even a descending iterator is ineffective at alleviating this
         problem
         What I still don't understand is WHY the deconvolver is behaving badly
         for some regions. It is extracting peaks that are too high.
      * Not deconvolving works pretty well, so I'm not really concerned. I'm
         resetting the defaults to no deconvolution once my next test is done....

    #. Started up a new test run to compare median stacking with weighted
       average stacking
