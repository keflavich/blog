Broken rotation
###############
:date: 2008-09-09 01:34
:author: Adam (adam.g.ginsburg@gmail.com)
:tags: googlepost, mapping
:slug: broken-rotation

I have to echo James in saying how remarkable it is than anything I ever
did worked at all! I'm growing more and more certain that I've been
double-correcting rotation for the past 2 months, and my maps don't look
all that bad!
.. image:: http://4.bp.blogspot.com/_lsgW26mWZnU/SMW4oOPcLaI/AAAAAAAADXw/1ARG8iyVXDQ/s400/070717_o15_rotations.png
Image caption:
Top left - both PA and rotang
Top right - neither
Bottom left - rotang only
Bottom right - PA only
I'm running the same sort of comparison on all of the GC and L=24 data.
Check out /scratch/adam\_work/ROT\_TEST for the results. I'll be
updating this when I've completed that analysis.
Update 6:35 PM: !@#$, etc. New problem child:
.. image:: http://1.bp.blogspot.com/_lsgW26mWZnU/SMXFUjLjRGI/AAAAAAAADX4/aynvuycRzGM/s400/060603_o16_rotations.png
Image caption (same as above, luckily):
Top left - both PA and rotang
Top right - neither
Bottom left - rotang only
Bottom right - PA only
So, can anyone tell me which one of THESE is right? Because I can't. Top
left is 'correct' except that it's not.
Update 7:10 PM: I compared adding/subtracting PA and RA, and I can say
this: subtracting PA never works. Adding/subtracting RA works variably.
I think I'm done testing parameter space. I haven't had very good luck
doing parameter space tests in the past; it usually is more beneficial
to take a step back and try to think through the problem.
Update 7:30 PM: Fixed. Much as this looks like a short-lived, easily
solved problem, it was one of the most subtle and insidious errors I've
made. I got extremely lucky that plotting PA and ROTANGLE happened to
spark off warning sirens in my mind about the positioning of the
variable names. I wouldn't normally look for that.

.. _|image2|: http://4.bp.blogspot.com/_lsgW26mWZnU/SMW4oOPcLaI/AAAAAAAADXw/1ARG8iyVXDQ/s1600-h/070717_o15_rotations.png
.. _|image3|: http://1.bp.blogspot.com/_lsgW26mWZnU/SMXFUjLjRGI/AAAAAAAADX4/aynvuycRzGM/s1600-h/060603_o16_rotations.png

