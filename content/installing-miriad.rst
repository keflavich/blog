:author: Adam <keflavich@gmail.com>
:tags: miriad
:date: 2015-09-14

From Andrew Walsh, a script to install MIRIAD:

.. code-block:: bash

   wget ftp://ftp.atnf.csiro.au/pub/software/miriad/miriad-common.tar.bz2
   wget ftp://ftp.atnf.csiro.au/pub/software/miriad/miriad-linux64.tar.bz2
   bzcat miriad-common.tar.bz2 | tar xvf -
   bzcat miriad-linux64.tar.bz2  | tar xvf -
   cd miriad
   export MIR=$PWD
   sed -e "s,@MIRROOT@,$MIR," scripts/MIRRC.in > MIRRC
   sed -e "s,@MIRROOT@,$MIR," scripts/MIRRC.sh.in > MIRRC.sh
   chmod 644 MIRRC*

   # Put these into .bashrc, or call them each time you want to run MIRIAD
   . MIRRC.sh
   export PATH=$PATH:$MIRBIN
