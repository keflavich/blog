Gildas CLASS
############
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: http://schemas.google.com/blogger/2008/kind#post, class

It's absurdly difficult to find help on GILDAS Class, probably because
you can't google "class" and most people probably don't label every
piece of code with "GILDAS class".
Anyway, here are some scripts that I refer back to often:
``file in August2009BGPS.datfile out August2009fits.dat multipleon error "file out August2009fits.dat"say "READ IN FILES"define character sourcelist*10[300]accept sourcelist /column observed_sources.txton error "continue"get 1001set window -100 160set mask -400 -100 160 400set mode x -400 400set align velocityfor i 1 to 161    say "Working on SOURCE "'i'    find /source 'sourcelist[i]' /telescope "CSO 4GHZ IF1" /offset 0 0 /quality 5    average    on error "@avplot2 'sourcelist[i]' 'i'; next"    base 3    line 0    min    plot    vis    write i!    on error "continue"next``
and
``file in araya-2004.clsfinddefine character filename*20for i 1 to 20     say "Working on source "'i'    get next    let filename "araya-2004_"'i'".fits"     say "fits write "'filename'" /mode spectrum"    fits write 'filename' /mode spectrumnext!file in araya-2002.cls!find!define character filename*20!for i 1 to 42 !    say "Working on source "'i'!    get i!    let filename "araya-2002_"'i'".fits" !    say "fits write "'filename'" /mode spectrum"!    fits write 'filename' /mode spectrum!next``
