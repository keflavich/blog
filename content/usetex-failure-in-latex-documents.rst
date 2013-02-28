usetex failure in latex documents
#################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, latex, matplotlib

When I use matplotlib's internal tex (rcParams['text.useTex']=False),
the postscript files generated cause errors that look like this when you
try to ps2pdf them:
``ps2pdf h2co_pilot.psError: /rangecheck in --get--Operand stack:   --dict:20/25(ro)(L)--   --nostringval--   71Execution stack:   %interp_exit   .runexec2   --nostringval--   --nostringval--   --nostringval--   2   %stopped_push   --nostringval--   --nostringval--   --nostringval--   false   1   %stopped_push   1862   1   3   %oparray_pop   1861   1   3   %oparray_pop   1845   1   3   %oparray_pop   1739   1   3   %oparray_pop   --nostringval--   %errorexec_pop   .runexec2   --nostringval--   --nostringval--   --nostringval--   2   %stopped_push   --nostringval--   %finish_show   --nostringval--   --nostringval--   9   6   0   --nostringval--   (pdf_text_enum_t)   %op_show_continue   --nostringval--Dictionary stack:   --dict:1147/1684(ro)(G)--   --dict:0/20(G)--   --dict:70/200(L)--   --dict:116/300(L)--   --dict:44/200(L)--   --dict:25/42(L)--Current allocation mode is localLast OS error: 2Current file position is 791626GPL Ghostscript 8.64: Unrecoverable error, exit code 1make: *** [h2co_pilot.pdf] Error 1``
They will not open in MacOS's Preview.app either.
Solution: Make figures with rcParams['text.useTex'] = True
