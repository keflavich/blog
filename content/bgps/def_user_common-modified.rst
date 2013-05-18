def_user_common modified
########################
:date: 2008-11-23 15:21
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, pipeline
:slug: def_user_common-modified

The NP doesn't work without USER\_COMMON defined because at a single
point it makes use of the 'which' function.
def\_user\_common is a disaster, though, because it calls
get\_screen\_size(), which forces an X connection to be launched, which
means that if you start a remote session and close X IDL crashes. This
has been a constant nagging problem and has cost me ~a few days of work.
So I commented out the offending (and offensive) line. The worst of it
is, I'm not even convinced there's anything that uses any of that
information. The common block is only needed to get paths, so which
could have been written better.
The pipeline ground to a halt for an unknown reason at an unknown point
so I added a lot more timing outputs to try to figure out what's going
on.
Back to the grind...
