finally got matplotlib to install...
####################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, matplotlib, computer

the key is reading the readme, not just the make.osx file.
These commands Just Work:
``make -f make.osx PYVERSION=2.6 PREFIX=/Users/adam/repos/mpl_dependencies/ fetch deps mpl_install_stdmake -f make.osx PYVERSION=2.7 PREFIX=/Users/adam/repos/mpl_dependencies/ fetch deps mpl_install_std``
while, e.g., this one:
``make -f make.osx PYVERSION=2.6 PREFIX=/Users/adam/repos/mpl_dependencies/ fetch deps mpl_install ``
didn't. I guess because that one doesn't actually install anything.
