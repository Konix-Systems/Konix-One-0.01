# Konix Programming System 
# Distribution: Konix One 0.01
#
# Konix is a programming system, which is a system that runs off of a programming language console.
# Konix is run off of python, a programming language at http://python.org.
#
# - System Variables -
st = 1
vs = "Konix One 0.01"
from sys import argv # import is here to create system variables
si = open('bin/inf/sysinfo.txt')
sis = (si.read()).split('\n')
usrn = sis[0]
pw = sis[1]
t = 0
cu = ['','']
# - System Declarations -
import os
from os import listdir
from os.path import isfile, join
import subprocess
from subprocess import sys
from sys import argv
import time
# - Title Declaration -
print "- K O N I X -"
print ""
print "- Konix One 0.01 -"
print ""
# - Verification -
vpw = raw_input('Please enter the password for '+usrn+'. If you just installed Konix and do not know what your password is, it should be the word konix. >')
while vpw != pw and t < 10:
	t += 1
	print ("Incorrect, try again in "+str(2**t)+" seconds")
	time.sleep(2**t)
	vpw = raw_input('Please enter the password for '+usrn+'. If you just installed Konix and do not know what your password is, it should be the word konix. >')
if t == 10:
	print "Incorrect 10 times, killing konix"
	st = 0
else:
	print "Correct, acsess granted."
# - Command Reading - 
while st == 1:
	ucmd = raw_input(usrn+"@konix"+" >")
	cmd = ucmd.partition(' ')[0]
	if cmd == "print" or cmd == "pt":
		print ucmd.partition(' ')[2]
	if cmd == "ci":
		cuv = raw_input('Please enter the password for '+usrn+'. >')
		if cuv == pw:
			print "Acsess granted."
			cu[0] = raw_input("Please choose a username for your account: ")
			cu[1] = raw_input("Please choose a password for your account: ")
			usrn = cu[0]
			pw = cu[1]
			cutext = '\n'.join(cu)
			with open('bin/inf/sysinfo.txt', 'w') as e:
				e.write(cutext)
		if cuv != pw:
			print "Acsess denied."
	if cmd == "version" or cmd == "vs":
		print vs
	if cmd == "tedit" or cmd == "td":
		if ucmd.partition(' ')[2] == "-h" or ucmd.partition(' ')[2] == "-help":
			print "Konix Tedit v1.2 Help"
			print "To open tedit, type in tedit -u in the console"
			print "You should see that your text pointer also has @tedit"
			print "To use tedit, first type in text normally."
			print "When you are done writing text, create two spaces, put 4 astrixes, and press enter again."
			print "It will show you what you wrote, and you have the option to save or not."
			print "Good luck using tedit!"
		elif ucmd.partition(' ')[2] == "-u":
			input_list = []
			while True:
				input_str = raw_input("konix@"+usrn+"#tedit >")
				if input_str == "****" and input_list[-1] == "":
					break
				else:
					input_list.append(input_str)
			for line in input_list:
				print line
			save = raw_input("Would you like to save this text to your file? [Y/N]: ")
			if save == "Y" or save == "y":
				name = raw_input("Please enter a name for this file (with .txt at the end): ")
				fsys = "fsys/"
				fsys += name
				filestring = '\n'.join(input_list)
				with open(fsys, 'w') as f:
					f.write(filestring)
			elif save != "N" or save != "n":
				print "Not saving"
	if cmd == "gm" or cmd == "game":		
		lnk = "gms/"+ucmd.partition(' ')[2]
		if os.path.isfile(lnk):
			subprocess.check_call([sys.executable, lnk])
		else:
			print (ucmd.partition(' ')[2]+" is not a game in your game directory.")
	if cmd == "list" or cmd == "ls":
		cwd = os.getcwd()
		files = os.listdir(cwd)
		files_fsys = os.listdir(files[4])
		list = '\n'.join(files_fsys)
		print list
		print ("\n"+str(os.path.getsize("fsys"))+" bytes used out of 2097152 bytes")
	if cmd == "kill" or cmd == "kl":
		print "Killing Konix - Farewell!"
		st = 0
	
