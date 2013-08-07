My favorite Splatalogue queries
===============================
:author: Adam Ginsburg
:date: 2013-08-05 10:37:59

I tend to be most interested in low-energy molecular lines: CO, |NH3|, and
|H2CO| being the main candidates.

.. code-block:: python

    >>> from astropy import units as u
    >>> from astroquery.splatalogue import Splatalogue
    >>> Splatalogue.query_lines(1*u.GHz,30*u.GHz,chemical_name='(H2.*Formaldehyde)|( HDCO )',energy_max=50,energy_type='eu_k',only_NRAO_recommended=True,noHFS=True).pprint()
    Species Chemical Name Freq-GHz Freq Err Meas Freq-GHz ... E<sub>L</sub> (K) E<sub>U</sub> (cm<sup>-1</sup>) E<sub>U</sub> (K) Linelist
    ------- ------------- -------- -------- ------------- ... ----------------- ------------------------------- ----------------- --------
     H2C18O  Formaldehyde   4.3888      0.0        4.3888 ...          15.09124                        10.63539          15.30187    SLAIM
     H213CO  Formaldehyde       --       --       4.59309 ...          15.12649                        10.66671          15.34693     CDMS
       H2CO  Formaldehyde  4.82966      0.0            -- ...          15.16318                         10.7001          15.39497     CDMS
       HDCO  Formaldehyde       --       --       5.34614 ...           10.9263                         7.77253          11.18287     CDMS
     H2C18O  Formaldehyde 13.16596      0.0      13.16596 ...          21.54268                        15.41217          22.17455    SLAIM
     H213CO  Formaldehyde       --       --       13.7788 ...          21.72296                        15.55791          22.38424     CDMS
       H2CO  Formaldehyde 14.48848      0.0            -- ...          21.92237                        15.72018          22.61771     CDMS
       HDCO  Formaldehyde       --       --      16.03787 ...          16.85776                        12.25177          17.62746     CDMS
     H2C18O  Formaldehyde 26.33012    1e-06      26.33014 ...           31.2184                        22.57628          32.48204    SLAIM
     H213CO  Formaldehyde       --       --      27.55567 ...          31.61565                        22.89326           32.9381     CDMS
       H2CO  Formaldehyde       --       --       28.9748 ...          32.05893                         23.2487          33.44949     CDMS

    >>> Splatalogue.query_lines(100*u.GHz,400*u.GHz,chemical_name='Carbon Monoxide',energy_max=50,energy_type='eu_k',only_NRAO_recommended=True,noHFS=True).pprint()
    Species  Chemical Name   Freq-GHz Freq Err Meas Freq-GHz ... E<sub>L</sub> (K) E<sub>U</sub> (cm<sup>-1</sup>) E<sub>U</sub> (K) Linelist
    ------- --------------- --------- -------- ------------- ... ----------------- ------------------------------- ----------------- --------
       C18O Carbon Monoxide 109.78218      0.0     109.78218 ...               0.0                         3.66194           5.26868    SLAIM
    13COv=0 Carbon Monoxide 110.20135      0.0            -- ...               0.0                         3.67592            5.2888     CDMS
       C17O Carbon Monoxide 112.35928    4e-06     112.35928 ...               0.0                          3.7479           5.39236    SLAIM
      COv=0 Carbon Monoxide  115.2712      0.0      115.2712 ...               0.0                         3.84503           5.53211    SLAIM
       C18O Carbon Monoxide 219.56036      0.0     219.56036 ...           5.26877                        10.98575          15.80595    SLAIM
    13COv=0 Carbon Monoxide 220.39868    1e-07            -- ...           5.28877                        11.02761          15.86618     CDMS
       C17O Carbon Monoxide 224.71437    9e-06     224.71439 ...            5.3925                        11.24366          16.17703    SLAIM
      COv=0 Carbon Monoxide   230.538      0.0       230.538 ...           5.53207                        11.53492          16.59608    SLAIM
       C18O Carbon Monoxide 329.33055    1e-06     329.33055 ...          15.80631                        21.97128           31.6116    SLAIM
    13COv=0 Carbon Monoxide 330.58797    1e-07            -- ...          15.86617                        22.05483          31.73179     CDMS
       C17O Carbon Monoxide  337.0611  1.2e-05     337.06113 ...          16.17751                        22.48715           32.3538    SLAIM
      COv=0 Carbon Monoxide 345.79599      0.0     345.79599 ...           16.5962                        23.06951          33.19169    SLAIM

    >>> Splatalogue.query_lines(1*u.MHz,2*u.GHz,chemical_name=' H2CO .*Formaldehyde',energy_max=75,energy_type='eu_k',energy_levels=['el2','el4'],line_strengths=['ls3','ls4'],only_NRAO_recommended=True).pprint()
    Species Chemical Name Freq-GHz Freq Err Meas Freq-GHz ... S<sub>ij</sub> Log<sub>10</sub> (A<sub>ij</sub>) E<sub>L</sub> (K) E<sub>U</sub> (K) Linelist
    ------- ------------- -------- -------- ------------- ... -------------- --------------------------------- ----------------- ----------------- --------
       H2CO  Formaldehyde       --       --       0.07114 ...          3.335                         -13.81846          57.60858            57.612     CDMS
       H2CO  Formaldehyde       --       --       0.35557 ...          2.334                         -12.02319          68.09376          68.11082     CDMS
           
    >>> result = Splatalogue.query_lines(1*u.MHz,2*u.GHz,chemical_name=' H2CO .*Formaldehyde',energy_max=75,energy_type='eu_k',energy_levels=['el2','el4'],line_strengths=['ls3','ls4'],only_NRAO_recommended=True)
    >>> result.remove_columns(('Linelist','S<sub>ij</sub>','Meas Freq Err','Freq Err','Freq-GHz')
    >>> result.pprint()
    Species Chemical Name Meas Freq-GHz Resolved<br>QNs Log<sub>10</sub> (A<sub>ij</sub>) E<sub>L</sub> (K) E<sub>U</sub> (K)
    ------- ------------- ------------- --------------- --------------------------------- ----------------- -----------------
       H2CO  Formaldehyde       0.07114   2(2,0)-2(2,1)                         -13.81846          57.60858            57.612
       H2CO  Formaldehyde       0.35557   3(2,1)-3(2,2)                         -12.02319          68.09376          68.11082
       

    >>> result = Splatalogue.query_lines(20*u.MHz,25*u.GHz,chemical_name=' NH3 ',energy_max=500,energy_type='eu_k',energy_levels=['el2','el4'],line_strengths=['ls3','ls4'],only_NRAO_recommended=True)['Species','Chemical Name','Resolved<br>QNs','Freq-GHz','Log<sub>10</sub> (A<sub>ij</sub>)','E<sub>U</sub> (K)']
    >>> result.sort('E<sub>U</sub> (K)')
    >>> result.pprint()Species Chemical Name Resolved<br>QNs Freq-GHz Log<sub>10</sub> (A<sub>ij</sub>) E<sub>U</sub> (K)
    ------- ------------- --------------- -------- --------------------------------- -----------------
     NH3v=0       Ammonia   1(1)0a-1(1)0s 23.69447                          -6.43769          24.40492
     NH3v=0       Ammonia   2(2)0a-2(2)0s  23.7226                          -6.31125           65.5867
     NH3v=0       Ammonia   2(1)0a-2(1)0s 23.09885                          -6.94808           81.5904
     NH3v=0       Ammonia  3(3)0a-3(-3)0s 23.87008                          -6.25203         124.68113
     NH3v=0       Ammonia   3(2)0a-3(2)0s 22.83422                            -6.662         151.33353
     NH3v=0       Ammonia   3(1)0a-3(1)0s 22.23456                          -7.29889         167.29666
     NH3v=0       Ammonia   4(4)0a-4(4)0s 24.13935                          -6.20938         201.67106
     NH3v=0       Ammonia  4(3)0a-4(-3)0s 22.68835                          -6.54002         238.96192
     NH3v=0       Ammonia   4(2)0a-4(2)0s 21.70341                          -6.95001         265.52612
     NH3v=0       Ammonia   4(1)0a-4(1)0s 21.13434                          -7.58659         281.43749
     NH3v=0       Ammonia   5(5)0a-5(5)0s 24.53292                           -6.1706         296.53357
     NH3v=0       Ammonia   5(4)0a-5(4)0s 22.65307                          -6.46829         344.46226
     NH3v=0       Ammonia  5(3)0a-5(-3)0s 21.28532                          -6.79928          381.6003
     NH3v=0       Ammonia   5(2)0a-5(2)0s 20.37145                          -7.20859         408.05568
     NH3v=0       Ammonia   5(1)0a-5(1)0s 19.83833                          -7.84539         423.90259
     NH3v=0       Ammonia   6(5)0a-6(5)0s 22.73249                          -6.41603         467.80451
           

.. |NH3| replace:: NH\ :sub:`3`
.. |H2CO| replace:: H\ :sub:`2`\ CO
