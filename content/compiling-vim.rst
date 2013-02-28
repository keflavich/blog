Compiling vim...
################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, install, vim

Figured I had to post this...
I've been trying to compile command-line vim 7.3 on Mac OS X 10.7. I
have the latest \`hg clone\`d version of vim. I'm stuck on ncurses.
If I \`./configure\` with no options, I get the following error:
checking --with-tlib argument... empty: automatic terminal library
selection
checking for tgetent in -ltinfo... no
checking for tgetent in -lncurses... no
checking for tgetent in -ltermlib... no
checking for tgetent in -ltermcap... no
checking for tgetent in -lcurses... no
no terminal library found
checking for tgetent()... configure: error: NOT FOUND!
You need to install a terminal library; for example ncurses.
Or specify the name of the library with --with-tlib.
If instead I try \`./configure --with-tlib=ncurses\`
checking --with-tlib argument... ncurses
checking for linking with ncurses library... configure: error: FAILED
I have Xcode 4.1. As far as I can tell, ncurses is available:
$ file /usr/lib/libncurses.\*
/usr/lib/libncurses.5.4.dylib: Mach-O universal binary with 2
architectures
/usr/lib/libncurses.5.4.dylib (for architecture x86\_64): Mach-O 64-bit
dynamically linked shared library x86\_64
/usr/lib/libncurses.5.4.dylib (for architecture i386): Mach-O
dynamically linked shared library i386
/usr/lib/libncurses.5.dylib: Mach-O dynamically linked shared library
i386
/usr/lib/libncurses.dylib: Mach-O universal binary with 2 architectures
/usr/lib/libncurses.dylib (for architecture x86\_64): Mach-O 64-bit
dynamically linked shared library x86\_64
/usr/lib/libncurses.dylib (for architecture i386): Mach-O dynamically
linked shared library i386
Then I changed my PATH from /usr/local/bin... to /usr/bin.....
The problem was trying to use my /usr/local/bin/gcc instead of the mac
default /usr/bin/gcc. Something about my locally installed gcc (4.6.1)
caused major problems.
I also eventually had to do this command:
LDFLAGS=-L/usr/lib CFLAGS='-arch i386 -arch x86\_64' CCFLAGS='-arch i386
-arch x86\_64' CXXFLAGS='-arch i386 -arch x86\_64' ./configure
--enable-perlinterp --enable-pythoninterp --enable-cscope
--with-features=huge
and then had to make sure my default python was NOT pointing to
enthought!
