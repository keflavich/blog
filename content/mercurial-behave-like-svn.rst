Mercurial - behave like SVN?
############################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, mercurial, subversion

I'm trying to use hooks to make mercurial behave like svn when
committing. I like the idea that I can commit changes to my cloned repo
while I'm away from the internet, but I never want that behavior when I
do have internet access. Therefore, I want to attempt to pull before
updating and attempt to push after committing. Every time. I have been
consistently very unhappy with the ``hg merge`` command.
``[hooks]precommit = hg pull; hg uppostcommit= hg pushpost-pull = hg up``
However, this doesn't work. precommit freezes with the error
``waiting for lock on working directory of [dir] held by [procnum]``
and pre-commit results in other errors:
``running hook pre-commit: hg pull; hg uppulling from [source]searching for changesno changes foundrunning hook post-pull: hg upabort: outstanding uncommitted mergeswarning: post-pull hook exited with status 255abort: outstanding uncommitted mergeswarning: pre-commit hook exited with status 255``
`AG`_

.. _AG: http://casa.colorado.edu/~ginsbura/index.htm
