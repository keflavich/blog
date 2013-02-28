cython vs f2py
##############
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, python, computer

I had a go at optimizing some code this past week, and ended up learning
to use both cython and f2py.
f2py is much easier to use. If you want to write a function in fortran
and use it in python, all you do is write the code and add
specifications using comments in the fortran code.
cython is more natural to code. The code style is C/fortran-like: think
in terms of loops instead of arrays. The syntax is python-like, which
makes coding somewhat clearer and simpler.
For my code, I found that cython was ~10% slower than fortran.
Check out the plfits in:
http://code.google.com/p/agpy/source/browse/#svn/trunk/
