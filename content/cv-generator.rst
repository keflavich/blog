Generating a Pretty CV using the ADS Labs API
=============================================
:date: 2013-09-21
:author: Adam (keflavich@gmail.com)
:tags: python


At `.astronomy <http://dotastronomy.com/>`__ this past week, the keynote
speaker was `Alberto
Accomazzi <https://www.cfa.harvard.edu/~alberto/>`__, introducing ADS
Labs and `ADS 2.0 <http://labs.adsabs.harvard.edu/adsabs/>`__, which are
really quite impressive.

I was inspired to use ADS Labs to help me auto-generate a nicely
formatted CV for myself. I used `Andy
Casey's <https://twitter.com/astrowizicist>`__
`ADS-python <https://github.com/andycasey/ads-python>`__ as a starting
point: he introduces a useful convention of storing your `ADS API
Key <https://github.com/adsabs/adsabs-dev-api#signup--access>`__:


In[1]:

.. code:: python


    import os
    
    def get_dev_key():
        """ A convenience function for accessing a system-wide ADS Developer's Key """
    
        ads_dev_key_filename = os.path.abspath(os.path.expanduser('~/.ads/dev_key'))
    
        if os.path.exists(ads_dev_key_filename):
            with open(ads_dev_key_filename, 'r') as fp:
                dev_key = fp.readline().rstrip()
    
            return dev_key
    
        if 'ADS_DEV_KEY' in os.environ:
            return os.environ['ADS_DEV_KEY']
    
        raise IOError("no ADS API key found in ~/.ads/dev_key")

We'll use ``requests`` to send the request to ADS, then ``json`` to
parse the data.


In[2]:

.. code:: python


    import requests
    import json

We then query the database using a keyword query (parameter ``q``)
specifying the author. Other required parameters are the API key
(``dev_key``) and a filter to select only astronomy articles. The
maximum number of rows returned in the API is 200 right now, which I
have set (the default is 10 or 20).


In[3]:

.. code:: python


    response = requests.post('http://adslabs.org/adsabs/api/search/',
                             params={'q':'author:ginsburg, a',
                                     'dev_key':get_dev_key(),
                                     'rows':200,
                                     'filter':'database:astronomy'})


In[4]:

.. code:: python


    J = response.json()
    J.keys()





.. parsed-literal::
    [u'meta', u'results']



The JSON 'meta' key is just metadata about the query, include the number
of matches and execution time.


In[5]:

.. code:: python


    J['meta']





.. parsed-literal::
    {u'api-version': u'0.1',
     u'count': 54,
     u'hits': 54,
     u'qtime': 3,
     u'query': u'author:ginsburg, a'}



The 'results' key includes what we're actually interested in, under
another key 'docs'.


In[6]:

.. code:: python


    J['results'].keys()





.. parsed-literal::
    [u'docs']




In[7]:

.. code:: python


    datalist = J['results']['docs']
    type(datalist), len(datalist)





.. parsed-literal::
    (list, 54)



``datalist`` is a list of the retrieved bibliographic entries.


In[8]:

.. code:: python


    datalist[0].keys()





.. parsed-literal::
    [u'bibcode',
     u'keyword',
     u'pubdate',
     u'title',
     u'property',
     u'aff',
     u'author',
     u'citation_count',
     u'pub',
     u'page',
     u'volume',
     u'database',
     u'doi',
     u'year',
     u'abstract',
     u'identifier',
     u'issue',
     u'id']



At this point, most of the remaining work is building up a nicely
formatted output. We'll start with a web-specific example, using HTML
unordered lists.

In this example, we'll make a list item that creates a hyperlink for the
author names and uses a reasonably standard bibliographic format:

::

    Authors Month, Year, Journal
    Title



In[9]:

.. code:: python


    fmt = u'''                <li><a class="norm" href="http://adsabs.harvard.edu/abs/{adsbibid}">{creator}</a> {month}, <b>{year}</b> {journal}
                    <br>&nbsp;&nbsp;&nbsp;{titlestring}'''

We need to do a little data wrangling to get the individual JSON entries
into the appropriate format:


In[10]:

.. code:: python


    def wrangle(data, authorname='Ginsburg'):
        """ Create new fields from the input data to insert into the format string """
        data['month'] = data['pubdate'][5:7]
        # Generally, the last identifier is the published version, 
        # while the first is an arXiv identifier
        # (data['identifier'] is a list)
        data['adsbibid'] = data['identifier'][-1]
        # data['title'] & ['pub'] are also lists
        data['titlestring'] = data['title'][0]
        data['journal'] = data['pub'][0]
        # This trick bolds my name in the list of authors
        data['authors'] = ['<b>{}</b>'.format(x) if authorname in x else x for x in data['author']]
        # Separate names by semicolons
        data['creator'] = u"; ".join(data['authors'])
        return data


The return from ``wrangle`` is a dict with new keys that match the
keywords in the format string. The python ``string.format`` method will
nicely ignore any extra keywords that we're uninterested in.


In[11]:

.. code:: python


    fmt.format(**wrangle(datalist[0]))





.. parsed-literal::
    u'                <li><a class="norm" href="http://adsabs.harvard.edu/abs/2013ApJ...773..102F">Fallscheer, C.; Reid, M. A.; Di Francesco, J.; Martin, P. G.; Hill, T.; Hennemann, M.; Nguyen-Luong, Q.; Motte, F.; Men\'shchikov, A.; Andr\xe9, Ph.; Ward-Thompson, D.; Griffin, M.; Kirk, J.; Konyves, V.; Rygl, K. L. J.; Sadavoy, S.; Sauvage, M.; Schneider, N.; Anderson, L. D.; Benedettini, M.; Bernard, J. -P.; Bontemps, S.; <b>Ginsburg, A.</b>; Molinari, S.; Polychroni, D.; Rivera-Ingraham, A.; Roussel, H.; Testi, L.; White, G.; Williams, J. P.; Wilson, C. D.; Wong, M.; Zavagno, A.</a> 08, <b>2013</b> T\n                <br>&nbsp;&nbsp;&nbsp;Herschel Reveals Massive Cold Clumps in NGC\xa07538'



Now to show it in the notebook...


In[12]:

.. code:: python


    import IPython.display
    IPython.display.HTML(fmt.format(**wrangle(datalist[0])))







You can make a complete bibliography by looping over a few entries. The
ordered list (``<ol>``) tag makes a numbered list.


In[13]:

.. code:: python


    html = "<ol>" + "\n".join(fmt.format(**wrangle(datalist[ii])) for ii in xrange(3)) + "</ol>"
    IPython.display.HTML(html)







If you want to make sure you only include refereed articles, use the
'property' tag.


In[14]:

.. code:: python


    print ['REFEREED' in d['property'] for d in datalist]



.. parsed-literal::

    [True, False, True, False, False, False, True, True, False, False, False, False, True, True, True, False, False, True, True, False, False, True, True, True, False, False, False, False, True, False, False, True, True, True, True, True, True, False, False, False, False, False, False, True, True, False, False, False, False, True, False, False, False, True]


Wishlist
--------

There are a few other features that would be nice to add to the CV, but
some are not yet well-supported.

1. You can get the full name, but right now not the short name
   ('bibstem'), of the journal
2. The bibtex entry is important for generating tex versions of CVs.
   Currently, it is not possible to completely reproduce one, largely
   because of point #1.

However, the ADS folks will certainly change this soon. You can find out
if they have by querying their API settings. If the query below returns
"True", then you can access the bibstem.


In[15]:

.. code:: python


    permissions_response = requests.post('http://adslabs.org/adsabs/api/settings/',params={'dev_key':get_dev_key()})
    permissions = permissions_response.json()
    'bibstem' in permissions['allowed_fields']





.. parsed-literal::
    False



In the meantime, you can get most of the way there. We'll create
"Article" entries for any articles or eprints and ignore abstracts
(e.g., conference abstracts). I don't have any books, but for others
that might be useful.

The approach we'll use is also a good way to reject unwanted articles in
the HTML bibliography above.


In[16]:

.. code:: python


    bibfmt = u"""@article{{{tagname},
    abstract={{{abstract}}},
    author={{{bibtexauthors}}},
    month={{{month}}},
    pages={{{page}}},
    title={{{titlestring}}},
    year={{{year}}},
    volume={{{volume}}}
    }}"""

Of course, it's necessary to wrangle the data again for the appropriate
author list formatting for bibtex:


In[17]:

.. code:: python


    def wrangleauthors(authorlist):
        """ Fit the author list into a bibtex-friendly format.  
        Not the cleanest hack, since we need to allow for single-name
        authors (e.g., astropy collaboration, Planck collaboration, etc.)
        The triple braces are needed because TeX uses them"""
        splita = [[b.strip() for b in a.split(",")] for a in authorlist]
        bracketed = [u'{{{}}}, {}'.format(a[0], a[1].replace(" ","~"))
                     if len(a) > 1
                     else u'{{{}}}'.format(a[0])
                     for a in splita]
        return u" and ".join(bracketed)


In[18]:

.. code:: python


    wrangleauthors(datalist[0]['author'])





.. parsed-literal::
    u"{Fallscheer}, C. and {Reid}, M.~A. and {Di Francesco}, J. and {Martin}, P.~G. and {Hill}, T. and {Hennemann}, M. and {Nguyen-Luong}, Q. and {Motte}, F. and {Men'shchikov}, A. and {Andr\xe9}, Ph. and {Ward-Thompson}, D. and {Griffin}, M. and {Kirk}, J. and {Konyves}, V. and {Rygl}, K.~L.~J. and {Sadavoy}, S. and {Sauvage}, M. and {Schneider}, N. and {Anderson}, L.~D. and {Benedettini}, M. and {Bernard}, J.~-P. and {Bontemps}, S. and {Ginsburg}, A. and {Molinari}, S. and {Polychroni}, D. and {Rivera-Ingraham}, A. and {Roussel}, H. and {Testi}, L. and {White}, G. and {Williams}, J.~P. and {Wilson}, C.~D. and {Wong}, M. and {Zavagno}, A."



Now we can start looping through, performing checks for article status,
and making bibentries:


In[19]:

.. code:: python


    for d in datalist:
        d['bibtexauthors'] = wrangleauthors(d['author'])
        d['tagname'] = d['author'][0].split()[0].strip(",") + d['year']


In[20]:

.. code:: python


    bibdata = ""
    for d in datalist:
        if 'ARTICLE' in d['property'] or 'EPRINT' in d['property']:
            bibdata += bibfmt.format(**d)



::

    ---------------------------------------------------------------------------
    KeyError                                  Traceback (most recent call last)

    <ipython-input-20-9c55bfea9ea0> in <module>()
          2 for d in datalist:
          3     if 'ARTICLE' in d['property'] or 'EPRINT' in d['property']:
    ----> 4         bibdata += bibfmt.format(**d)
    

    KeyError: u'volume'


Actually, this doesn't work. We'll need to try something else... the ADS
folks will probably provide.
