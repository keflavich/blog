ALMA Cycle 9 corrupted zip fix
##############################
:date: 2022-04-14 09:18 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: alma, proposals

If you encounter a bug like this:

.. image:: |static|/images/ALMAC9ZipBug.png
   :width: 600px

"XML (syntax or validity) error" because you hit issue `C1_032 <https://almascience.eso.org/documents-and-tools/cycle9/known-issues>`_,
the fix is really easy:

.. code-block:: python

    import zipfile
    import os

    # not strictly necessary, but important if you want to avoid filling your directory with files
    os.mkdir('recovery')
    os.chdir('recovery')

    # replace with your AOT file name
    with zipfile.ZipFile('../corrupted.aot', 'r') as aot:
        # this will extract all the files into the current directory
        aot.extractall()
        files = aot.filelist

    with zipfile.ZipFile('../recovered.aot', 'w') as aot:
        for fh in files:
            aot.write(fh.filename)

At least, this worked on the one case where I got bitten.
