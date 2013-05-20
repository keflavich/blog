Failed fields
#############
:date: 2008-09-13 21:00
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, mapping
:slug: failed-fields

-  l030 - comments were in the form ;; instead of # in the infile
-  l055 - no such folder
-  l026 - no infile existed; made one
-  l028 - /scratch/sliced\_polychrome/l028/060605\_o[\*\*]\_raw\_ds5.nc
   are bad
-  l031 - Downsampling seems to have failed for most of this directory.
   Need to downsample all files and create a new infile
-  l035 - /scratch/sliced\_polychrome/l035/060605\_o[\*\*]\_raw\_ds5.nc
   are bad - that's all 060605 observations of l035.
-  l036 - /scratch/sliced\_polychrome/l036/070702\_o25\_raw\_ds5.nc,
   /scratch/sliced\_polychrome/l036/070705\_o21\_raw\_ds5.nc are bad
-  l038 - /scratch/sliced\_polychrome/l038/060627\_ob3\_raw\_ds5.nc,
   /scratch/sliced\_polychrome/l038/060627\_ob[3567]\_raw.nc are bad -
   had to re-preprocess
-  l054 - /scratch/sliced\_polychrome/l054/070724\_o25\_raw\_ds5.nc is
   bad
-  l057 - /scratch/sliced\_polychrome/l057/070907\_o16\_raw\_ds5.nc is
   bad

Except for l057, there is no guarantee that the whole observation is
bad, BUT the code failed on ncdf\_open, so it possible the observation
turned bad during downsampling/preprocessing.
fixed: 30, 26, 55, 35, 28, 31, 38, 54, 57
so far all observations on 060605 are bad.

