My favorite Splatalogue queries
===============================
:author: Adam Ginsburg
:date: 2013-08-05 10:37:59

I tend to be most interested in low-energy molecular lines: CO, |NH3|, and
|H2CO| being the main candidates.

Note: Splatalogue has made some recent changes to their returned tables, partly
per my recommendations.  The code below has been update to reflect these
changes.

.. code-block:: python

    >>> from astropy import units as u
    >>> from astroquery.splatalogue import Splatalogue
    >>> S = Splatalogue(energy_max=500,
    ...    energy_type='eu_k',energy_levels=['el4'],
    ...    line_strengths=['ls4'],
    ...    only_NRAO_recommended=True,noHFS=True)
    >>> def trimmed_query(*args,**kwargs):
    ...     columns = ('Species','Chemical Name','Resolved QNs','Freq-GHz',
    ...                'Meas Freq-GHz','Log<sub>10</sub> (A<sub>ij</sub>)',
    ...                'E_U (K)')
    ...     table = S.query_lines(*args, **kwargs)[columns]
    ...     table.rename_column('Log<sub>10</sub> (A<sub>ij</sub>)','log10(Aij)')
    ...     table.rename_column('E_U (K)','EU_K')
    ...     table.rename_column('Resolved QNs','QNs')
    ...     table.sort('EU_K')
    ...     return table
    >>> trimmed_query(1*u.GHz,30*u.GHz, 
    ...     chemical_name='(H2.*Formaldehyde)|( HDCO )',
    ...     energy_max=50).pprint()
    Species Chemical Name      QNs      Freq-GHz Meas Freq-GHz log10(Aij)   EU_K
    ------- ------------- ------------- -------- ------------- ---------- --------
       HDCO  Formaldehyde 1(1,0)-1(1,1)       --       5.34614   -8.31616 11.18287
     H2C18O  Formaldehyde 1(1,0)-1(1,1)   4.3888        4.3888   -8.22052 15.30187
     H213CO  Formaldehyde 1(1,0)-1(1,1)       --       4.59309   -8.51332 15.34693
       H2CO  Formaldehyde 1(1,0)-1(1,1)  4.82966            --   -8.44801 15.39497
       HDCO  Formaldehyde 2(1,1)-2(1,2)       --      16.03787   -7.36194 17.62746
     H2C18O  Formaldehyde 2(1,1)-2(1,2) 13.16596      13.16596   -6.86839 22.17455
     H213CO  Formaldehyde 2(1,1)-2(1,2)       --       13.7788   -7.55919 22.38424
       H2CO  Formaldehyde 2(1,1)-2(1,2) 14.48848            --   -7.49383 22.61771
     H2C18O  Formaldehyde 3(1,2)-3(1,3) 26.33012      26.33014   -6.03008 32.48204
     H213CO  Formaldehyde 3(1,2)-3(1,3)       --      27.55567   -6.95712  32.9381
       H2CO  Formaldehyde 3(1,2)-3(1,3)       --       28.9748   -6.89179 33.44949
    
    
    >>> trimmed_query(100*u.GHz,400*u.GHz,
    ...     chemical_name='Carbon Monoxide',
    ...     energy_max=50).pprint()
    Species  Chemical Name   QNs   Freq-GHz Meas Freq-GHz log10(Aij)   EU_K
    ------- --------------- ----- --------- ------------- ---------- --------
       C18O Carbon Monoxide   1-0 109.78218     109.78218   -7.20058  5.26868
    13COv=0 Carbon Monoxide   1-0 110.20135            --   -7.49946   5.2888
       C17O Carbon Monoxide J=1-0 112.35928     112.35928   -7.17404  5.39236
      COv=0 Carbon Monoxide   1-0  115.2712      115.2712   -7.14236  5.53211
       C18O Carbon Monoxide   2-1 219.56036     219.56036   -6.21833 15.80595
    13COv=0 Carbon Monoxide   2-1 220.39868            --   -6.51752 15.86618
       C17O Carbon Monoxide J=2-1 224.71437     224.71439   -6.19179 16.17703
      COv=0 Carbon Monoxide   2-1   230.538       230.538   -6.16011 16.59608
       C18O Carbon Monoxide   3-2 329.33055     329.33055   -5.66014  31.6116
    13COv=0 Carbon Monoxide   3-2 330.58797            --   -5.95976 31.73179
       C17O Carbon Monoxide J=3-2  337.0611     337.06113    -5.6336  32.3538
      COv=0 Carbon Monoxide   3-2 345.79599     345.79599   -5.60192 33.19169
    
    >>> trimmed_query(1*u.MHz,2*u.GHz,
    ...     chemical_name=' H2CO .*Formaldehyde',energy_max=75,
    ...     energy_type='eu_k').pprint()
    Species Chemical Name      QNs      Freq-GHz Meas Freq-GHz log10(Aij)   EU_K
    ------- ------------- ------------- -------- ------------- ---------- --------
       H2CO  Formaldehyde 2(2,0)-2(2,1)       --       0.07114  -13.81846   57.612
       H2CO  Formaldehyde 3(2,1)-3(2,2)       --       0.35557  -12.02319 68.11082
        
           
    >>> trimmed_query(20*u.MHz,25*u.GHz,chemical_name=' NH3 ').pprint()
    Species Chemical Name      QNs       Freq-GHz Meas Freq-GHz log10(Aij)    EU_K
    ------- ------------- -------------- -------- ------------- ---------- ---------
     NH3v=0       Ammonia  1(1)0a-1(1)0s 23.69447       23.6945   -6.43769  24.40492
     NH3v=0       Ammonia  2(2)0a-2(2)0s  23.7226      23.72263   -6.31125   65.5867
     NH3v=0       Ammonia  2(1)0a-2(1)0s 23.09885      23.09881   -6.94808   81.5904
     NH3v=0       Ammonia 3(3)0a-3(-3)0s 23.87008      23.87013   -6.25203 124.68113
     NH3v=0       Ammonia  3(2)0a-3(2)0s 22.83422      22.83418     -6.662 151.33353
     NH3v=0       Ammonia  3(1)0a-3(1)0s 22.23456       22.2345   -7.29889 167.29666
     NH3v=0       Ammonia  4(4)0a-4(4)0s 24.13935      24.13942   -6.20938 201.67106
     NH3v=0       Ammonia 4(3)0a-4(-3)0s 22.68835      22.68831   -6.54002 238.96192
     NH3v=0       Ammonia  4(2)0a-4(2)0s 21.70341      21.70336   -6.95001 265.52612
     NH3v=0       Ammonia  4(1)0a-4(1)0s 21.13434      21.13431   -7.58659 281.43749
     NH3v=0       Ammonia  5(5)0a-5(5)0s 24.53292      24.53299    -6.1706 296.53357
     NH3v=0       Ammonia  5(4)0a-5(4)0s 22.65307      22.65302   -6.46829 344.46226
     NH3v=0       Ammonia 5(3)0a-5(-3)0s 21.28532      21.28528   -6.79928  381.6003
     NH3v=0       Ammonia  5(2)0a-5(2)0s 20.37145      20.37145   -7.20859 408.05568
     NH3v=0       Ammonia  5(1)0a-5(1)0s 19.83833      19.83835   -7.84539 423.90259
     NH3v=0       Ammonia  6(5)0a-6(5)0s 22.73249      22.73243   -6.41603 467.80451
        
           

.. |NH3| replace:: NH\ :sub:`3`
.. |H2CO| replace:: H\ :sub:`2`\ CO
