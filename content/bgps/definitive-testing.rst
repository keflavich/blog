Definitive Testing
##################
:date: 2011-04-11 19:09
:author: Adam (noreply@blogger.com)
:tags: googlepost, testing, pipeline
:slug: definitive-testing

It is now possible to make artificial timestreams!
First round of tests:
For pointing maps with ~21 scans in 15" steps, array angle is
approximately negligible.
deconv does NOT recover point sources, but reconv does (perfectly)
The algorithm starts to decay and produce weird ringey residuals at a
S/N ~300. The residuals are only at the 1% level out to S/N ~1000.
