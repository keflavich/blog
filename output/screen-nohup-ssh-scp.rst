Screen, nohup, ssh, scp
#######################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, ssh, security, computer

I learned a lot about the above in the past day, but I didn't keep track
of the links.
First, screen is very useful: it allows you to run any task, detach the
screen, and let it run in the background. You can resume it later.
Example:
``screenipython run_fitter.py<ctrl-a> dscreen -r``
Second, it's a huge pain to type a password every time I use scp and
ssh. The solution is to make a key on your computer and put it in the
authorized\_keys file.
``ssh-keygen -t rsascp ~/.ssh/id_rsa ginsbura@milkyway.colorado.edu:.ssh ginsbura@milkyway.colorado.educat id_rsa >> ~/.ssh/authorized_keysssh -v ginsbura@milkyway.colorado.edu``
Use ssh -v to figure out why it fails if it still asks you for a
password. In one case, this happened because the computer I was using
expected the id to be in ~/.ssh/identity instead of ~/.ssh/id\_rsa.
There may also be permissions issues (i.e. you want restrictive
permissions on your ssh keys).
With the latter, you can still use nohup, which is helpful if you want
to pipe your output to a log file.
