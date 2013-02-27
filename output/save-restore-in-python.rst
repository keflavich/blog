SAVE / RESTORE in Python
########################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, python, computer

Save/Restore is probably the single best feature of IDL that, sadly, is
very poorly replicated in Python. For 1 or 2 dimensional variables, you
can use Pylab's ``save/load``, but I never use such piddling tiny
arrays. For higher dimensional objects, either using FITS files (a pain
because of header definitions) or pickling ought to work.
e.g.:
``import numpyimport picklex=ones([10,10,10,10],dtype='float64')pickle.dump(x,open('x.pysav','w'))X = pickle.load(open('x.pysav','r'))``
