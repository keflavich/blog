The extragalactic view of W51 at 220 and 290 GHz
################################################
:date: 2017-12-01 11:23 
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: w51, alma, synthetic extragalactic

These are APEX data covering 5.5' x 5.5' centered on W51 Main:
https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/RYEANM

W51 is at a distance of 5.1 kpc, so this field of view is equivalent to 8.1 pc, or 1.7" at
1 Mpc or 0.33" at 5 Mpc.

The linewidth is 12.7-15.2 km/s (H2CO 4-3, CO 2-1) FWHM averaged over this full field.


Images of the spectra, with some lines identified, are shown here (open them in
a new tab to see the full resolution).  The baselines aren't great, but it's
easy to fit a local linear baseline around any of the fairly narrow lines.

.. image:: |filename|/images/w51/lineid_avg_W51_12CO_merge.png
   :width: 200px

.. image:: |filename|/images/w51/lineid_avg_W51_217GHz_merge.png
   :width: 200px

.. image:: |filename|/images/w51/lineid_avg_W51_218GHz_merge.png
   :width: 200px

.. image:: |filename|/images/w51/lineid_avg_W51_232GHz_merge.png
   :width: 200px

.. image:: |filename|/images/w51/lineid_avg_W51_291GHz_merge.png
   :width: 200px

.. image:: |filename|/images/w51/lineid_avg_W51_293GHz_merge.png
   :width: 200px

Scripts to obtain the data and process them are here:
https://github.com/keflavich/W51_APEX_H2CO

See the related project by Watanabe et al looking at W51 in the 3mm band:
http://adsabs.harvard.edu/abs/2017ApJ...845..116W
