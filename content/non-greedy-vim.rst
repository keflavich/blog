Non-greedy vim
##############
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer

.. raw:: html

   <p>

To make .\* in VIM be non-greedy (i.e. match just <a href=x> out of "<a
href=x> </a>"), use:

::

    .\{-}

.. raw:: html

   </p>

