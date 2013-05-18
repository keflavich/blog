Postscript to PDF conversion
############################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, computer, postscript

``ls *.ps | sed 's/\(.*\).ps/ps2pdf \1.ps \1.pdf/' | bash``
because it's impossible to view multiple postscripts in a single
window.... how annoying.
Corollary:
``ls *.pdf | sed 's/\(.*\).pdf/pdf2jpeg \1.pdf \1.jpg/' | bash``
