Listing variables (e.g IDL help) in Python
##########################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, python, computer

Again, IDL has the simple 'help' command to tell you all variables in
your namespace. Python has the same thing, but the namespace tends to be
cluttered with imported functions. The commands who, who\_ls, and whos
are meant for interactive use. They are a hell of a lot more useful than
var, locals, globals, and dir.
examples:
``whos floatwhos ndarraywho modulefloat_vars = %who_ls floatgrep('x',float_vars)``
I'm afraid I don't know how to make the last two lines into a one-liner,
as would be desirable.
