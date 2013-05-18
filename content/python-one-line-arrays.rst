Python: one-line arrays
#######################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, python

Ahhh, refreshing:
``      whscan = asarray([arange(scanlen)+i for i in scans_info[:,0]]).ravel()``
Not like IDL, which takes at least 4 lines b/c of the variable
declaration. There's probably a better way to do that too.
