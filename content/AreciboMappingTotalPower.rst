Arecibo Mapping: Total Power Measurements
#########################################
:date: 2013-03-22 22:50
:author: Adam (keflavich@gmail.com)
:tags: arecibo, idl

Worked on reducing the Arecibo continuum data.  There were some serious
problems with the off positions previously, in particular generating weird
slopes.

I suspect the problem was with these lines 

..code ::

        sorted1 = sort(totals[0:-1:2])
        sorted2 = sort(totals[1:-1:2])

since the indexing is wrong, but I'm not sure yet.  I re-wrote the whole
off-position measurement to average over all scans.  Still in progress, but the
fitting works now. Here's an example:

.. figure:: static/images/total_vs_integnum.png


