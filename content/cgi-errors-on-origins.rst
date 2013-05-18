CGI errors on Origins
#####################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, computer

.. raw:: html

   <p>

First step:

::

    tail -f /usr/local/apache/logs/casa/casa_error_log

Then, make sure .htaccess has the right lines.

::

    AddType text/html  .htmAddHandler application/x-httpd-php .php .htmAddHandler server-parsed .htm .htmlAddHandler cgi-script .cgi .pl

.. raw:: html

   </p>

