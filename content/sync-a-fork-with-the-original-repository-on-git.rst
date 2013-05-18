Sync a fork with the original repository on Git
###############################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, git

A seemingly simple operation that I just can't seem to get right.
`This page`_ gives me useless information:
``$ git checkout -b upstream/master $ git remote add upstream git://github.com/upstream_maintainer/master.git $ git pull upstream remote $ git checkout master $ git merge upstream/master ``
If you do that, it frankly doesn't work. Why? "upstream/master" etc. all
have special meanings.
Here's the real process & explanation (thanks to Erik Tollerud for some
help):
``git checkout master  # (assuming you have a local branch named master - otherwise, pick whatever branch you want synced)git remote add original git@github.com:thing/thing.git # "upstream" = "original" = "remote" - the place you're trying to sync fromgit fetch original # 'original' being the name YOU gave for the "remote/original" repositorygit merge master original/master # now merge the "original/master" branch (they should have  a branch named "master" too, otherwise you have to figure out which branch to get) into your mastergit push # push your now-merged stuff back to github# I was instructed to use these commands.  They didn't work.# git reset original # the word "original" here matches the word "original" on the previous line# git reset --hard original # this will overwrite local changes``

.. _This page: http://groups.google.com/group/github/browse_thread/thread/6196487279beb2a8/181b7bc4bf7a3e16
