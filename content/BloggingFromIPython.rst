
Blogging from IPython
=====================


:author: Adam <keflavich@gmail.com>
:tags: python, blogging, meta
:date: 2013-09-22

[ `Notebook Form of this
post <http://nbviewer.ipython.org/urls/raw.github.com/keflavich/blog/master/content/BloggingFromIPython.ipynb>`__
]

There have been
`many <http://jmcarp.github.io/blog/2013/07/07/hello-world/>`__
`other <http://danielfrg.github.io/blog/2013/02/16/blogging-pelican-ipython-notebook/>`__
`posts <http://danielfrg.github.io/blog/2013/03/08/pelican-ipython-notebook-plugin/>`__
about blogging in ipython, but they all included more overhead than I
really wanted to deal with.

Instead, I've gone directly to `the
source <http://nbviewer.ipython.org/urls/raw.github.com/Carreau/posts/master/06-NBconvert-Doc-Draft.ipynb>`__
and used nbconvert in ipython 2.0 to convert my notebooks to rst, then
put them through pelican.

This post outlines my workflow.

First, and most inconvenient, it is necessary to head any blog post with
metadata. I don't have any convenient workflow to deal with that, I just
write it in by hand in a raw text box (ctrl-m, t) as you can see above.
`Daniel Rodriguez <http://danielfrg.github.io/>`__ took a `different
approach <http://danielfrg.github.io/blog/2013/03/08/pelican-ipython-notebook-plugin/>`__
using the ipython metadata directly and an ipython plugin, but I didn't
want to have to worry about installing plugins and I am definitely
worried about breaking notebooks by messing with the
`metadata <https://github.com/ipython/ipython/wiki/IPEP-20%3A-Informal-structure-of-cell-metadata>`__
as the ipy devs give some fairly `strict
warnings <https://gist.github.com/Carreau/4437348>`__.

Next, the ipynb -> rst step is fairly straightforward. I modified the
rst template because I don't want to see the ``In[#]:`` and ``Out[#]:``
prefixes around my code. I also use ``.. code-block::`` rather than
``.. code::``.

This very simple function below makes sure that my local ``rst.tbl``
file is seen before ipython's. Their templates are in
``IPython/nbconvert/templates``. Note that you could normally use Jinja2
templating and "Extend" their template, but I wanted to remove rather
than extend.

[
`Source <https://github.com/keflavich/blog/blob/master/nbconverter.py>`__
]


.. code-block:: python

    from IPython.nbconvert.exporters import RSTExporter
    
    def export(nbname, outfilename=None):
        exportRST = RSTExporter()
        # exclude default paths
        exportRST.template_path = ['.','/Users/adam/repos/blog'] 
    
        (body,resources) = exportRST.from_filename(nbname)
    
        if outfilename is None:
            outfilename = nbname.replace("ipynb","rst")
    
        with open(outfilename,'w') as f:
            f.write(body)
    
        return body,resources

I then run the script from the command line:
``~/virtual-ipydev/bin/ipython ./nbconverter.py content/GenerateCVExample.ipynb``

I'm using a virtual environment with ipython 2 installed because I'm not
yet ready to make the jump to the dev version of ipython (though these
days, with Travis and Jenkins around, it's probably safe to assume the
dev version won't break anything).

With this rst file generated, the only remaining step is
`pelican <http://blog.getpelican.com/>`__, which only requires a
``make github`` command in the blog directory. Installing & setting up
pelican is reasonably easy, but not the topic of this post.

I've made my own `custom pelican
theme <https://github.com/keflavich/pelican-themes/tree/master/mine>`__,
so I generally need to update the theme before building:

``pelican-themes --upgrade /Users/adam/repos/pelican-themes/mine && make github``
