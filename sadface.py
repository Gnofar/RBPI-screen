
with open('sadface.txt') as f:
  while True:
    line = f.readline()
    if not line:
      print "End of file"
      break
    newline = line.replace("b","\033[31;47m")
    newline = newline.replace(":","\033[31;45m")
    print newline
