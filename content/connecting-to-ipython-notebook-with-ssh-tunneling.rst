Connecting to ipython notebook with SSH tunneling
#################################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost

.. raw:: html

   <div dir="ltr" style="text-align: left;">

.. raw:: html

   <div dir="ltr" style="text-align: left;">

My typical ssh tunnel looks something like:
``ssh -N -f -L 8889:SERVER.colorado.edu:8889 ginsbura@SERVER.colorado.edu``

.. raw:: html

   </div>

For ipython notebooks, this approach was giving me the error:
`` channel 2: open failed: connect failed: Connection refused``.
The ipython notebook is at http://127.0.0.1:8888/ locally. Therefore,
the correct ssh tunnel command is:
``ssh -N -f -L localhost:8888:localhost:8888 adam@SERVER.colorado.edu``

.. raw:: html

   </div>

.. raw:: html

   </p>

