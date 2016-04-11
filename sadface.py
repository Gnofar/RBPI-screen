#import RPIO.GPIO as GPIO

#sadface = open('sadface.txt','r')

with open('sadface.txt') as f:
    for line in f:
        for ch in line:
            if ch == "b":
                print "\033[31;47m"
            elif ch== ":":
                print "\033[31;45m"
            else
                print "\033[31;46"

#with open('sadface.txt') as f:
#    for line in f:
#        print line
