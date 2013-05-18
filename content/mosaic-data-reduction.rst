MOSAIC data reduction
#####################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, iraf

MOSAIC reduction is very difficult.
`http://www.noao.edu/noao/noaodeep/ReductionOpt/frames.html`_ has the
official instructions.
Important things:
Have the latest version of `MSCRED`_ and `MSCDB`_ installed. Both will
give cryptic errors or "cannot open file" errors (because the files
don't exist) otherwise.
``mscredsetinstrument kpno CCDMosaThin1msccmatch obj09*.fits coords="!mscgetcat $I $C" search=60 rsearch=1 nfit=30 accept=yes interactive=no fit=no``

.. _`http://www.noao.edu/noao/noaodeep/ReductionOpt/frames.html`: http://www.noao.edu/noao/noaodeep/ReductionOpt/frames.html
.. _MSCRED: http://iraf.noao.edu/iraf/ftp/iraf/extern/mscred/
.. _MSCDB: http://iraf.noao.edu/iraf/ftp/iraf/extern/mscdb/
