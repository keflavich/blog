Hacking plotms to let pipeline run
##################################
:date: 2022-04-11 08:02
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa

For the ACES project, I'm re-running the ALMA pipeline using MPI.

However, this results in all runs crashing with the following error:

.. code-block::

    2022-04-06 04:22:43 INFO: Executing plotms(vis='uid___A002_Xf512ae_X2626.ms', xaxis='azimuth', yaxis='elevation', spw='25:0~0,27:0~0,29:0~0,31:0~0,33:0~0,35:0~0', antenna='0&&*', avgchannel='9000', avgtime='10', coloraxis='field', customflaggedsymbol=True, flaggedsymbolshape='autoscaling', title='Elevation vs Azimuth for uid___A002_Xf512ae_X2626.ms', plotfile='azel.png', showgui=False, clearplots=True)
    fuse: failed to exec fusermount: No such file or directory

    Cannot mount AppImage, please check your FUSE setup.
    You might still be able to extract the contents of this AppImage
    if you run it with the --appimage-extract option.
    See https://github.com/AppImage/AppImageKit/wiki/FUSE
    for more information
    open dir error: No such file or directory


This fails even if I set the global APPIMAGE_EXTRACT_AND_RUN as `directed
<https://docs.appimage.org/user-guide/troubleshooting/fuse.html#extract-and-run-type-2-appimages>`_
on the appimage.org docs.

This indicates that the appimage is older than the environmental variable.

Running the full command "works":
``/orange/adamginsburg/casa/casa-6.2.1-7-pipeline-2021.2.0.128/lib/py/lib/python3.6/site-packages/casaplotms/__bin__/casaplotms-x86_64.AppImage --appimage-extract``
but ``--appimage-extract-and-run`` gives ``--appimage-extract-and-run is not yet implemented in version continuous-1-g6f3138f``

So to run plotms, we need to use the ``AppRun`` executable in the extracted ``squashfs-root`` directory.

My original hack was to just tell plotms not to run at all, which I accomplished by editing the
``plotmstool.py`` file (``lib/py/lib/python3.6/site-packages/casaplotms/private/plotmstool.py``) to
just skip the ``__launch`` command:

.. code-block:: python

    def __launch( uri=None ):
        return

However, in writing this post, I've changed to instead modifying the ``app_path`` to this:

.. code-block:: python

    app_path = "/tmp/casaplotms/squashfs-root/AppRun"
    if not __os.path.exists(app_path):
        print(f"Did not find extracted path {app_path}")
        app_path = __os.path.join( __os.path.abspath( __os.path.join(__os.path.dirname(__file__),"..") ), '__bin__/casaplotms-x86_64.AppImage')

I haven't tried it but I'm slightly hopeful.
