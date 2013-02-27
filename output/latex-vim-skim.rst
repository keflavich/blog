LaTeX: VIM + Skim
#################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, latex, vim, code

.. raw:: html

   <p>

`macvim-skim-install.sh`_ is my install script for using MacVim.app with
Skim.app.
The `agpy wiki page`_ has instructions that are probably more clear; I
don't really like the colorscheme / layout of this blog.
You can use `synctex`_ to make an editor and viewer work together, but
it is far from easy and far harder than it should be. Forward-search is
pretty easy, but the latex-suite ``\ls`` only works intermittently and
is not easily customizable.
I had to do the following:
For VIM->Skim.app (Skim.app is necessary for any of this to work), add
these commands to .vimrc:

::

    " Activate skimmap ,v :w<CR>:silent !/Applications/Skim.app/Contents/SharedSupport/displayline -r <C-r>=line('.')<CR> %<.pdf %<CR><CR>map ,p :w<CR>:silent !pdflatex -synctex=1 --interaction=nonstopmode %:p <CR>:silent !/Applications/Skim.app/Contents/SharedSupport/displayline -r <C-r>=line('.')<CR> %<.pdf %<CR><CR>map ,m :w<CR>:silent !make <CR>:silent !/Applications/Skim.app/Contents/SharedSupport/displayline -r <C-r>=line('.')<CR> %<.pdf %<CR><CR>" Reactivate VIMmap ,r :w<CR>:silent !/Applications/Skim.app/Contents/SharedSupport/displayline -r <C-r>=line('.')<CR> %<.pdf %<CR>:silent !osascript -e "tell application \"MacVim\" to activate" <CR><CR>map ,t :w<CR>:silent !pdflatex -synctex=1 --interaction=nonstopmode %:p <CR>:silent !/Applications/Skim.app/Contents/SharedSupport/displayline -r <C-r>=line('.')<CR> %<.pdf %<CR>:silent !osascript -e "tell application \"MacVim\" to activate" <CR><CR>

The ``,m`` command will reload the file and put your cursor where the
text is. ``,t`` will return VIM to the front afterwards.
Going the other way (reverse-search / inverse-search) was MUCH more
challenging. The code that does this is `on agpy`_. Reproduced here for
posterity (I hope to update the agpy version to `deal with tabs`_). [A
few hours later, I HAVE replaced the code. Below are the old applescript
version, then the new, vim-based version
``#!/bin/bashfile="$1"line="$2"[ "${file:0:1}" == "/" ] || file="${PWD}/$file"# Use Applescript to activate VIM, find file, and load it# the 'delay' command is needed to prevent command/control/shift from sticking when this# is activated (e.g., from Skim, where the command is command-shift-click)## key code 53 is "escape" to escape to command mode in VIMexec osascript \-e "delay 0.2" \-e "tell application \"MacVim\" to activate" \-e "tell application \"System Events\"" \-e "  tell process \"MacVim\"" \-e "    key code 53 "\-e "    keystroke \":set hidden\" & return " \-e "    keystroke \":if bufexists(bufname('$file'))\" & return " \-e "    keystroke \":exe \\\":buffer \\\" . bufnr(bufname('$file'))\"  & return " \-e "    keystroke \":else \" & return " \-e "    keystroke \":echo \\\"Could not load file\\\" \" & return " \-e "    keystroke \":endif\" & return " \-e "    keystroke \":$line\" & return " \-e "  end tell" \-e "end tell"``
New code: `download link`_

::

    #!/bin/bash# Install directions:# Put this file somewhere in your path and make it executable# To set up in Skim, go to Preferences:Sync# Change Preset: to Custom# Change Command: to macvim-load-line# Change Arguments: to "%file" %linefile="$1"line="$2"debug="$3"echo file: $fileecho line: $lineecho debug: $debugfor server in `mvim --serverlist` do    foundfile=`mvim --servername $server --remote-expr "WhichTab('$file')"`    if [[ $foundfile > 0 ]]    then        mvim --servername $server --remote-expr "foreground()"         if [[ $debug ]] ; then echo mvim --servername $server --remote-send ":exec \"tabnext $foundfile\" "; fi        mvim --servername $server --remote-send ":exec \"tabnext $foundfile\" "        if [[ $debug ]] ; then echo mvim --servername $server --remote-send ":$line "; fi        mvim --servername $server --remote-send ":$line "    fidone

Save that as an executable in your default path (e.g.,
``/usr/local/bin/macvim-load-line``) and open Skim.app, go to
Preferences:Sync and make the command look like this:

.. raw:: html

   <div class="separator" style="clear: both; text-align: center;">

`|image0|`_

.. raw:: html

   </div>

You need to have mvim on your path. mvim comes with MacVim.app, but is
NOT installed by default. Install it by doing something like:
`` cp /Users/adam/Downloads/MacVim-7_3-53/mvim /usr/local/bin/mvim ``
You'll also need to install WhichTab.vim in your ``~/.vim/plugins/``
directory. It's available `here`_ (`download link`_). Here's the source:

::

    function! WhichTab(filename)    " Try to determine whether file is open in any tab.      " Return number of tab it's open in    let buffername = bufname(a:filename)    if buffername == ""        return 0    endif    let buffernumber = bufnr(buffername)    " tabdo will loop through pages and leave you on the last one;    " this is to make sure we don't leave the current page    let currenttab = tabpagenr()    let tab_arr = []    tabdo let tab_arr += tabpagebuflist()    " return to current page    exec "tabnext ".currenttab    " Start checking tab numbers for matches    let i = 0    for tnum in tab_arr        let i += 1        echo "tnum: ".tnum." buff: ".buffernumber." i: ".i        if tnum == buffernumber            return i        endif    endforendfunctionfunction! WhichWindow(filename)    " Try to determine whether the file is open in any GVIM *window*    let serverlist = split(serverlist(),"\n")    "let currentserver = ????    for server in serverlist        let remotetabnum = remote_expr(server,             \"WhichTab('".a:filename."')")        if remotetabnum != 0            return server        endif    endforendfunction

.. raw:: html

   </p>

.. _macvim-skim-install.sh: http://agpy.googlecode.com/svn/trunk/macvim-skim/macvim-skim-install.sh
.. _agpy wiki page: http://code.google.com/p/agpy/wiki/macvimskim
.. _synctex: http://mactex-wiki.tug.org/wiki/index.php/SyncTeX
.. _on agpy: http://code.google.com/p/agpy/source/browse/trunk/macvim-skim/macvim-load-line
.. _deal with tabs: http://stackoverflow.com/questions/8839846/vim-check-if-a-file-is-open-in-current-tab-window
.. _download link: http://agpy.googlecode.com/svn/trunk/macvim-skim/macvim-load-line
.. _|image1|: http://3.bp.blogspot.com/-SbMLRTNSxug/Tw8_0saPQUI/AAAAAAAAGrc/9Ab8bgH8Ej0/s1600/Screen%2Bshot%2B2012-01-12%2Bat%2B1.17.09%2BPM.png
.. _here: http://code.google.com/p/agpy/source/browse/trunk/macvim-skim/WhichTab.vim
.. _download link: http://agpy.googlecode.com/svn/trunk/macvim-skim/WhichTab.vim

.. |image0| image:: http://3.bp.blogspot.com/-SbMLRTNSxug/Tw8_0saPQUI/AAAAAAAAGrc/9Ab8bgH8Ej0/s320/Screen%2Bshot%2B2012-01-12%2Bat%2B1.17.09%2BPM.png
.. |image1| image:: http://3.bp.blogspot.com/-SbMLRTNSxug/Tw8_0saPQUI/AAAAAAAAGrc/9Ab8bgH8Ej0/s320/Screen%2Bshot%2B2012-01-12%2Bat%2B1.17.09%2BPM.png
