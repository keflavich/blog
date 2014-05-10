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
crash point.  You can also move up and down the function hierarchy with the ``u``
and ``d`` commands.  

The existence of the ipdb debugger suggests a natural approach for those
familiar with IDL debugging: simply add a ``raise`` statement wherever you would
normally have put a ``stop`` statement.  There are a few key differences,
however: in IDL, you could just ``.continue`` to run the rest of the code as if
no stop occurred; in python the same is not possible with the default ipdb.

However, the ipdb_ package allows the insertion of breakpoints just like in IDL:

.. code-block:: python

    import ipdb; ipdb.set_trace()

From within one of these breakpoints, the ``.continue`` command will continue on
to the next breakpoint, as you might expect.  The ``n`` and ``s`` commands will go
to the next line in the code, while ``s`` will allow you to drop into called functions (how?)
   

`Postmortem debugging`_ is also awesome.  If you have run a command and gotten a traceback,
you can retroactively enter the debugger:

.. code-block:: python

   %debug

but as with the normal traceback debugger, one cannot ``continue`` afterward.

Reloading Code
--------------

Python code is typically distributed in packages managed with a ``setup.py``
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
can be accessed via the ``%magic`` command.

For debugging "compiled" packages, though, more thought is needed.

If you are working on your own package, you can use setuptools_ to enable the
``python setup.py develop`` command, which installs a symbolic link to the
source code directory - meaning any changes you make are immediately reflected
in the python source path.  This does *not* mean that any changes are
recognized in the local python environment, though!

If you are in an active ``ipython`` session, you need to ``reload`` packages to
see their results.  As far as I know, you can *never* "reload" the source code
underlying an already-instantiated class, so you have to remake any class
instances you want to examine.

The ``reload`` command is tricky to use.  You will only see changes to the source code
if you import the exact package in which the code is stored.  For example, if you have a file structure like this:

.. code-block:: bash

   mypackage/
       __init__.py
       core.py

and you do ``reload(mypackage)``, that will effectively reload only the source
code in ``__init__.py``.  If the code you want to use is called ``myfunction``
and it lives in ``core.py``, you can reload that source code by doing
``reload(mypackage.core)``.  Reloading ``mypackage`` may have no effect.  So
the key for developing packages is finding the right module to reload!

IPython has a `deepreload package
<http://ipython.org/ipython-doc/dev/interactive/reference.html#dreload>`_
intended to recursively reload functions; it may work but I had trouble in the
past.

Tests
-----

It's generally much better to have a test suite enabled with unit tests for
each component of your code.  This is the approach adopted by most open-source
projects and many industrial code developers.

Tests are invoked with the command ``py.test`` with a variety of command
options.  Among my favorites are ``py.test --tb=short``, which gives a much
less verbose traceback, ``py.test --pastebin=failed``, which posts any failure
results to pastebin for easy sharing, ``py.test -p packagename`` (or ``python
setup.py test -P packagename`` in astropy) to select tests for a specific
package.  A great deal more options can be found in the `pytest docs
<http://pytest.org/latest/>`_.  

A test suite, if properly constructed, can also be run from with in ipython:

.. code-block:: python

   import astroquery
   astroquery.test('eso')



Postscript
----------


Some useful related links:

 * http://stackoverflow.com/questions/1623039/python-debugging-tips
 * https://pypi.python.org/pypi/pudb


.. great picture: http://commons.wikimedia.org/wiki/File:Richard_Hook_and_Eric_Emsellem_at_the_ESO_50th_Anniversary_Gala_Event.jpg

.. _boss: http://www.eso.org/~eemselle/CV.html
.. _ESO-python tutorial: https://github.com/ESO-python/ESOPythonTutorials
.. _ipdb: https://pypi.python.org/pypi/ipdb
.. _Postmortem debugging: http://scipy-lectures.github.io/advanced/debugging/#using-the-python-debugger
.. _setuptools: https://pythonhosted.org/setuptools/setuptools.html#develop-deploy-the-project-source-in-development-mode
