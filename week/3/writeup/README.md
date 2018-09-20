Writeup 3 - OSINT II, OpSec and RE
======

Name: John Kos	
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John Kos
## Assignment 3 Writeup

### Part 1 (100 pts)
Suggestion 1: Week Passwords
First a password such as pokemon is extremely weak because it exists in the rock you password list, and similarly having it be named after a popular hobby that the account owner was a fan of is also extremely incriminating. To prevent hacking, the passwords should be a random assortment of at least 16 letters, number and characters. A password of that length has 
47672402000000000000000000000 (62^16) different combinations. This effectively makes a brute force attack infeasible. Having users use a precreated password or even phrase could do wonders for improving security. The time to crack a 10 digit password of high complexity(all characters possible) is one month. Data from here https://blog.preempt.com/weak-passwords. Having 6 possible character posistions increased the time exponentially.

Suggestion 2: Keep admin IP private
Having the admin page display the admin port was dangerous because even offering that information made the hackers job a lot easier. With out that information the would have to do an attack on the websites IP with way less information in hopes that it would give enough info, or lead to somewhere with more. The exposed IP data was part of a webpage that was not created yet and therefore did not need to be displayed. Secondly, if you want users to access administrative information you could use the website to do it in a way that is filtered and less subject to other types of hacks such SQL injection. For that reason it is smarter to just not have the admin page at all unless it is completely necessary. One could additionally keep changing the IP to make the database harder to hack. Forcing IP changes can be done with servers. https://thebestvpn.com/hide-ip

Suggestion 3: Close Unused ports
Having the open ports that were open to Nmap scanning is was another thing that lead to the company being hacked. It would be smart to close all ports unless completely necessary. And if ports need to be open, make sure that they are protected with proper passwords. As well, it is easy to see when someone is Nmap scanning your site, so it may be useful to block any connection that may be coming from the computer as well as blocking people that are trying to login multiple times in quick succession. This would at the very least slow down a hacker enough to make hacking unfeasible and at the very most discourage him completely.
