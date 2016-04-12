from __future__ import print_function

with open('mehface.txt') as f:
  while True:
    line = f.readline()
    if not line:
      break
    newline = line.replace("b","\033[39;49m ") #default
    newline = newline.replace(":","\033[33;43m ") #yellow
#    newline = newline.replace(";","\033[31;41m ") #red
    
    print(newline, end="")
