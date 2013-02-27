IDL syntax highlighting in VIM
##############################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, idl

I've edited my idlang.vim to auto-identify files that start with a
semicolon.
Add Line 19:
`` syn match idlangStatement "^\s*;\s"``
Line 61/2 (allow spaces before ;):
``syn match  idlangComment "\s*[\;].*$" contains=idlangTodo``
`AG`_

.. _AG: http://casa.colorado.edu/~ginsbura/index.htm
