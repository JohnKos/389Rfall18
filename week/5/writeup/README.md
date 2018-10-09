Writeup 5 - Binaries I
======

Name: John Kos
Section: 201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John Kos

## Assignment 5 Writeup

This week reminded me a lot of working with y86 in 216. It turns out a lot of the syntax is similar, and I think I remember working on these exact functions in that class so it was a matter of jogging my memory. I started with the simple set a counter to 0 and then do the expected problem. I realized this would fail for size 0 because I was using a do while loop. Because of this I instituted a check to see if a size 0 change was expected and if that was true I just jumped to the end of the function. A couple things were not the same as y86 for example I had to use a more correct jump fucntion to jump only under specific circumstances. While I had this in y86 it was a different function.

Between the two functions the only difference was having to dereference a pointer to get a char instead of just using the first one passed in. Sadly you can not use double brackets for the assignment function so I just used an tmp register.

Lastly while making I ran into the i386 issue so I had to re download Kali, push my work and then pull it from the new machine.

After running it on the new machine I realized that my string copy failed likely because I was copying to the wrong string. After some refactoring I started to get Hello Hello World!U for str copy and Hello zzzzz for memset. I realized that memset was missing the exclimation point and that was also tied into the problem for string copy. Both my strings did not end correctly because the origninal string was over written. To fix this I just had to grab a value of the exclimation point and then make sure to insert that at the end of the string.

