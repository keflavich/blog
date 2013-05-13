Recovering from "Startup drive out of memory"
=============================================
:date: 2013-05-13 9:26
:author: Adam (keflavich@gmail.com)
:tags: mac, memory, crash

To continue frozen processes, you need to find all sleeping procs and restart them with ``kill -CONT``.

In principle, this command should do that:

``ps -A -o tpgid,uid,pid,state,flags | awk '$1!="0" && $2==501 && $4=="S" && $5!="4000410c" {print "kill -CONT " $3}' | bash``

Without the flags exclusion, this failed for me on apple's VNC server:
``ps -A -o tpgid,uid,pid,state,flags | awk '$2==501 && $4=="S" && $5!="4000410c" {print "kill -CONT " $3}' | bash``

This is necessary for recovering mac processes:
``-A      Display information about other users' processes, including those without controlling terminals.``

The outputs from the ``ps`` process are:

 *      tpgid      control terminal process group ID
 *      pid        process ID
 *      uid        effective user ID
