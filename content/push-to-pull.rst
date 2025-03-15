Pushing to a pull request
#########################
:date: 2025-03-15
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: github


A very common workflow in open source development is for someone to open a pull request onto your (or the upstream) repository from their fork, and then if "Maintainers are allowed to edit this pull request." is checked, you want to edit their PR.

This is a pain in the ass if you try to use any documented command line tools.  Github docs tell you how to check out the PR, but not how to push it back - all of the online docs I found, and both chatGPT and Claude, require that you add the PR's fork as a remote.   That's stupid.

The better way is:

.. code-block:: bash

    git fetch origin pull/<PULL_REQUEST_NUMBER>/head:<LOCAL_BRANCH_NAME>
    # ... make edits ...
    git commit -am 'I edited the PR'
    git push git@github.com:<contributor-name>/<repo-name>.git <LOCAL_BRANCH_NAME>:<REMOTE_BRANCH_NAME>

so, for example, we tried this on my CV from ``alissapajer``:

.. code-block:: bash

    git fetch origin pull/1/head:alissapajer-patch-1
    git checkout alissapajer-patch-1
    git commit -am 'blah'
    git push git@github.com:alissapajer/keflavich-cv.git HEAD:alissapajer-patch-1

(`HEAD` works here b/c I was still on that branch)

It would also work, and be more explicit, to use the remote name:

.. code-block:: bash

    git fetch git@github.com:alissapajer/keflavich-cv.git alissapajer-patch-1