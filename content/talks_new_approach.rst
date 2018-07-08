Talks: Now using revealjs
#########################
:date: 2018-07-08 12:37
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: talks, w51, sgrb2, clusters


I'm attempting to wean myself off of Mac-specific technology, inspired by some
impending hardware failures (see below), the not-falling cost of not-improving
hardware, and the lack of budget growth.

Following a suggestion from `Peter Williams <https://github.com/pkgw/>`_, I'm
using reveal.js based on `Peter's template
<https://github.com/pkgw/htmltalk>`_, which I have previously played with a
little with mixed success.  The slid.es editor seems nearly fully featured as a
replacement for keynote, but I quickly dropped it because of its
subscription-only paid features; the cost-benefit analysis is that Keynote is
much cheaper than slid.es for someone like me, since Keynote cost $30 one-time
for ~10 years of use, while the minimum usable plan for slid.es is $10/month,
or $1200 over the same period.  If that was the tradeoff I was considering,
mac+keynote would be about the same as linux+slid.es.

I'm taking the somewhat ridiculous approach of raw HTML/CSS editing with the
Chrome inspector as my interactive testing tool.  This is a little tedious
because of the html tagging, but that's honestly not so bad; it lets me do the
hard work with the keyboard instead of the mouse.  The biggest problem is the
learning curve of css, but I look at that as skill and knowledge worth having.
If you don't, this is probably not the approach for you.  I hope, though, that
some day there is a slid.es-like solution that is reasonably priced.

Another problem is image editing, which was pretty convenient in keynote, but
there are plenty of other decent-to-good image editors out there, e.g., gimp,
preview, etc.  For cropping and opacity, which are most of what you want to do,
css works and can even be tested interactively in the browser.  But, this
should also give more motivation to just make the figures presentation-ready in
the code.

Anyway, the talks I've created are hosted at github, and they're fully-featured:
you should be able to just click these links and walk through the talks.

My "Tracing the Flow" invited talk on High Mass Cluster Formation:
https://keflavich.github.io/talks/HighMassClusterFormation_TracingTheFlow2018.html

Some slides for a work meeting on the ALMA-IMF project, with a technical bent:
https://keflavich.github.io/talks/ALMA_IMF_W51_SgrB2.html

If you want the pdf version of either of these, add ``?print_pdf`` to the end
of the URL, then use your browser to print and save to pdf.


Some pictures of the impending failure.  My mac doesn't close any more, and
the charger cable has frayed severely:

.. image:: |filename|/images/frayed_adapter.jpg
   :width: 600px

.. image:: |filename|/images/lappy_wont_close.jpg
   :width: 600px
