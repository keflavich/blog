Montage wrapper
###############
:date: 2012-09-20 20:02
:author: Adam (keflavich@gmail.com)
:tags: googlepost, code

(I'm going to try to gradually shift my blogging to this one...)
I wrote a bash wrapper for Tom Robitaille's montage wrapper to allow
fits wildcards.
``#!/bin/bashorigdir=`pwd`#echo $# $*if [ $# -gt 0 ]then    for ii in $*    do        if [ ${ii%=*} == 'header' ]        then            /usr/local/bin/montage/mGetHdr ${ii#*=} mosaic.hdr        elif [ ${ii%=*} == 'outfile' ]        then            outfile=${ii#*=}        elif [ `echo $ii | grep =` ]         then            params="$params,${ii%=*}='${ii#*=}'"        elif [ `echo $ii | grep ".fits"` ]         then            files=( ${files[@]} $ii )        fi    donefiecho ${files[@]} ${#files} if [ ${#files} -gt 0 ] then    mkdir tmp    cp ${files[@]} tmp/    cp mosaic.hdr tmp/    cd tmp/fiif [ -f mosaic.hdr ] then     echo "mosaic.hdr exists, continuing"    dir=`pwd`    echo python -c "import montage; montage.wrappers.mosaic('$dir','$dir/mosaic',header='$dir/mosaic.hdr'$params)"    python -c "import montage; montage.wrappers.mosaic('$dir','$dir/mosaic',header='$dir/mosaic.hdr'$params)"    cd $origdir    if [ -d tmp ]    then        if [ $outfile ]        then            mv tmp/mosaic/mosaic.fits $outfile        else            mv tmp/mosaic mosaic        fi        rm -r tmp    fielse    echo "mosaic.hdr does not exist.  Quitting."    cd $origdirfi``
