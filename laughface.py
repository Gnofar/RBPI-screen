from __future__ import print_function
import time
import os

for x in xrange(1,5):
	os.system('clear'),
	with open('laughface.txt') as f:
	  while True:
	    line = f.readline()
	    if not line:
	      break
	    newline = line.replace("b","\033[39;49m ") #default
	    newline = newline.replace(":","\033[33;43m ") #yellow
	    newline = newline.replace("w","\033[97;107m ") #white    
	    print(newline, end="")
	time.sleep(1),
	os.system('clear'),
	with open('laughcryface.txt') as f:
	  while True:
	    line = f.readline()
	    if not line:
	      break
	    newline = line.replace("b","\033[39;49m ") #default
	    newline = newline.replace(":","\033[33;43m ") #yellow
	    newline = newline.replace("w","\033[97;107m ") #white
   	    print(newline, end="")
	time.sleep(1)
	    
