Determing ALMA Array Configurations
###################################
:date: 2021-04-27 08:51
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: alma

ALMA's named array configurations are not accessible through CASA.
They are available from https://almascience.eso.org/observing/observing-configuration-schedule/prior-cycle-observing-and-configuration-schedule

This snippet will let you grab the tables and create a mapping from date to array config name.

However, it's a HUGE waste of time, because these data are stored directly in the MS!

This is the right way:

.. code:: python

   tb.open(vis+'/ASDM_EXECBLOCK')
   tb.getcol('configName')
   # array(['C43-3'], dtype='<U16')


This is the hacky, reconstructed from the website, bad way:

.. code:: python

   import requests
   from bs4 import BeautifulSoup
   from astropy.table import Table, vstack
   from astropy.io import ascii
   from astropy.time import Time

   url = "https://almascience.eso.org/observing/observing-configuration-schedule/prior-cycle-observing-and-configuration-schedule"

   response = requests.get(url)
   response.raise_for_status()
   soup = BeautifulSoup(response.text)
   tables = soup.findAll('table', class_="grid listing")

   def clean_lines(soup, badrows=['Long Baseline Campaign',
                                  'February Maintenance Period',
                                  'End of Cycle',
                                  'Engineering/Software',
                                  'Engineering/Software Time',
                                      ]):
       for tr in soup('tr'):
           if any(bad in str(tr) for bad in badrows):
                _=tr.extract()
       return soup

   tables = soup.findAll('table', class_="grid listing")
   tables = [ascii.read(str(clean_lines(tbl)), format='html') for tbl in tables]
   tables[3] = tables[3][:-1]
   tables[3]['Block'] = tables[3]['Block'].astype('int')
   tables[4]['maximumrecoverablescale2(")'] = tables[4]['maximumrecoverablescale2(")'].astype('str')

   stacked = vstack(tables)
   start_times = Time(stacked['Start date'])
   end_times = Time(stacked['End date'])


Then, say you have a list of measurement sets ``mses``, you can look up the
array configuration for each date and field.  The choice of ``fields[0]`` here
only makes sense if your data had a single target; it's a bad choice if there
are multiple targets in a scheduling block:

.. code:: python

   import json
   from casatools import msmetadata
   msmd = msmetadata()

   results = {}

   for vis in mses:
       msmd.open(mses)
       obstime = Time(msmd.timerangeforobs(0)['begin']['m0']['value'], format='mjd')
       fieldnames = np.array(msmd.fieldnames())
       fields = np.unique(fieldnames[msmd.fieldsforintent('OBSERVE_TARGET#ON_SOURCE')])
       msmd.close()

       array_config = stacked[(obstime > start_times) & (obstime < end_times)]['Approx\xa0Config.']
       if fields[0] in results:
           results[fields[0]][obstime.strftime('%Y-%m-%d')] = array_config[0]
       else:
           results[fields[0]] = {obstime.strftime('%Y-%m-%d'): array_config[0]}

   with open('array_configurations.json', 'w') as fh:
       json.dump(results, fh)
