casa's plotms in a notebook
###########################
:date: 2021-06-14 12:30 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa

CASA's plotms requires an X11 frontend to work properly, so you either need to run it with xvfb or
with X.

I want to just make UV data plots in jupyter notebooks.

This is harder than it sounds, particularly for concatenated data sets.

First step is that you need to assemble the metadata:

.. code-block:: python
    msmd.open(scvis)
    scsum = msmd.summary()
    msmd.close()

The resulting ``scsum`` is a nested dictionary containing a ton of information.
We need only some of it.

To get out some flattened information, such as the "data description IDs" associated
with data that are actually in my concatenated MS (in my case, 8 of 11 observation blocks
in the metadata are not present in the data), this tool gets and flattens the resulting
information:

.. code-block:: python
    def walk_summary(summary, key):
        if isinstance(summary, dict):
            try:
                if key in summary:
                    return summary[key]
                else:
                    result = [walk_summary(summary[kk], key) for kk in summary]
                    try:
                        result = np.unique([x for x in result if x is not None])
                        if len(result) > 0:
                            return result
                    except:
                        return [x for x in result if x is not None]
            except (KeyError,TypeError):
                return

Then we grab the usable observation and data description IDs:                

.. code-block:: python
    obsids = [key for key in scsum if 'observationID' in key and scsum[key] != {}]
    ddids = walk_summary(scsum, 'data description IDs')


Now we have to load the actual data.  I needed to create new versions of the ``mstool`` each time
because I was getting weird errors where ``ms.close()`` followed by ``ms.open(fn)`` was not properly
resetting, which resulted in ``ms.getdata`` returning the same data for two different MSes - BAD!

.. code-block:: python
    ms6 = mstool()
    ms6.open(scvis)
    scdata_all = {}
    for ddid in ddids:
        ms6.selectinit(ddid, reset=True)
        ms6.selectinit(ddid)
        scdata_all[ddid] = ms6.getdata(['amplitude', 'weight', 'uvdist', 'axis_info', 'flag', 'corrected_amplitude'], ifraxis=True)
    ms6.close()


Then plotting is a hassle, but at least is not insane - it's just normal array manipulation:

.. code-block:: python
    pl.figure(figsize=(12,12))
    colors = itertools.cycle(pl.rcParams["axes.prop_cycle"].by_key()["color"])
    for key in scdata_all: # the keys are SPW numbers from the multi-MS file
        weight = scdata_all[key]['weight']
        uvd = scdata_all[key]['uvdist']
        pl.semilogy(uvd.ravel(), weight.reshape(weight.shape[0], uvd.size).T, ',', color=next(colors), label=key, alpha=0.5)
    pl.legend(loc='best')
    pl.xlabel("UV Distance (m)")
    pl.ylabel("Weight")

That is basically equivalent to ``plotms(vis, xaxis='uvdist', yaxis='weight', coloraxis='spw')``.  It's just slightly more flexible, since
you can also make waterfall plots, etc.

Selecting along various axes, like antenna, gets tricky.  You'd rather not go back to ``ms.getdata`` because it is _slow_.


The "identifying baselines" step that you can do in plotms can be achieved through normal boolean array selection, with a result that's somewhat easier to read than CASA's logger:

.. code-block:: python

    highwt = (scdata_all[56]['weight'] > 1e5)
    scdata_all[56]['axis_info']['ifr_axis']['ifr_name'][highwt.any(axis=(0,2))]
    # array(['DA41-DV12', 'DA42-DV12', 'DA43-DV12', 'DA44-DV12', 'DA45-DV12',
    #  'DA46-DV12', 'DA47-DV12', 'DA48-DV12', 'DA49-DV12', 'DA50-DV12',
    #  'DA51-DV12', 'DA52-DV12', 'DA53-DV12', 'DA54-DV12', 'DA55-DV12',
    #  'DA56-DV12', 'DA57-DV12', 'DA58-DV12', 'DA60-DV12', 'DA61-DV12',
    #  'DA62-DV12', 'DA63-DV12', 'DA64-DV12', 'DA65-DV12', 'DV01-DV12',
    #  'DV02-DV12', 'DV03-DV12', 'DV04-DV12', 'DV05-DV12', 'DV06-DV12',
    #  'DV07-DV12', 'DV08-DV12', 'DV09-DV12', 'DV10-DV12', 'DV11-DV12',
    #  'DV12-DV14', 'DV12-DV16', 'DV12-DV17', 'DV12-DV19', 'DV12-DV20',
    #  'DV12-DV21', 'DV12-DV22', 'DV12-DV23', 'DV12-DV24', 'DV12-DV25'],
    # dtype='<U16')

in this case, the output shows that DV12 is clearly the antenna that's overweighted.


Handling flags is tricky.  The 'weight' array has shape ``[2,nbaseline,ntime]``, but I don't know if that 2 refers to frequency
or polarization, since I have two of each and there is no information about this in the ``axis_info`` dictionary.  So... I'm
doing the conservative thing and ignoring any row of frequency or polarization if _any_ of the data are flagged.

.. code-block:: python
    pl.figure(figsize=(12,12))
    colors = itertools.cycle(pl.rcParams["axes.prop_cycle"].by_key()["color"])
    for key in scdata_all:
        weight = scdata_all[key]['weight']
        uvd = scdata_all[key]['uvdist']
        flag = scdata_all[key]['flag']
        okflag = ~np.any(flag, axis=(0,1))
        pl.semilogy(uvd[okflag], weight.reshape(weight.shape[0], uvd.size).T[okflag.ravel(), :], ',', color=next(colors), label=key, alpha=0.5)
    pl.legend(loc='best')
    _=pl.xlabel("UV Distance (m)")
    _=pl.ylabel("Weight")

And, indeed, doing this revealed that the super-high-weight antenna was already flagged out.


This has been a demo of how to do some stuff with CASA to replicate plotms


Errors
******

Along the way, I hit a ton of errors I didn't understand, so I need a record of what they mean.


"Data shape varies, selecting first data desc id only"
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the worst.  It means that you have a multi-ms file (mms) that has been produced by ``concat``.  It is therefore doing something *explicitly wrong* and returning only the first data description ID.

Data description IDs are super counterintuitive.  They refer, afaict, to SPW numbers.  If you have an MMS with unmerged SPWs (same frequency, but you didn't merge them because of tolerances or something),
each SPW will correspond to a single observation ID.  

The solution is to explicitly ``ms.selectinit``, i.e.:

.. code-block:: python
   ms.open(vis)
   ms.selectinit(datadescid) # note: "reset=True" appears to _override_ the selection
   ms.select(...) # use this as needed
   data = ms.getdata(...)
   ms.close()

but ``datadescid`` is _not_ the observation ID.  It's just... some number you need to get from the metadata.


Mismatched data shapes when comparing two MSes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I got into this whole thing because I wanted to compare the data in two MSes to determine where we went wrong (we did go wrong).

Unfortunately, somewhere along the way, the autocorrelations got dropped.  I don't know how it happened because I never did it
(but I wish I had earlier), but that means that now the data shapes are mismatched.

The solution was to use ``ms.select`` and explicitly downselect to the baselines from MS #1 in MS #2 using MS #1's ``axis_info``: ``{'ifr_number': scdata['axis_info']['ifr_axis']['ifr_number']}``:

.. code-block:: python
    ms3 = mstool()
    ms3.open(newvis)
    ms3.selectinit(80) # 80? what the hell kind of datadescid is that?!
    ms3.select({'ifr_number': scdata['axis_info']['ifr_axis']['ifr_number']})
    newdata = ms3.getdata(['amplitude', 'uvdist', 'axis_info', 'corrected_amplitude'], ifraxis=True)
    ms3.close()
    newdata.keys()

That downselected the baselines to match the baselines present in ``scdata``, which was MS 1.

The wrong data are showing up when I open a new MS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I was comparing several MSes, and sometimes the data looked the same for MSes I was *dead certain* were different.
I was right, and the problem was apparently reusing the ms tool.

I didn't show the import statement above, but it was this:

.. code-block:: python
    from casatools import ms, msmetadata
    mstool = ms
    ms = ms()
    msmd = msmetadata()

If I tried to reuse ``ms`` as normal, like so:

.. code-block:: python
   
   ms.open(vis1)
   ms.selectinit(80)
   data1 = ms.getdata(...)
   ms.close()

   ms.open(vis2)
   ms.selectinit(80)
   data2 = ms.getdata(...)
   ms.close()

then I can't say exactly what ``data1`` and ``data2`` are, but they weren't the same.

So, instead, I created a new ``mstool`` instance each time:

.. code-block:: python

   ms = mstool()
   ms.open(vis1)
   ms.selectinit(80)
   data1 = ms.getdata(...)
   ms.close()

   ms = mstool()
   ms.open(vis2)
   ms.selectinit(80)
   data2 = ms.getdata(...)
   ms.close()



Put all together...
*******************

Here's some code to loop over a list of MSes and plot both amp and weight vs. uvdist for the field W43-MM3.

Of course this crashed immediately because it exceeded the available memory.

.. code-block:: python

   for vis in mses:
       msmd.open(vis)
       vissum = msmd.summary()
       msmd.close()
    
       vobsids = [key for key in vissum if 'observationID' in key and vissum[key] != {}]
       vddids = walk_summary(vissum, 'data description IDs')
       fids = np.where(vissum['fields'] == 'W43-MM3')[0]
       print(f"obsids: {vobsids}, ddids: {vddids}")
    
       ms = mstool()
       ms.open(vis)
       msdata_all = {}
       for ddid in vddids:
           ms.selectinit(ddid, reset=True)
           ms.selectinit(ddid)
           ms.select({'field_id': fids})
           msdata_all[ddid] = ms.getdata(['amplitude', 'weight', 'uvdist', 'axis_info', 'flag', 'corrected_amplitude'], ifraxis=True)
       ms.close()

       colors = itertools.cycle(pl.rcParams["axes.prop_cycle"].by_key()["color"])
       pl.figure(figsize=(12,12))
    
       for key in msdata_all:
           weight = msdata_all[key]['weight']
           uvd = msdata_all[key]['uvdist']
           flag = msdata_all[key]['flag']
           okflag = ~np.any(flag, axis=(0,1))
           pl.semilogy(uvd[okflag], weight.reshape(weight.shape[0], uvd.size).T[okflag.ravel(), :], ',', color=next(colors), label=key, alpha=0.5)
       pl.legend(loc='best')
       pl.set_title(vis)
       _=pl.xlabel("UV Distance (m)")
       _=pl.ylabel("Weight")
    
       colors = itertools.cycle(pl.rcParams["axes.prop_cycle"].by_key()["color"])
       pl.figure(figsize=(12,12))
    
       for key in msdata_all:
           amp = msdata_all[key]['amplitude']
           uvd = msdata_all[key]['uvdist']
           flag = msdata_all[key]['flag']
           okflag = ~np.any(flag, axis=(0,1))
           pl.plot(uvd[okflag], amp.reshape(amp.shape[0]*amp.shape[1], uvd.size).T[okflag.ravel(), :], ',', color=next(colors), label=key, alpha=0.5)
       pl.legend(loc='best')
       pl.set_title(vis)
       _=pl.xlabel("UV Distance (m)")
       _=pl.ylabel("Amplitude")    
