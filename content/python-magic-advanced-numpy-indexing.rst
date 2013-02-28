Python magic / advanced numpy indexing
######################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, python

Yeah, indexing python arrays should really be easy.
`Stefan van der Walt's page`_
``In [85]: bi = (f.bolo_indices[np.newaxis,:] + zeros([7751,1])).astype('int')In [86]: whc = (whscan[:,np.newaxis] + zeros([1,107])).astype('int')In [87]: array2d[whc,bi] = temp2d``

.. _Stefan van der Walt's page: http://mentat.za.net/numpy/numpy_advanced_slides/
