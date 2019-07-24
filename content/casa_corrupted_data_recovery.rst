CASA corrupted measurement sets
###############################
:date: 2019-07-23 13:11
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA


Over the weekend, I had a huge quantity of ALMA data get corrupted. The
corruption appears to have been caused by an incorrectly-mounted lustre system
that had "flock" disabled.  When they re-mounted the filesystem, every
measurement set I had touched was unreadable.

Corrupted data sets had messages like this when opened with ``msmd.open``::

    RuntimeError: Exception: Illegal DATA_DESC_ID value 30 found in main table. /lustre/cv/projects/ALMA_IMF/2017.1.01355.L/science_goal.uid___A001_X1296_X211/group.uid___A001_X1296_X212/member.uid___A001_X1296_X217/calibrated/uid___A002_Xcbdb2a_X6e67.ms.split.cal/DATA_DESCRIPTION only has 0 rows (IDs).
    ... thrown by void casa::MSChecker::checkReferentialIntegrity() const at File: ../../msvis/MSVis/MSChecker.cc, line: 78


The solution was to replace all of the ``table.dat`` files in the
``DATA_DESCRIPTION``, ``POLARIZATION``, ``STATE``, and ``PROCESSOR`` folders
with "backups" from the parent measurement set.  Luckily, all of my data were
split from other measurement sets that still existed, and they were split with
``reindex=False``, which meant that these tables were actually usable.  There's
no guarantee they would be in general.


My fix script is this:


.. code-block:: python

    def getdata(x):
        with open(x, 'rb') as fh:
            return fh.read()

    def diff(x, y):
        return {ii:(xx,yy) for ii,(xx,yy) in enumerate(zip(x, y)) if xx!=yy}

    def fix_bad_mses():
        for dirpath, dirnames, filenames in os.walk('.'):
            for fn in dirnames:
                if fn[-10:] == ".split.cal":
                    ffn = os.path.join(dirpath, fn)
                    workingfn = os.path.join(dirpath, 'working', fn[:-10])

                    if os.path.exists(workingfn):
                        #print("Working on files {0} and {1}".format(ffn, workingfn))
                        print(ffn)

                        for dn in ['POLARIZATION', 'PROCESSOR', 'DATA_DESCRIPTION', 'STATE']:
                            tbpth1 = os.path.join(ffn, dn, 'table.dat')
                            tbpth2 = os.path.join(workingfn, dn, 'table.dat')

                            if os.path.exists(tbpth1) and os.path.exists(tbpth2):
                                d1 = getdata(tbpth1)
                                d2 = getdata(tbpth2)
                                delta = diff(d1, d2)
                                #print("Diff from {0} to {1} is {2}".format(tbpth1, tbpth2, delta))

                                if len(delta) > 0:
                                    print("FIXING: Diff for {0} is {1}".format(dn, delta))
                                    shutil.copy(tbpth1, tbpth1+".bck")
                                    shutil.copy(tbpth2, tbpth1)




which spewed out a bunch of messages like this::

    FIXING: Diff for POLARIZATION is {24: ('\x00', '\x01'), 1059: ('\x00', '\x01')}
    FIXING: Diff for PROCESSOR is {24: ('\x00', '\x03'), 1078: ('\x00', '\x03')}
    FIXING: Diff for DATA_DESCRIPTION is {24: ('\x00', '\x18'), 772: ('\x00', '\x18')}
    FIXING: Diff for STATE is {24: ('\x00', '\x1d'), 1699: ('\x00', '\x1d')}

showing that for each bad file, two bytes were flipped.  I don't know how or why.  Notably, though,
the byte flips that corrupted the data did *not* change the file modification date - somehow CASA
hid this operation from the filesystem.
