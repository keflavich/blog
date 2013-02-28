Quicksilver sounds
##################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer

To switch sound source from the command line:
`switchaudio`_
Use this to make scripts such as:
``#!/bin/bash/Users/adam/humor/SwitchAudioSource -s "Built-in Line Output"afplay /Users/adam/humor/losinghorn.wav/Users/adam/humor/SwitchAudioSource -s "Built-in Output"``
Then make triggers in Quicksilver by:

#. Go to trigger pane, make new hotkey trigger
#. press "." to allow you to type a command
#. make sure the action is "Run"
#. hook up a hotkey
#. if it doesn't work, just try again. Persist through crashes, they
   happen often.

Follow-up: You can also control the volume!
http://discussions.apple.com/thread.jspa?threadID=585781
`` osascript -e 'set volume output volume 100'``

.. raw:: html

   </p>

.. _switchaudio: http://code.google.com/p/switchaudio-osx/
