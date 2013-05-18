Catalog vs Image shift?  A possible solution to the ATLASGAL issue
##################################################################
:date: 2012-12-26 23:02
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, pointing
:slug: catalog-vs-image-shift-a-possible-solution-to-the-atlasgal-issue

.. raw:: html

   <div dir="ltr" style="text-align: left;">

In the `previous post`_, I came up with a final plot showing the
pointing offset was, on average, not significant, even in the ATLASGAL
overlap zone.
So why did the ATLASGAL group infer a net pointing offset?
The problem is probably one or two fields with a slight pointing offset,
but a huge number of source.  l=1 has an offset of the right sign and is
the single most source-rich degree in the survey, with 368 sources.

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_

.. raw:: html

   </div>

This figure shows the v1 vs v2 source locations in grey, their average
and standard deviation in green, and the cross-correlation offset in
red.  The plot is somewhat difficult to interpret, but it appears that
the v1 point sources are systematically more shifted to negative
longitudes than v2, and the point sources more than the maps themselves.
 There may have been some reason sources were systematically selected at
more negative longitudes in the v1 catalog; around Sgr B2 there's a lot
of structure that had to be decomposed somehow but was not necessarily
"source".
One thing to note is the reversal in left-right (in pixel space) vs the
positive/negativeness in longitude.  The above plot is correct (negative
longitudes, as shown on the plot, are "right" in images), but most of my
other plots have the X-axis flipped.
In the end, after spending two weeks hammering my head against this, I
find no clear evidence for an offset  between the BGPS and Herschel or
v1/v2 data overall or in the ATLASGAL fields.  In any individual field,
that statement is not necessarily true.
Despite the strong statistical evidence, it is really hard to be really
sure about sub-pixel offsets, since the "model" image is never perfect.
 I think we can safely state the ~1/2 pixel offsets (~3") but I just
don't feel confident about numbers below that range for ALL fields.

.. raw:: html

   </div>

.. raw:: html

   </p>

.. _previous post: http://bolocam.blogspot.com/2012/12/pointing-cross-correlation-yet-again.html
.. _|image1|: http://2.bp.blogspot.com/-ONF7C_v8rNk/UNpmXIEe6HI/AAAAAAAAHUI/kdf3pmUKyE0/s1600/l001_catalog_image_compare.png

.. |image0| image:: http://2.bp.blogspot.com/-ONF7C_v8rNk/UNpmXIEe6HI/AAAAAAAAHUI/kdf3pmUKyE0/s320/l001_catalog_image_compare.png
.. |image1| image:: http://2.bp.blogspot.com/-ONF7C_v8rNk/UNpmXIEe6HI/AAAAAAAAHUI/kdf3pmUKyE0/s320/l001_catalog_image_compare.png
