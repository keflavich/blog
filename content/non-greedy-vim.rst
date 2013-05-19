Non-greedy vim
##############
:date: 2008-09-05 01:12
:author: Adam (noreply@blogger.com)
:tags: googlepost
:slug: non-greedy-vim


To make .* in VIM be non-greedy (i.e. match just ``<a href=x>`` out of ``"<a href=x> </a>"``), use::

    .\{-}


