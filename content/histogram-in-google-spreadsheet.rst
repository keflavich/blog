Histogram in Google Spreadsheet
###############################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, spreadsheet

It's not easy to make a histogram in google spreadsheets without
replicating data. The "countif" function would be great, except it only
allows very simple criteria. However, there's a workaround:
=count(Filter('Grades'!V2:V30,'Grades'!V2:V30>0.9))
=count(Filter('Grades'!V2:V30,'Grades'!V2:V30<0.9,'Grades'!V2:V30>0.8))
The Filter() function returns an array, which can be operated on like
any other set of cells.
It's still not easy to make a nice-looking histogram, but the output of
this process is at least usable.
