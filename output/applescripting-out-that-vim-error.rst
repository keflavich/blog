Applescripting out that VIM error
#################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer

.. raw:: html

   <p>

I have a frequent problem where my VIM window is too large for my
macbook screen but it fits on my external monitor, so when I unplug the
external the VIM file bar gets stuck behind the Mac OS menu bar. It's a
huge pain to fix this normally, but I wrote/stole an applescript to fix
the problem:

::

    try    tell application "Vim"        activate    end tell    tell application "System Events"        tell process "Vim"            set size of the first window to {1000, 200}            set position of the first window to {50, 50}        end tell    end tellend try

.. raw:: html

   </p>

