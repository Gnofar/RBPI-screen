from __future__ import print_function
import os

with open('sadface.txt') as f:
  os.system('clear'),
  while True:
    line = f.readline()
    if not line:
      break
    newline = line.replace("b","\033[39;49m ") #default
    newline = newline.replace(":","\033[33;43m ") #yellow
    newline = newline.replace("w","\033[97;107m ") #white
    
    print(newline, end="")
