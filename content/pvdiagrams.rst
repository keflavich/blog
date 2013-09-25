Position-Velocity Diagrams
==========================
:date: 2013-09-24
:author: Adam Ginsburg (adam.g.ginsburg@gmail.com)
:tags: python, spectra

Current state of affairs
------------------------


Position-velocity diagrams with arbitrary position axes have been a common tool
for studying spectra for a long time, probably because the "native" format of
long-slit spectra on CCDs is effectively a position-velocity diagram.

It's becoming more common now to have data cubes (PPV) than 1D or 2D spectra.
But PV diagrams still have utility.  Unfortunately, there aren't very good
tools to produce them.

There are plenty of tools that can slice along any of the native axes of a data
cube.  If you take your data cube in RA/Dec space, extracting along lines of
constant RA or Dec is trivial (`GAIA`_ can do it natively, but it's easy to
slice a cube in IDL or python).

However, if you wanted to slice along lines of constant GLON or GLAT, you'd
have to reproject the cube to use this approach.  There are nice tools that
implement cube rotation: CASA has an `imrebin recipe`_ and STARLINK has a
rotation tool (though I can't find it now...).

However, this approach is terribly inefficient if you want slices at multiple
different angles, and it's outright awful if you want to track a filament.

An alternative approach
-----------------------

The alternative is to interpolate between pixels along a specified axis.  This
can be done very efficiently in python using scipy's map_coordinates_, which
by default does a cubic-spline interpolation at the specified points.

I've started to build a tool to extract position-velocity diagrams on this
basis.  It's fully functional, but doesn't do anything interactive just yet.
pvextractor_ is `available on github`_.

There is a complete example demonstrating its use `here`_.

In short, though, it allows you to describe paths like this:

.. image:: |filename|/images/paths_i05358.png
   :width: 800px

and extract them into position-velocity diagrams like this:

.. image:: |filename|/images/pv_i05358.png
   :width: 800px


.. _GAIA: http://star-www.dur.ac.uk/~pdraper/gaia/gaia.html
.. _imrebin recipe: http://star-www.dur.ac.uk/~pdraper/gaia/gaia.html
.. _map_coordinates: http://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.interpolation.map_coordinates.html
.. _pvextractor: https://github.com/keflavich/pvextractor
.. _available on github: http://keflavich.github.io/pvextractor/
.. _here: http://keflavich.github.io/pvextractor/examples/IRAS05358Slicing.html
