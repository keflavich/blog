Make PDFs open with the thumbnails window open
##############################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, pdf

Neat trick I picked up from here:
http://www.ghostscript.com/~ghostgum/pdftips.htm
Add this code:
``  \special{! /pdfmark               [/View [/XYZ null null 1]  % unspecified x and y offset, 100% zoom               /Page 1               /PageMode /UseThumbs % /UseNone /UserOutlines /UseThumbs /FullScreen              /DOCVIEW pdfmark               }``
to a LaTeX document (probably near the top) and when you ps2pdf it, it
will open the PDF with the thumbnail bar open. This is very useful for
proofreading after you latex a file. Of course, xdvi also works well for
this, but xdvi is VERY unstable on the Mac. At least adobe, being a
native Mac program, doesn't crash as often.
