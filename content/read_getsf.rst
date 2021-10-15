Reading a getsf catalog
#######################
:date: 2021-05-15 21:23
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: getsf


To read a `getsf <http://irfu.cea.fr/Pisp/alexander.menshchikov/#method>`_ catalog, you can do:

.. code:: python

    from astropy.io import ascii
    cat = ascii.read('getsf.cat', data_start=0, format='commented_header', header_start=110, comment=\"!\")

though ``header_start`` may be different; I've seen 110 and 120 at least.
