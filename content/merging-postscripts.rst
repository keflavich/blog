Merging postscripts
###################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer, postscript

This is essential and really difficult to find answers to, but this guy
gave it:
`http://ludo.qix.it/archive/2005/08/merge-postscript-files.html`_
The keywords I would have liked to see:
`"merge postscripts into multi-page document"`_
or `"combine postscript multiple page"`_
e.g.
``gs -sDEVICE=pswrite -sOutputFile=output.ps -dNOPAUSE -dBATCH file1.ps file2.ps file3.psorgs -sDEVICE=pswrite -sOutputFile=05358spectra.ps -dNOPAUSE -dEPSFitPage -dBATCH `ls 05358_*.eps`(the added option is to make sure the .eps isn't cropped)``

.. _`http://ludo.qix.it/archive/2005/08/merge-postscript-files.html`: http://ludo.qix.it/archive/2005/08/merge-postscript-files.html
.. _"merge postscripts into multi-page document": http://ludo.qix.it/archive/2005/08/merge-postscript-files.html
.. _"combine postscript multiple page": http://ludo.qix.it/archive/2005/08/merge-postscript-files.html
