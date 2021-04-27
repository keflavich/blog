CASA: Logfiles & tclean from pysynthesisimager
##############################################
:date: 2020-05-09 14:59
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa

A few brief notes I don't want to forget, so I'm posting them here:

The name of the log file being used by the currently active CASA session is in ``casalog.logfile()``.

I'm trying to get the pysynthesisimager version of tclean to work.  This is, in
theory, "exactly the same thing as tclean", except you (the user) have the
ability to control individual steps.  The process is documented in the `tclean documentation
under examples <https://casa.nrao.edu/casadocs-devel/stable/global-task-list/task_tclean/examples>`_.

However, it is not a one-to-one mapping.  ``tclean`` is not implemented using the exact script quoted
in the examples.  The differences are the variety that shouldn't matter but inevitably do.

I'm working on a translation of ``tclean``'s input parameters to
``pysynthesisimager``'s, but it's not complete:
https://gist.github.com/keflavich/a9953c88cbe098b5e9bb4bdac6485f09

That was dumb anyway, because
https://github.com/radio-astro/casa/blob/master/gcwrap/python/scripts/task_tclean.py
does everything I really needed.

My version saves the image, residual, and model at each major cycle.  
