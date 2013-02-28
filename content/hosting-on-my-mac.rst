Hosting on my mac
#################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer

I'm hosting my website off my mac; it should be accessible to the
outside world now: `eta.colorado.edu`_.
A few things went into this....

#. Don't install the fink version. The two versions clash and depending
   on how you access your computer you could end up looking at entirely
   different directories (e.g. localhost and eta.colorado.edu referred
   to different sites for a while)
#. The configuration file is /private/etc/apache2/httpd.conf
#. I needed to change DirectoryIndex to index.htm (from index.html)
#. uncommmented "LoadModule php5\_module libexec/apache2/libphp5.so"
#. had to allow override so that .htaccess files would work.

.. raw:: html

   </p>

.. _eta.colorado.edu: http://eta.colorado.edu/
