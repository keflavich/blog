My python + ipython + vim debugging workflow
############################################
:date: 2015-05-07 12:00
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: python, workflow, debugging, ipython, vim

My boss_ asked a great question at our first weekly `ESO-python tutorial`_
session: What does a good ipython debugging workflow look like?

The one advantage I had found in IDL was that *everything* is a script, which
means that *everything* can be debugged in the same way: add a stop statement
at the relevant line of code.  Of course, that debugging model breaks apart
badly once you start writing complex programs and using things like common
blocks.

In ipython, there is a beautiful debugger that is far more feature-rich than
the IDL equivalent.  It can be activated simply:

.. code-block:: python

   %pdb

will toggle the interactive ipython debugger.  Then, if you run into a code
crash, you will be dumped out at an `ipdb>` prompt, with access to a
fully-functional python prompt in the local namespace / environment of the
crash point.  You can also move up and down the function hierarchy with the `u`
and `d` commands.  

The existence of the ipdb debugger suggests a natural approach for those
familiar with IDL debugging: simply add a `raise` statement wherever you would
normally have put a `stop` statement.  There are a few key differences,
however: in IDL, you could just `.continue` to run the rest of the code as if
no stop occurred; in python the same is not possible with the default ipdb.

However, the ipdb_ package allows the insertion of breakpoints just like in IDL:

.. code-block:: python

    import ipdb; ipdb.set_trace()

From within one of these breakpoints, the `.continue` command will continue on
to the next breakpoint, as you might expect.  The `n` and `s` commands will go
to the next line in the code, while `s` will allow you to drop into called functions (how?)
   

`Postmortem debugging`_ is also awesome.  If you have run a command and gotten a traceback,
you can retroactively enter the debugger:

.. code-block:: python

   %debug

but as with the normal traceback debugger, one cannot `continue` afterward.

Reloading Code
--------------

Python code is typically distributed in packages managed with a `setup.py`
script.  These are the most convenient way to install, use, and distribute
code, but they are not ideal for debugging.

When debugging a normal script, something you could run by invoking

.. code-block:: bash

   python myfile.py

or

.. code-block:: python

   %run myfile.py
   # in the local namespace
   %run -i myfile.py
   # with the python debugger active:
   %run -d myfile.py

can easily be debugged by running it line-by-line.  The `documentation
<http://ipython.org/ipython-doc/dev/interactive/tutorial.html#running-and-editing>`_
can be accessed via the `%magic` command.

For debugging "compiled" packages, though, more thought is needed.

If you are working on your own package, you can use `setuptools` to enable the ```python setup.py develop`` <https://pythonhosted.org/setuptools/setuptools.html#develop-deploy-the-project-source-in-development-mode>`_
command, which 



Postscript
----------


Some useful related links:
http://stackoverflow.com/questions/1623039/python-debugging-tips
https://pypi.python.org/pypi/pudb


.. great picture: http://commons.wikimedia.org/wiki/File:Richard_Hook_and_Eric_Emsellem_at_the_ESO_50th_Anniversary_Gala_Event.jpg

.. _boss: http://www.eso.org/~eemselle/CV.html
.. _ESO-python tutorial: https://github.com/ESO-python/ESOPythonTutorials
.. _ipdb: https://pypi.python.org/pypi/ipdb
.. _Postmortem debugging: http://scipy-lectures.github.io/advanced/debugging/#using-the-python-debugger
