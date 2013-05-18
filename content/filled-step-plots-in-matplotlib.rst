Filled step plots in matplotlib
###############################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, matplotlib, python

.. raw:: html

   <p>

It's not possible to do a simple filled step plot in matplotlib using
default
commands. Workaround:

::

    def steppify(arr,isX=False,interval=0):    """    Converts an array to double-length for step plotting    """    if isX and interval==0:        interval = abs(arr[1]-arr[0]) / 2.0        newarr = array(zip(arr-interval,arr+interval)).ravel()        return newarrplot(xx,yy,linestyle='steps-mid',color='b',linewidth=1.5)fill_between(steppify(xx[x1:x2],isX=True),    steppify(yy[x1:x2])*0,    steppify(yy[x1:x2]),    facecolor='b',alpha=0.2)

.. raw:: html

   </p>

