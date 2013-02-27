Major mac problems
##################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, crash, computer

The errors are, in short:

-  Browser stops responding / starts returning "page not found"
   (indicating a failure of mDNSResponder)
-  killing mDNSResponder sometimes brings browser back, but more often
   leads to a partial system freeze (some windows don't respond, can't
   switch between windows except by clicking)
-  /var/log/system.log gets flooded with "too many files open" errors.
-  somewhere in here the Dock fails
-  killing Google Chrome and/or the Dock fails; the process never halts
   (even kill -9 + kill -s SIGCHLD)
-  usually one or two crash reports pop up, at least one of which is for
   crash\_reporter
-  system.log stops getting flooded, but the browser and Dock never
   recover

The only message in system.log that gives me any hint about what might
be happening is occasionally a freeze was resolved at the same time as
this message: Jun 22 19:02:09 eta Quicksilver[93771]: Multiple Scans
Attempted but it doesn't seem to change the situation if quicksilver is
open or not. Google has nothing on this issue, either, except for the
quicksilver source code, so evidently it has not caused problems for
other people system.log was also being flooded with this message:

::

    Jun 23 08:57:19 eta postfix/master[99954]: fatal: open /dev/null: Bad file descriptorJun 23 08:57:20 eta com.apple.launchd[1] (org.postfix.master[99954]): Exited with exit code: 1Jun 23 08:57:20 eta com.apple.launchd[1] (org.postfix.master): Throttling respawn: Will start in 9 seconds

so I disabled my postman:

::

    Jun 23 08:57:27 eta sudo[99955]: adam : TTY=ttys006 ; PWD=/Users/adam/proposals/alma ; USER=root ; COMMAND=/bin/launchctl unload -w /System/Library/LaunchDaemons/org.postfix.master.plist

These errors:

::

    Jun 23 09:06:40 eta Dock[99877]: kCGErrorIllegalArgument: CGSSetWindowTransformAtPlacement: Singular matrix [nan 0.000 0.000 nan]Jun 23 09:06:40 eta com.apple.Dock.agent[99877]: Thu Jun 23 09:06:40 eta.colorado.edu Dock[99877] : kCGErrorIllegalArgument: CGSSetWindowTransformAtPlacement: Singular matrix [nan 0.000 0.000 nan]

are correlated with opening Chrome windows and/or Chrome's
crash\_inspector

::

    Jun 23 09:06:09 eta [0x0-0x69e69e].com.google.Chrome[99995]: [99995:24579:485131152128125:ERROR:shared_memory_posix.cc(164)] Creating shared memory in /var/folders/ni/ni+DtdqFGMeSMH13AvkNkU+++TI/-Tmp-/.com.google.chrome.sHcu6r failed: Too many open files in system

This is the problem that really gets me... I think it's
crash\_inspector's fault.
But there's definitely more going on here than just Chrome. Trying to
change default browsers (by opening Safari and opening Preferences) led
to a partial Dock crash (?!) in which I can alt-tab but can't see the
Dock. Not clear at all what's going on.... argh.

.. raw:: html

   </p>

