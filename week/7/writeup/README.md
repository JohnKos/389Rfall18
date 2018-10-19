Writeup 7 - Forensics I
======

Name: John Kos
Section: 0201

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: John Kos

## Assignment 7 writeup

### Part 1 (40 pts)

1. Jpeg

2. Chicago Illinois, at the John Hancock Center

3. August 22nd 2018 11:33:24

4. Iphone 8

5. 539.5M altitude

6. CMSC389R-{look_I_f0und_a_str1ng} by using string and scrolling through the data. ran binwalk, notices that there were 4 other files besides the jpeg. tried extracting all of them but it only gave me the images in one pack plus the zlib. ran binwalk with extract and focusing on the png filetype with -D (binwalk -D 'png image:png' image) and got an image with the flag CMSC389R-(abr@cadabra}. Tried binwalk on different values with no results. Could not figure out how to decompress the zlib file.


### Part 2 (55 pts)

I ran sudo dd on the binary and then exiftool all the files only to see that they all have the same values. ran strings on binary and saw the text "where is your flag" as well as what looks like a bunch of python commands. After binwalking the files, I noticed again they were all the same meaning I probably only had to work with the original binary. I also noticed that it was an elf file, after googling, I decided I was gonna try to run python on it since it contained python commands. It failed but after looking at the string again I noticed a binary.c so I will try to remname it and run it. After running the binary itself I just got the text "where is your flag again. The last tool in forensics was steghide, after trying to analyze that I got requested a password. I figured I had to move onto looking into the binary itself next. tried readelf no help. used radare2 and saw /tmp/.stego in the main function. copied it to my folder and ran strings and saw nothing. Used binwalk and saw that the first decimal was not used and that the rest of the file was a jpeg. I ran binwalk again to download the jpeg file using --dd. Ran exiftool and strings on it to see anything and nothing changed. This reminded me of the first OSINT assignment where his password was given away from the pictures of pokemon, and maybe this is the password to the steghide. I tried steghide on the jpeg and got the flag. CMSC389R-{dropping_files_is_fun}. Funnily enough when I run steghide on the binary which is the first file that requested a password it says the binary is not supported.



