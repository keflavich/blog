Methods Paper: Figures / analysis to produce
############################################
:date: 2009-03-04 03:43
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, methods paper
:slug: methods-paper-figures-analysis-to-produce

The methods paper needs some justification of the number of PCA
components used. This will require a map of some field with a range of
number of PCA components.
Plan:
simulate a map of L111 (the most square field) with 0-20 PCA components
x 21 iterations and a variety of source sizes and plot the recovered
flux vs. number of PCA components. Ideally, do this with both
deconvolution and not. Estimated processing time is ~24 hours.
Also, a plot of flux vs. iteration number will be useful.
Glitch filtering method has been modified:
"Glitches are removed by drizzling each bolometer measurement into a
given pixel using the mapping M[p], but retaining each pixel as an array
of measurements. Then, measurements exceeding $3\\times MAD$ (Median
Average Deviation) are flagged out in the timestream. In cases where
there were too few ($<3$) hits per pixel, the pixel was completely
flagged out. This only occurred for pixels at scan edges."
Data flagging:
Partly covered by deglitching. Many scans were flagged by hand to remove
overly noisy scans and those that were observed to confuse the iterative
mapper. Hand flagging is more robust than automated and can remove
features caused by the filter convolved with the glitch.
Creation of astrophysical model:
Not entirely sure what this section entails. Should have a subsection on
deconvolution though.
Jackknifing has not generally been done...
