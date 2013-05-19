Scripting the Whole Survey
##########################
:date: 2008-09-16 00:43
:author: Adam (noreply@blogger.com)
:tags: googlepost, alignment, mapping, pipeline
:slug: scripting-the-whole-survey

First, discovered more fields with some sort of failure:

::

    ls -d l[0-3][0-9][0-9] | sed 's:\(.*\):ls \1/*_map01.fits > \1/\1_infile.txt:' | bashls: l004/*_map01.fits: No such file or directoryls: l017/*_map01.fits: No such file or directoryls: l025/*_map01.fits: No such file or directoryls: l108/*_map01.fits: No such file or directoryls: l135/*_map01.fits: No such file or directoryls: l136/*_map01.fits: No such file or directoryls: l137/*_map01.fits: No such file or directoryls: l138/*_map01.fits: No such file or directoryls: l192/*_map01.fits: No such file or directory

Also, that command was a total screwup.

::

    ls -d l[0-3][0-9][0-9] | sed 's:\(.*\):ls /scratch/adam_work/\1/*_map01.fits > \1/\1_fitslist.txt:' | bashls: /scratch/adam_work/l004/*_map01.fits: No such file or directoryls: /scratch/adam_work/l017/*_map01.fits: No such file or directorybash: line 12: l020/l020_fitslist.txt: Permission deniedls: /scratch/adam_work/l025/*_map01.fits: No such file or directoryls: /scratch/adam_work/l108/*_map01.fits: No such file or directoryls: /scratch/adam_work/l135/*_map01.fits: No such file or directoryls: /scratch/adam_work/l136/*_map01.fits: No such file or directoryls: /scratch/adam_work/l137/*_map01.fits: No such file or directoryls: /scratch/adam_work/l138/*_map01.fits: No such file or directoryls: /scratch/adam_work/l192/*_map01.fits: No such file or directory

Now that those files exist, it should be possible to run a set of
super-scripts like this:
coalign\_field,'l057','070719\_o29',sliced\_dir='sliced\_polychrome',premap=0
coalign\_field,'l351','070725\_ob3'
coalign\_field,'l354','070724\_o10'
coalign\_field,'l357','070724\_ob3'
coalign\_field,'l000','070719\_o14'
coalign\_field,'l003','070718\_o16'
coalign\_field,'l006','070715\_ob5'
coalign\_field,'l009','070717\_ob5'
coalign\_field,'l012','070715\_o10'
coalign\_field,'l015','070714\_o36'
coalign\_field,'l018','070717\_o10'
coalign\_field,'l021','070715\_o15'
coalign\_field,'l024','070717\_o15'
coalign\_field,'l027','070715\_o20'
coalign\_field,'l030','070717\_o20'
coalign\_field,'l033','070718\_ob5',sliced\_dir='sliced\_polychrome'
coalign\_field,'l036','070715\_o25',sliced\_dir='sliced\_polychrome'
coalign\_field,'l039','070717\_o25',sliced\_dir='sliced\_polychrome'
coalign\_field,'l042','070715\_o30',sliced\_dir='sliced\_polychrome'
coalign\_field,'l044','070718\_o24',sliced\_dir='sliced\_polychrome'
coalign\_field,'l048','070717\_o30',sliced\_dir='sliced\_polychrome'
coalign\_field,'l050','070718\_o29',sliced\_dir='sliced\_polychrome'
coalign\_field,'l054','070724\_o28',sliced\_dir='sliced\_polychrome'
coalign\_field,'l057','070719\_o29',sliced\_dir='sliced\_polychrome'
where premap=0 means I'm not re-mapping the whole field, the
sliced\_dir='slice\_polychrome' keyword is for those fields that do not
have a regular sliced directory.
This kind of thing ought to be really, really helpful when mapping the
fields whose masters are not in the field: I'll have to modify the
'coalign\_field' code to search in a different directory, though.
Yearghhh.... last command was bad too.

::

    ls -d l[0-3][0-9][0-9] | sed 's:\(.*\):ls /scratch/adam_work/\1/0*_map01.fits > \1/\1_fitslist.txt:' | bashls: /scratch/adam_work/l004/0*_map01.fits: No such file or directoryls: /scratch/adam_work/l017/0*_map01.fits: No such file or directorybash: line 12: l020/l020_fitslist.txt: Permission deniedls: /scratch/adam_work/l025/0*_map01.fits: No such file or directoryls: /scratch/adam_work/l108/0*_map01.fits: No such file or directoryls: /scratch/adam_work/l135/0*_map01.fits: No such file or directoryls: /scratch/adam_work/l136/0*_map01.fits: No such file or directoryls: /scratch/adam_work/l137/0*_map01.fits: No such file or directoryls: /scratch/adam_work/l138/0*_map01.fits: No such file or directoryls: /scratch/adam_work/l192/0*_map01.fits: No such file or directory

