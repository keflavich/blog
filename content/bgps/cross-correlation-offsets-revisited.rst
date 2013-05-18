Cross-Correlation Offsets Revisited
###################################
:date: 2012-09-08 08:06
:author: Adam (noreply@blogger.com)
:tags: googlepost, alignment, pointing
:slug: cross-correlation-offsets-revisited

.. raw:: html

   <div dir="ltr" style="text-align: left;">

Since last time (`Taylor Expansion & Cross
Correlation`_\ `,`_\ `Coalignment Code`_), I have attempted to re-do the
cross-correlation with an added component: error estimates.
It turns out, there is a better method than the Taylor-expansion around
the cross-correlation peak.  Fourier upsampling can be used to
efficiently determine precise sub-pixel offsets (`matlab version`_,
`Manuel Guizar, author`_, `refereed article`_).
However, in the published methods just cited, there is no way to
determine the error - those algorithms are designed to measure offsets
between identical images corrupted by noise but still strongly dominated
by signal.
We're more interested in the case where individual pixels may well be
noise-dominated, but the overall signal in the map is still large.
So, I've developed a python translation of the above codes and then
some.
`Image Registration on github`_
The docstrings are pretty solid, but there is no overall documentation.
However, there's a pretty good demo of the simulation AND fitting code
here:
`Tests and Examples`_
The results for the Bolocam data are here (only applied to v2-Herschel
offsets):

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_

.. raw:: html

   </div>

.. raw:: html

   </div>

.. raw:: html

   </p>

.. _Taylor Expansion & Cross Correlation: http://bolocam.blogspot.com/2009/03/43-relative-alignment-and-mosaicing.html
.. _,: 
.. _Coalignment Code: http://bolocam.blogspot.com/2012/03/new-coalignment-code.html
.. _matlab version: http://www.mathworks.com/matlabcentral/fileexchange/18401-efficient-subpixel-image-registration-by-cross-correlation/content/html/efficient_subpixel_registration.html
.. _Manuel Guizar, author: http://people.web.psi.ch/guizar_m/main/
.. _refereed article: http://www.opticsinfobase.org/view_article.cfm?gotourl=http%3A%2F%2Fwww%2Eopticsinfobase%2Eorg%2FDirectPDFAccess%2F6C566DF3-B5C5-B342-97F01180999C7632_148843%2Fol-33-2-156%2Epdf%3Fda%3D1%26id%3D148843%26seq%3D0%26mobile%3Dno&org=University%20of%20Colorado%20at%20Boulder%20Library
.. _Image Registration on github: https://github.com/keflavich/image_registration
.. _Tests and Examples: https://github.com/keflavich/image_registration/blob/master/doc/CrossCorrelationSimulation.pdf?raw=true
.. _|image1|: http://2.bp.blogspot.com/-PMJx-wX23w8/UErt7G3PqfI/AAAAAAAAHOQ/-5xD6ReBRGs/s1600/Offsets_XYplot.png

.. |image0| image:: http://2.bp.blogspot.com/-PMJx-wX23w8/UErt7G3PqfI/AAAAAAAAHOQ/-5xD6ReBRGs/s320/Offsets_XYplot.png
.. |image1| image:: http://2.bp.blogspot.com/-PMJx-wX23w8/UErt7G3PqfI/AAAAAAAAHOQ/-5xD6ReBRGs/s320/Offsets_XYplot.png
