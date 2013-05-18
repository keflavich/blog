Using AWK to fixed-format print in VIM
######################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, computer

.. raw:: html

   <p>

::

    24,42!awk '{printf("\%30s\%20f\%15g\%15g\%15g\%15g\%15g\%15g\%15g\%5i\n" , $1,$2,$3,$4,$5,$6,$7,$8,$9,$10)}'

It's important that the %'s must be escaped, otherwise they print the
current filename.

.. raw:: html

   </p>

