Gem OB1
#######
:date: 2009-01-14 23:49
:author: Adam (noreply@blogger.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, mapping
:slug: gem-ob1

With Miranda's help, I discovered some serious errors in Gem OB1 and
fixed them.

#. L189 was using L134 data for no apparent reason
#. many September 2007 observations have the WRONG rotation angle in
   place in array\_params! Unfortunately it's not clear yet which ones
   suffer from this problem: I need a list of when rotangle was/was not
   used, and it looks like it'll be a pain to fix the problem.
#. GemOB1link wasn't mapped, it will be now.

.. raw:: html

   </p>

