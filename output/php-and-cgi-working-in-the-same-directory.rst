PHP and CGI working in the same directory
#########################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, computer

.. raw:: html

   <p>

While it's not possible to get CGI and PHP to work within the same file,
you can get .html and .htm files to use cgi/php scripts alternately in
the same directory with the following .htaccess file:

::

    RemoveHandler  .htmlAddType text/html  .htmAddHandler application/x-httpd-php .php .html AddHandler server-parsed .htm .html 

If anyone can prove the previous statement false, please do! I spent
hours googling and hacking to try to get php and cgi to work within the
same file.
Also, the way the above file is parsed makes no sense to me. It is
inverted from how I would have thought it should work.

.. raw:: html

   </p>

