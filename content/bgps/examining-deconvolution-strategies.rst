Examining deconvolution strategies
##################################
:date: 2011-04-07 22:05
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post
:slug: examining-deconvolution-strategies

This is a direct continuation of what I did yesterday (but only posted
today because I forgot to click post).
No-deconvolution doesn't work, at least not reliably. It recovers
structures that are too large to be believable. Perhaps a higher
threshold should be required to include signal in the model? The noise
actually looks too high anyway. Also, the flagging doesn't look great.
Grr.
The agreement between the three is somewhat better, down to a 50%
increase of reconv over deconv:
[deconv, nodeconv, reconv]:
BMAJ: 0.00916667 BMIN: 0.00916667 PPBEAM: 23.8028 SUM/PPBEAM: 8.19765
Sum: 195.127 Mean: 1.04346 Median: 0.751545 RMS: 0.78342 NPIX: 187
BMAJ: 0.00916667 BMIN: 0.00916667 PPBEAM: 23.8028 SUM/PPBEAM: 10.1592
Sum: 241.816 Mean: 1.29314 Median: 1.04031 RMS: 0.778854 NPIX: 187
BMAJ: 0.00916667 BMIN: 0.00916667 PPBEAM: 23.8028 SUM/PPBEAM: 12.1694
Sum: 289.664 Mean: 1.54901 Median: 1.31107 RMS: 0.808915 NPIX: 187
But this time there is less indication of negative residuals than
previously.
I was very confused by negatives being included in the model for
nodeconv, then realized it's because of the grow\_mask option.
sncut = 1 is now default for nodeconv. I think it makes sense.
(sncut = 1 drops the flux by <10%:
BMAJ: 0.00916667 BMIN: 0.00916667 PPBEAM: 23.8028 SUM/PPBEAM: 9.31507
Sum: 221.725 Mean: 1.18569 Median: 0.915137 RMS: 0.783316 NPIX: 187)
While reconv has produced reasonable results in some cases, a close look
at the maps shows that deconv ~ nodeconv << reconv. There is something
wrong with reconv. It spreads out and increases the flux artificially.
So.... why did it work so damn well for point sources?
The new weighting scheme seems to flag a dangerous number of bolos as
'high weight'. It drops after iteration #1, but not all the way.
Need to remember to reprocess all December 2009 data with more flagged
bolos
