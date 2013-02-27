Dying Dock
##########
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer

My dock keeps dying. Repeatedly. Over and over.
Only solution so far:
``ps -vax | grep -E "Dock|PID"kill -HUP PIDkill -s SIGCHLD PID``
And similarly for problems with Chrome + /usr/sbin/mDNSResponder. They
tend to go bad together.... no clues yet from the system logs.
Ironically, the crash reporter seems to fail the most often...
