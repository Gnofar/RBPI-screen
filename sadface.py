#import RPIO.GPIO as GPIO

#sadface = open('sadface.txt','r')

with open('sadface.txt') as f:
    for line in f:
        for ch in line:
            if ch == "b":
                print "\033[31;47m"


with open('sadface.txt') as f:
    for line in f:
        print line
        
#with open('sadface.txt') as f:
#  while True:
#    c = f.read(1)
#    if not c:
#      print "End of file"
#      break
#    print "Read a character:", c
