CASA coordinate defaults
########################
:date: 2016-05-19 09:31
:author: Adam Ginsburg (Adam.G.Ginsburg@gmail.com)
:tags: CASA


A brief public service announcement: CASA coordinate strings follow a
convention of their own making that I at least find thoroughly
counterintuitive.  If you specify a sexagesimal coordinate, e.g. 05:12:15.3
-5:10:20.5 or something similar, CASA interprets that as 5 hours, -5 hours.
The declination is interpreted as being in hours.  Those are units no one has
ever used.  The CASA version requires the second half of the sexagesimal string
to be decimal separated::

    2016-05-19 00:45:13     WARN    SynthesisParams::stringToMDirection (file /var/rpmbuild/BUILD/casa-prerelease/casa-prerelease-4.6.0/code/synthesis/ImagerObjects/SynthesisUtilMethods.cc, line 786)     You provided the Declination/Latitude value "-28:23:29.22" which is understood to be in units of hours.
    2016-05-19 00:45:13     WARN    SynthesisParams::stringToMDirection (file /var/rpmbuild/BUILD/casa-prerelease/casa-prerelease-4.6.0/code/synthesis/ImagerObjects/SynthesisUtilMethods.cc, line 786)+    If you meant degrees, please replace ":" by ".".

This has broken my scripts more than a handful of times now, since copying &
pasting coordinates from any other program inevitably has the "wrong"
units.
