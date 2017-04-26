A quick performance test on CASA cleaning
#########################################
:date: 2017-04-26 11:03 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA, clean, tclean

I ran some speed tests to compare CASA's speed when imaging single channels vs
blocks of channels.  The tests were run with savemodel='none' on a lustre node ::

    'speedtest_nchan1_concat': 249,
    'speedtest_nchan1_individual': 523,
    'speedtest_nchan5_concat': 803,
    'speedtest_nchan5_individual': 916,
    'speedtest_nchan20_concat': 2303,
    'speedtest_nchan20_individual': 2346,
    'speedtest_nchan40_concat': 4010,
    'speedtest_nchan40_individual': 4136,
    'speedtest_nchan80_concat': 8101,
    'speedtest_nchan80_individual': 9298,


.. image:: |filename|/images/casa/cube_performance.png
   :width: 600px

The fit is y = 98x + 237

So at least until swapping happens, there is no serious advantage or
disadvantage to running a different # of channels simultaneously.
