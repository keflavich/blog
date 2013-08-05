Splatalogue Queries I need to save and automate
===============================================
:author: Adam Ginsburg
:date: 2013-08-05 10:37:59

(work in progress)

http://www.cv.nrao.edu/php/splat/c.php?submit=submit&sid[]=194&sid[]=324&sid[]=109&sid[]=155&from=1&to=18&frequency_units=GHz&energy_range_to=5&energy_range_type=eu_K

.. code-block:: python

    import requests
    import copy

    default_payload = {
        'no_atmospheric':'no_atmospheric',
        'no_potential':'no_potential',
        'no_probable':'no_probable',
        'displayLovas':'displayLovas',
        'displaySLAIM':'displaySLAIM',
        'displayJPL':'displayJPL',
        'displayCDMS':'displayCDMS',
        'displayToyaMA':'displayToyaMA',
        'displayOSU':'displayOSU',
        'displayRecomb':'displayRecomb',
        'displayLisa':'displayLisa',
        'displayRFI':'displayRFI',
        'submit':'Search',
        'data_version':'v2.0',
        'lill':'on',
        'chemical_name':'',
        'calcIn':'',
        'tran':'',
        'energy_range_from':'',
        'energy_range_to':'',
        'energy_range_type':'',
        }


    url = 'http://www.cv.nrao.edu/php/splat/c.php'
    payload = copy.copy(default_payload)
    payload={'sid[]':[194,324,155,109],
             'from':'1','to':'18','frequency_units':'GHz','energy_range_from':'','energy_range_to':'50','energy_range_type':'eu_K',
             'el2':'el2', 'el4':'el4', 'ls1':'ls1', 'ls5':'ls5', }
    response = requests.post(url,data=payload)

Unfortunately, this doesn't work completely: the returned page does not filter based on upper energy level state.

http://www.cv.nrao.edu/php/splat/c.php?energy_range_to=50&displaySLAIM=displaySLAIM&sid%5B%5D=194&sid%5B%5D=324&sid%5B%5D=155&sid%5B%5D=109&displayLovas=displayLovas&ls5=ls5&energy_range_from=0&frequency_units=GHz&no_probable=no_probable&ls1=ls1&energy_range_type=eu_K&displayOSU=displayOSU&no_atmospheric=no_atmospheric&from=1&no_potential=no_potential&data_version=v2.0&displayToyaMA=displayToyaMA&submit=submit&displayLisa=displayLisa&to=18&displayJPL=displayJPL&el2=el2&displayCDMS=displayCDMS&displayRecomb=displayRecomb&el4=el4&displayRFI=displayRFI&lill=on&calcIn=&chemical_name=&tran=
