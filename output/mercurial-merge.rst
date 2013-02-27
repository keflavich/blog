mercurial merge
###############
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, mercurial

.. raw:: html

   <p>

`AG`_
My most hated behavior of mercurial:

::

    searching for changesadding changesetsadding manifestsadding file changesadded 1 changesets with 3 changes to 3 files (+1 heads)(run 'hg heads' to see heads, 'hg merge' to merge)remote: 1 changesets foundrunning hook post-pull: hg upabort: crosses branches (merge branches or use --clean to discard changes)warning: post-pull hook exited with status 255$ hg mergeabort: outstanding uncommitted changes (use 'hg status' to list changes)$ hg commitnothing changed

Solution:
`` hg merge --force ``
Hopefully there are other solutions that I'll eventually add to this.

.. raw:: html

   </p>

.. _AG: http://casa.colorado.edu/~ginsbura/index.htm
