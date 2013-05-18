Weird problem
#############
:date: 2011-03-31 02:25
:author: Adam (noreply@blogger.com)
:tags: googlepost, errors
:slug: weird-problem

I'm remapping everything, and there's a really strange situation in
ic1396... only one field has a source that doesn't have rotation
problems, every other observation is clearly improperly rotated. The
weird thing is that it's NOT the one you'd expect from the information
below:
``readcol,'/Volumes/disk2/sliced/infiles/ic1396_infile.txt',filelist,format='A'for i=0,6 do begin & ncdf_varget_scale,filelist[i],'array_params',ap & print,filelist[i],ap & endfor/Volumes/disk2/sliced/ic1396/070911_o19_raw_ds5.nc      7.70000      31.2000      70.7000      0.00000      0.00000/Volumes/disk2/sliced/ic1396/070912_o26_raw_ds5.nc      7.70000      31.2000      84.0000      0.00000      0.00000/Volumes/disk2/sliced/ic1396_d/070913_o19_raw_ds5.nc      7.70000      31.2000      84.0000      0.00000      0.00000/Volumes/disk2/sliced/ic1396_l/070913_o17_raw_ds5.nc      7.70000      31.2000      84.0000      0.00000      0.00000/Volumes/disk2/sliced/ic1396_r/070913_o18_raw_ds5.nc      7.70000      31.2000      84.0000      0.00000      0.00000/Volumes/disk2/sliced/ic1396_u/070913_o20_raw_ds5.nc      7.70000      31.2000      84.0000      0.00000      0.00000``
One ofthese things is not like the others... but it's
070913\_o18\_raw\_ds5.nc, not
/Volumes/disk2/sliced/ic1396/070911\_o19\_raw\_ds5.nc
