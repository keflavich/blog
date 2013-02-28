IDL colors
##########
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer

.. raw:: html

   <p>

To get IDL colors to 'work right' (i.e. a colortable has 255 colors
etc), put this in a startup file:

::

    device, true_color = 24, retain = 2, decompose = 0red = [0,1,1,0,0,1]green = [0,1,0,1,0,1]blue = [0,1,0,0,1,0]if not strcmp(getenv('DISPLAY'),'') then $   tvlct, 255*red, 255*green, 255*blue

.. raw:: html

   </p>

