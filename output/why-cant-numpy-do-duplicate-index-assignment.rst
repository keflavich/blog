Why can't numpy do duplicate index assignment
#############################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, numpy

`AG`_
I want to do drizzling with numpy. It should be trivial, but it's
impossible (without a for loop, afaik) instead.
``In [2]: a = array([1,1,2,2])In [3]: b = arange(5)In [4]: b[a] += 1In [5]: bOut[5]: array([0, 2, 3, 3, 4])In [6]: # but b should really be:In [7]: b[a] += 1In [8]: bOut[8]: array([0, 3, 4, 3, 4])``

.. _AG: http://casa.colorado.edu/~ginsbura/index.htm
