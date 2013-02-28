BASH discoveries, readline questions
####################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, bash, python, unix, computer

1. `` shopt -p ``
Maybe my hostname completion worked and then stopped working because the
bash option hostcomplete was not set. Duh! Why? I don't know. Anyway,
`` shopt -s hostcomplete`` solves the problem.
`` nocaseglob `` is also pretty cool (case insensitive tab completion)
2. it's really hard to search for readline stuff on google. Can anyone
explain to me how BASH readline works? I would REALLY like to make bash
readline work like ipython, in which you can start typing a command and
hit the 'up' key to search through the history for anything beginning
with the stuff you've typed up to that point. But I can't even find
documentation for the ipython readline! Any hints, anyone?
3. my desktop at work blocks ssh connections. I can ssh into some
computers and then into it, but not directly into it.
...as usual, I made a list where not-a-list would have sufficed, and I
had to add the last thing because a 2-item list is dumb.
