Comparing tclean parameters
###########################
:date: 2016-01-14 09:57
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: casa, clean, tclean

Comparing clean methods with identical data & parameters (as far as possible):
`code <https://github.com/keflavich/W51_ALMA_2013.1.00308.S/blob/master/script_merge/clean_method_comparison.py>`_.

An example using natural weighting:

.. image:: |static|/images/casa/tclean_compare.png
   :width: 600px

None of the methods are acceptable.  Multiscale is the worst, but hogbom is
extremely bad: there are major ringing artifacts (stripes parallel to the main
filament).


Disturbingly, even though I have given multiple scales, there are clearly no
non-pointlike scales in any of the model images, including mem, so I think
there's a major problem with tclean:

.. image:: |static|/images/casa/tclean_compare_models.png
   :width: 600px

I'm re-doing it with uniform weighting, because that's the case I was actually
interested in.


.. image:: |static|/images/casa/tclean_compare_uniform.png
   :width: 600px

The uniform tests come up with a clear and obvious answer: use clark clean, DO
NOT use any other methods as they are all unstable.
