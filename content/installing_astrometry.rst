Installing astrometry.net in November 2014
##########################################
:date: 2014-11-26 9:57
:author: Adam 
:tags: install

Installing astrometry.net is all about navigating dependency hell.

Requirements:

 - libpng
 - libtiff
 - libjpeg
 - netpbm (requires above 3)

To install netpbm, a recent version - NOT the stable version - is required,
which means navigating throught 3-4 layers of links including a sourceforge
build-my-tarball link.

To compile astrometry.net-0.50:

        ARCH_FLAGS="" make -j 8

To compile cairo, I had to install pixman (no problem) the setup a PKG_CONFIG_PATH:

    PKG_CONFIG_PATH=/usr/local/lib/pkgconfig ./configure

