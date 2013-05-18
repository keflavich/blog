Reinstalling a system
#####################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, python, computer

Python died tonight when I foolishly tried to update numpy or
matplotlib. One was not compatible with the other in upgraded form, and
the update for matplotlib wouldn't install because of GTK issues that
were totally opaque.
So, I reinstalled EVERYTHING - fink AND macports - from scratch. If I
don't get things running by morning I'm going to have to do a restore,
which is ugly as death.
Things I need to do post-install:
``        sudo port install python_select          sudo python_select python25``
test ipython
test matplotlib
test numpy
