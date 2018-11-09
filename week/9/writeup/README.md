Writeup 9 - Crypto I
=====

Name: John Kos
Section: 0201

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John Kos

## Assignment 9 Writeup

### Part 1 (60 Pts)
I began by passing all the hashes and words into an array for quick access later. I used a loop to add salt to the word and then compare it to the array of hashes by using the hashlib function passing in sha256 as a parameter. This was not working so I was wondering if the newline character was messing it up, after noticing that was not the issue (by using a function to cut it off) I realized we had to use sha512, so I passed that in a parameter. It still was not working, so then I realized that maybe if I used the shorter way to run the function in the library this might alleviate any issue I may have accidently coded in. After alternating cutting off the new line character on the hashes and the passwords it finally worked when I left in both.

salt: k   word: neptune

salt: m   word: jordan 

salt: p   word: pizza

salt: u   word: loveyou



### Part 2 (40 Pts)
CMSC389R-{H4sh-5l!ngInG-h@sH3r}

For my script, I thought it would be smart to just grab the individual posistions of the value to be hashed and the function. To do this I nced the server and tried to figure out their place in an array if the string was split by spaces. I miscounted because I did not include the welcome message, and then I also realized that because the welcome message only displays once, I would have to grab different positions on the array a second time. Because the hashlib function I tried to use at first took in a string as a parameter to decide the hash function I just passed that in. Next I updated it with the value I grabbed and then hashed it. It worked suprisingly well and I got the flag. I also looked at my old socket project and saw I had to include a new line character for it to work.

