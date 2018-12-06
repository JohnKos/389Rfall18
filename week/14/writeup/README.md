Writeup 10 - Crypto II
=====

Name: John Kos
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John Kos

## Assignment 10 Writeup

### Part 1 (70 Pts)

Looking around the website, I saw that there was no place for user input. So I started clicking around the website. After a while I noticed that there was an ID in the url of the product pages. I entered 1337 at the top because that was the cost of the first item and got the flag CMSC389R-{y0U-are_the_5ql_n!nja}. I entered the rest of the meme numbers and got nothing.

### Part 2 (30 Pts)

For the first I ran a simple alert by inputing <script>alert('display');</script>. This was exactly like the example in the slides.

For the Second I tried the method the same as the first, I guessed that maybe I could try using other html tags. I input 
<h1 color=<script>alert('test')</script>></h1> and this only returned alert('test');> so I knew that this did not break the input in the correct way to run the code. Upon looking at the source code, I noticed that we were already in a script tag that just loads all the info into html and displays it. The game's hints also mentioned on error and img. I tried <img src="/static/logos/level2.png" onerror="alert('test');">. This did not work and I figured it is because I loaded a file correctly so I inputed a random webaddress as well as put javascript: before alert to pull it out of the html. This worked.

This reminded me of the sql attack above, so I tried loading in random text to the top bar and got a frame of the frame. Tried to add an alert to the search bar by just typing onerror="alert('test');". it just returned a empty image, and I took this to mean that the src is pulled from the address bar. and that I should close the src if I want to append the error alert. The hints confirmed my beliefs by saying that I would need to use an HTML element and by also saying <script> would not work.
I typed an ' before my alert on error and it worked.

I tried entering an alert in the search bar similar to above. I kept getting '). After looking at the hints, it said I should use hex for the html, and because the semicolon was the part that was not showing up, I figured it would be for that part. Looking at the HTML I saw onload="startTimer('{{timer }}');". I figured I would have to build arround that. The hints also confirmed that. I entered ')%3b to close out the call. Then I input the alert('test')%3b to run the time and then lastly (' to close out the img tag.

Similar to last one, there is a link to {{ next }}. The search bar had next=confirm so I thought that this would be where I could enter the value. because it was in a tag, and didnt have onload or onerror I figured I would need to do similar to the second problem and have javascript: before the alert. I typed next=javascript:alert('test') and this worked.

looking at the source code, I can not load things with http. I tried to load multiple webpages with no luck. Looking at the fourth hint, I copied and pasted and added callback=alert. Noting that the regex did not look for upper case I just typed in Https://google.com/jsapi?callback=alert and this worked. 


