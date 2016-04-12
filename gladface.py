from __future__ import print_function

with open('gladface.txt') as f:
  while True:
    line = f.readline()
    if not line:
      print("End of file")
      break
    newline = line.replace("b","\033[39;49m ") #default
    newline = newline.replace(":","\033[33;43m ") #yellow
    newline = newline.replace("a","\033[31;41m ") #red
    
    print(newline, end="")
