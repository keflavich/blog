wget
####
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer

wget is very useful for acquiring data from, e.g., IRSA, the NASA
Infrared Science Archive.
``wget -nd -r -l1 -A*g09*_b4_20.fits http://irsa.ipac.caltech.edu/data/IGA/images/``
The important elements:
-nd: don't reproduce the host directory structure
-r: recursive. Grab the files referred to by the page, not just the page
itself
-l#: number of recursion levels
-A: "accept" wildcard
