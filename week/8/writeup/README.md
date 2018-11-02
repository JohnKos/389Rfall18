Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION HERE*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. Open wireshark and see a connection to facebook.com

2. clicking through the info and saw. Frame 22 laz0rh4x22 104.248.224.85. Started clicking through more on No 230. an address is interacting with laz0rh4x from address 206.189.113.189 and the name c0uchpot4doz

3. who is.

4. Using port 2749

5. (Meet Tomorrow at 1500 No 260. Plans updated 476. Still plan to meet tomorrow. He also sent a google drive link and mentioned a parser.

6. (I started with a binwalk of the file) I ran binwalk on the file and found a google drive link. This brought me to the update file. /drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

7. Tomorrow 

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*

Reading the documentation I saw that the file was 24 byes long. 4 magic, 4 version, 4 timestamp, 8 author and 4 section count. For everything other than author I figured I should use "L" because that was in the sample code and the specs said they were of the same type. I looked at the documentation to get how to deal with string( what the author should be) and saw a char and chose 8 as per specs again. 

I then do the same but for type and length. I don't know if I can open a png without the magic byte or maybe if I just call it a png it will work. The magic byte wasnt in the slides, so I think it might just work cause the magic byte is just to indicate file type anyway. It will be like last week, where I used exiftool to extract the files, I just had to specify what they were. For the array I could just make an array and unpack every value individually and add it to the array. The text I could just handle like author. I could do the same thing for an array of words and doubles as I did with D words. for the touple, I could unpack the two variables and print them. Section reference is just a single word, and ASCII is just more chars. Creating an array and pushing values seems to be creating issues, I am going to just see if I can encode all length at first insteaed.

Everything is working as intended except png. will try to encode the magic bytes first

1. Generated value was weird int, maybe I had the format wrong.

2. Created by laz0rh4x

3. 9. what does really mean? I ran the algorithm as long as I could and it found 11!

4. 
	1. Text "call this number to get your flag (422) - 537 - 7946"

	2. Word array
(3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9)

	3. Coordinates
38.99161  -77.02754

	4. Section 
Reference 1
	
	5. Text
('The imfamous security pr0s at CMSC389R will never find this!',)

	6. Text
('The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}',)

	7. coordinates
38.9910941  -76.9328019

	8. Png
	9. Text
('AF(saSAdf1AD)Snz**asd1',)
	10. Text
('Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9\n',)

	11. (4, 8, 15, 16, 23, 42)	

5.

	CMSC389-{PlaIN_dIfF_FLAG}
