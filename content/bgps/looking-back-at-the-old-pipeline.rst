Looking back at the old pipeline
################################
:date: 2008-08-07 16:33
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, pipeline
:slug: looking-back-at-the-old-pipeline

I've obviously missed something. So to try to figure out what it is, I'm
going back to the old pipeline... again...
in map\_ncdf\_reading, lines 441-448, there is something curious that
goes back to a definition-of-variables problem: ddec and dra are ADDED
to ra and dec to get the new "ra\_all" and "dec\_all" variables. ddec
and dra are calculated from eaz and eel: ERROR OFFSETS in Az and El.
Why? What?!
I added a new piece of code, correct\_eaz\_eel.pro. It is extremely
short, but extremely necessary.

::

    pro correct_eaz_eel,ra,dec,el,az,eel,eaz,pa    dra=-eaz*cos(!dtor*pa)*cos(!dtor*el)+eel*sin(!dtor*pa)    ddec=eaz*sin(!dtor*pa)*cos(!dtor*el)+eel*cos(!dtor*pa)    dec += ddec/3600.    ra  += dra/3600. / cos(!dtor*dec) / 15.end    

This comes back to the fact that I don't know what ANY of the variables
in the NCDF header are supposed to be. Why are "error" variables
actually OFFSET variables, and why didn't anyone know about them?

