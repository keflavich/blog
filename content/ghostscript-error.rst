Ghostscript error?
##################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, latex, postscript

.. raw:: html

   <p>

I've been receiving the following error when attempting to compile
(ps2pdf) my w5 outflows paper:

::

    Error: /rangecheck in --get--Operand stack:   pdfmark   --dict:20/25(ro)(L)--   --nostringval--   50Execution stack:   %interp_exit   .runexec2   --nostringval--   --nostringval--   --nostringval--   2   %stopped_push   --nostringval--   --nostringval--   --nostringval--   false   1   %stopped_push   1878   1   3   %oparray_pop   1877   1   3   %oparray_pop   1861   1   3   %oparray_pop   1755   1   3   %oparray_pop   --nostringval--   %errorexec_pop   .runexec2   --nostringval--   --nostringval--   --nostringval--   2   %stopped_push   --nostringval--   %finish_show   --nostringval--   --nostringval--   8   6   1   --nostringval--   (pdf_text_enum_t)   %op_show_continue   --nostringval--Dictionary stack:   --dict:1153/1684(ro)(G)--   --dict:0/20(G)--   --dict:71/200(L)--   --dict:125/300(L)--   --dict:44/200(L)--   --dict:138/224(L)--Current allocation mode is localLast OS error: 2Current file position is 267478928GPL Ghostscript 8.71: Unrecoverable error, exit code 1

I get the same error with Ghostscript 8.64, but on my laptop, using the
fink version, it works. Similarly, there are errors with the postscript,
so I'm led to believe it's an error in latex:

::

    $ latex --versionpdfTeX 3.1415926-1.40.10-2.2 (TeX Live 2009)kpathsea version 5.0.0Copyright 2009 Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).There is NO warranty.  Redistribution of this software iscovered by the terms of both the pdfTeX copyright andthe Lesser GNU General Public License.For more information about these matters, see the filenamed COPYING and the pdfTeX source.Primary author of pdfTeX: Peter Breitenlohner (eTeX)/Han The Thanh (pdfTeX).Compiled with libpng 1.2.39; using libpng 1.2.39Compiled with zlib 1.2.3; using zlib 1.2.3Compiled with xpdf version 3.02pl3

No idea what the cause is but it's time to start documenting steps and
looking for a workaround. Compiling on the lappy isn't a good option.

.. raw:: html

   </p>

