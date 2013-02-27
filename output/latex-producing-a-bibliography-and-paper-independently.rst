latex: producing a bibliography and paper independently
#######################################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, latex

`AG`_
If you want citations to work, but you don't want your bibliography to
show up, try the following:
``latex file.texbibtex file``
comment out \\biblography{} line
``latex file.tex``
If you latex again, it will screw up.
To make an independent bibliography, remove all text and replace all
citep/citet/cite commands with \\nocite{} in a different document.
Remember to usepackage{natbib} etc. You may have to copy over the .bbl
file.

.. _AG: http://casa.colorado.edu/~ginsbura/index.htm
