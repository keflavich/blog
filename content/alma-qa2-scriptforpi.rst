ALMA QA2 restoration
####################
:date: 2015-10-02 09:00
:author: Adam (keflavich@gmail.com)
:tags: alma


In case you ever encounter this error about a missing `Source.xml` file::

    IOError: [Errno 2] No such file or directory: '/diskb/aginsbur/orion/2013.1.00546.S/science_goal.uid___A001_X122_X35c/group.uid___A001_X122_X35d/member.uid___A001_X122_X35e/calibrated/working/uid___A002_X960614_X39db.ms/Source.xml'
    WARNING: Failure executing file: <scriptForPI.py>

the solution is this ticket: https://help.almascience.org/index.php?/Knowledgebase/Article/View/266/5/what-should-i-do-if-scriptforpi-aborts-at-the-importasdm-step-with-error


So my solution::

    orion /diskb/aginsbur/atca master$ mv /diskb/aginsbur/casa/casapy-42.2.30986-pipe-1-64b/lib64/libxml2.so.2 /diskb/aginsbur/casa/casapy-42.2.30986-pipe-1-64b/lib64/origlibxml2.so.2
    orion /diskb/aginsbur/atca master$ locate libxml2.so.2
    /diskb/aginsbur/casa/casapy-42.2.30986-pipe-1-64b/lib64/libxml2.so.2
    /diskb/aginsbur/casa/casapy-42.2.30986-pipe-1-64b/lib64/libxml2.so.2.6.26
    /home/aginsbur/anaconda/lib/libxml2.so.2
    /home/aginsbur/anaconda/lib/libxml2.so.2.9.2
    /home/aginsbur/anaconda/pkgs/libxml2-2.9.2-0/lib/libxml2.so.2
    /home/aginsbur/anaconda/pkgs/libxml2-2.9.2-0/lib/libxml2.so.2.9.2
    /opt/anaconda/lib/libxml2.so.2
    /opt/anaconda/lib/libxml2.so.2.9.2
    /opt/anaconda/pkgs/libxml2-2.9.2-0/lib/libxml2.so.2
    /opt/anaconda/pkgs/libxml2-2.9.2-0/lib/libxml2.so.2.9.2
    /usr/lib64/libxml2.so.2
    /usr/lib64/libxml2.so.2.9.1
    orion /diskb/aginsbur/atca master$ ln -sf /usr/lib64/libxml2.so.2 /diskb/aginsbur/casa/casapy-42.2.30986-pipe-1-64b/lib64/libxml2.so.2
