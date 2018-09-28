Writeup 3 - Pentesting I
======

Name: John Kos
Section: 0201

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John Kos

## Assignment 4 Writeup

### Part 1 (45 pts)
I typed in the command to get to Fred's new uptime system, and was presented with a request for an IP address. I thought about the two I found during the Osint Week and considered using the admin one right away. I was having trouble figuring out how to get into the file system so I tried running an nmap and then looked up how the nc command works. I found out that the 45 refers to port number I so I tried the nc command onto the open port abyss. got flag {p1ng_as_a_@serv1c3}. This is not what we were shown in class so I wonder if I am doing things correctly. opened logs and tried to cat a pcap file and seemed to have broken the system. I think these files are records of people that tried to log in to the admin system. Their commands are covered so I cannot see if I am doing the right thing. Found the {th@t-hack-w@s-sh0ck1ing} flag. Found the command curl -H "user-agent: () { :; }; echo; echo; /bin/bash -c 'cat /etc/passwd;'" https://your-ip:8080/cgi-bin/stats. going to try this command on the cornerstone airlines IP. No luck. I think I got the right flag earlier with nc cornerstoneairlines 9999. This brought up the entire back end of the uptime system. I think the script being used by the runtime system is called container_startup.sh. looking through startup.sh he could have closed port 9999.cd . I continued looking around the file system and saw a folder for josh. upon looking more and seeing a folder named git_grades I thought it would be a good idea to report it to the instructors. turns out I was not doing it the correct way. I tried running the curl command on the address to no avail. after messing around with the terminal I realized I just had to input quotes around a command and then another command. This is probably what was intended. After opening up the flag file as intended, I got the same flag as before {p1ng_as_a_@serv1c3}. This is probably what was intended so using this exploit I will try to create the shell.

### Part 2 (55 pts)
Shell implementation:
I built the shell system with a series of while true loops that would read inputs. First the inputs that would read for the quit, help, pull and shell commands. Once the shell command is typed in it enters another while true loop but also creates an array that will be used to keep track of the file system. In the shell loop I have four specific commands. First cd xxxxx which looks for the name of a directory. If this is found it adds the directory name to the end of the array with an "/" attached. Next I look for cd .. which if found pops the last entry in the array. next the third specific command that the shell looks for is exit which will just break the while true loop. Lastly the shell looks for ls because it is only a single command it will also insert the directory array as well. If that is not met the else condition is running the command and then the directory array. Useful for commands such as cat or grep. In the outer loop pull allows the user to pull a file of the address. help will give the user the list of possible commands and quit will exit the program entirely.

