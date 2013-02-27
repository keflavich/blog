Mac terminal stuff
##################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer

xterm-color has some annoying features when SSHing to other compys,
including 'top' not functioning properly. The error I receive:
``top: no termcap entry for a `xterm-color' terminal``
The solution:
`From MacOSXhints`_, in bash just add ``export TERM="vt100"`` to your
``.profile`` file.

.. _From MacOSXhints: http://www.macosxhints.com/article.php?story=20031031185759986
