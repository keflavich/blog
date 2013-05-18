New mapping procedure
#####################
:date: 2009-01-15 18:21
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, mapping
:slug: new-mapping-procedure

I cut down the number of maps made by the pipeline from 80 to 30 by
merging regions with severe overlap. I don't think this will result in
any net change in efficiency of the mapping process because a few of the
maps will go over to swap, but it will reduce the amount of overlap /
noisy edges and make debugging simpler. It should also reduce hard drive
usage once I decide that I'm satisfied with the results and remove the
old (v0.6) redundant data.
As part of this process, the reference fields for coalignment have been
re-set to the v0.6.2 coadds + some (crappy) mosaics from v0.6.2 so that
we no longer need to rely on 3x1's for the alignment.
See /data/bgps/releases/v0.7/readme.txt for details (reproduced below)
Created 01/14/09
Version 0.7 does not exist yet. This is the 'release notes' indicating
what will change
-Overlapping redundant fields will be eliminated
Mapping of field name to area covered, followed by number of
observations
included:
gemob1: l189-l192 11 - 2 = 9
w5: l135-l138 46 = 46
l133: l133-l134 34 - 1 = 33
l111: l110-l111 88 = 88
l086: l085-l086 17 = 17
l082: l080-l084 33 = 33
l077: l075-l080 43 - 1 = 42
l072: l070-l074 10 - 2 = 8
l065: l059-l069 19 = 19
l055: l053-l058 10 - 1 = 9
l050: l048-l052 19 = 19
l045: l043-l047 20 - 4 = 16
l040: l038-l042 33 - 4 = 27
l035: l034-l037 53 = 53
l032: l031-l033 61 = 61
l030: l030 61 - 3 = 58
l029: l028-l029 53 - 4 = 49
l024: l021-l027 29 = 29
l018: l015-l021 29 - 3 = 26
l012: l011-l014 7 = 7
l009: l008-l010 11 = 11
l006: l005-l007 15 - 1 = 14
l003: l002-l004 25 - 1 = 24
l001: l001 20 = 20
l000: l000 23 - 1 = 23
l359: l359 14 = 14
l357: l356-l358 9 - 1 = 8
l354: l353-l355 3 = 3
l351: l350-l352 9 = 9
