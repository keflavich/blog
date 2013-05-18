Open Questions I'm trying to answer
###################################
:date: 2011-07-17 22:58
:author: Adam (noreply@blogger.com)
:tags: googlepost
:slug: open-questions-im-trying-to-answer

I still haven't dealt with
`http://bolocam.blogspot.com/2011/07/additional-problems.html`_, or
essentiall any of
`http://bolocam.blogspot.com/2011/07/minor-ongoing-problems.html`_.
However, they're probably related to this problem:
``% CLEAN_ITER_STRUCT: There were            1 bolometers with high weights:       13.5047 indices:      142 or flagged indices          142``
which indicates that in a simulation in which there can be no outliers
(in terms of weight/scale), there is one being rejected as an outlier.
That indicates that weights are being computed incorrectly, despite the
fact that scales look right (so far):
``Relsens calibration: Scaled to bolometer #        0% RELSENS_CAL_PCA: There were            0 NAN scales and            0 very low scales% RELSENS_CAL_PCA: Scale Median/Mad:        1.0005510+/-     0.010990833 led to            0 scales set to zero for a total of            0 bad bolos% RELSENS_CAL_PCA: Scales avg+/-std =        1.0007304355062783+/-       0.0103252880998329Relsens calibration: Scaled to bolometer #        0% RELSENS_CAL_PCA: There were            0 NAN scales and            0 very low scales% RELSENS_CAL_PCA: Scale Median/Mad:       0.99955294+/-    0.0093122063 led to            0 scales set to zero for a total of            0 bad bolos% RELSENS_CAL_PCA: Scales avg+/-std =        0.9990063123041220+/-       0.0096663438876613``

.. _`http://bolocam.blogspot.com/2011/07/additional-problems.html`: http://bolocam.blogspot.com/2011/07/additional-problems.html
.. _`http://bolocam.blogspot.com/2011/07/minor-ongoing-problems.html`: http://bolocam.blogspot.com/2011/07/minor-ongoing-problems.html
