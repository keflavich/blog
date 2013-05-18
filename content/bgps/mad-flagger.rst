MAD flagger
###########
:date: 2008-11-19 04:50
:author: Adam (noreply@blogger.com)
:tags: googlepost, flagging
:slug: mad-flagger

.. raw:: html

   <p>

::

    ; The Mad Flagger; Flag based on the median average deviation within a spatial pixelfunction mad_flagger,data,inds,flags,nsig=nsig    t = systime(/sec)    f0 = total(where(flags))    if n_e(nsig) eq 0 then nsig = 3            newflags = flags    mx=max(inds)    vec3=fltarr(mx+1)    h=histogram(inds,reverse_indices=ri,OMIN=om)    for j=0L,n_elements(h)-1 do begin        if ri[j+1] gt ri[j] then begin            v_inds = [ri[ri[j]:ri[j+1]-1]]            if n_e(v_inds) gt 2 then begin                vec = data[v_inds];                vecmad = mad(vec)  ; the MAD is WAY too small!  I ended up rejecting 8% of points!                vecmad = stddev(vec)                vecmed = median(vec,/even)                madreject = where( (vec gt vecmed + nsig*vecmad) or (vec lt vecmed - nsig*vecmad) )                if (n_e(madreject) gt 0 and total(madreject)) gt 0 then begin                    reject_inds = v_inds[madreject]                    newflags[reject_inds] = 1                endif             endif        endif    endfor    print,"MAD flagger took ",strc(systime(/sec)-t)," seconds and flagged ",$        strc(round(total(where(newflags)) - f0)),' points'    return,newflagsend

.. raw:: html

   </p>

