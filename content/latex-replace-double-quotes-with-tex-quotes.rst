LaTeX: replace double quotes with tex quotes
############################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, latex

People often make the mistake of putting " in place of \`\` in LaTeX
documents. To repair this, the only easy solution is something like:
s/\\(\\s\\)"/\\1\`\`/g
in VIM or sed.
I've seen alternate solutions posted but they're all too complicated.
One recommendation was to switch to XeTeX, which sounds like overkill,
and others all stated that a complicated perl script is required. The
latter is technically true, but why isn't such a thing readily
available?
Any other ideas?
