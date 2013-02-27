Awk sexagesimal to decimal conversion
#####################################
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, astronomy, computer

In VIM I often need to convert columns of RA/Dec from Sexagesimal into
Decimal format.
``%!awk '{ra = ($2+$3/60+$4/3600)*15; dec = $6+$7/60+$8/3600; print $1,"ra=",ra,",  dec=  ",$5,dec}'``
The far more irritating inverse operation:
`` %!awk '{h=($2/15); h=h-(h\%1);  m=($2-h*15)/15*60; m=m-(m\%1); s=($2-h*15-m*15/60)/15*3600; d=-($3-$3\%1); am=(-$3-d)*60; am=am-(am\%1); as=(-$3-d-am/60)*3600; printf "\%s  \%02i:\%02i:\%02.2f,  -\%02i:\%02i:\%02.2f   \%s  \%s  \%s\n" , $1,h,m,s,d,am,as,$4,$5,$6}'   ``
