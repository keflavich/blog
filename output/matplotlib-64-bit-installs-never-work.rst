matplotlib 64 bit installs never work
#####################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, matplotlib, computer

a clue as to why:
functional ft2font.so:
``$ otool -L /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/matplotlib/ft2font.so /Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/site-packages/matplotlib/ft2font.so: /usr/local/lib/libfreetype.6.dylib (compatibility version 10.0.0, current version 10.22.0) /usr/lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.3) /usr/local/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.14.0) /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 125.2.11)``
nonfunctional ft2font.so:
``$ otool -L /Users/adam/repos/yt/yt-i386/lib/python2.7/site-packages/matplotlib/ft2font.so/Users/adam/repos/yt/yt-i386/lib/python2.7/site-packages/matplotlib/ft2font.so: /Users/adam/repos/yt/yt-i386/lib/libfreetype.6.dylib (compatibility version 13.0.0, current version 13.2.0) /Users/adam/repos/yt/yt-i386//lib/libz.1.dylib (compatibility version 1.0.0, current version 1.2.3) /usr/local/lib/libstdc++.6.dylib (compatibility version 7.0.0, current version 7.14.0) /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 125.2.11) /usr/local/lib/libgcc_s.1.dylib (compatibility version 1.0.0, current version 1.0.0)``
The culprit is the difference between those two (maybe?):
``$ file /usr/local/lib/libgcc_s.1.dylib/usr/local/lib/libgcc_s.1.dylib: Mach-O universal binary with 4 architectures/usr/local/lib/libgcc_s.1.dylib (for architecture i386): Mach-O dynamically linked shared library i386/usr/local/lib/libgcc_s.1.dylib (for architecture x86_64): Mach-O 64-bit dynamically linked shared library x86_64/usr/local/lib/libgcc_s.1.dylib (for architecture ppc): Mach-O dynamically linked shared library ppc/usr/local/lib/libgcc_s.1.dylib (for architecture ppc64): Mach-O 64-bit dynamically linked shared library ppc64$ otool -L /usr/local/lib/libgcc_s.1.dylib/usr/local/lib/libgcc_s.1.dylib: /usr/local/lib/libgcc_s.1.dylib (compatibility version 1.0.0, current version 1.0.0) /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 88.3.9)``
