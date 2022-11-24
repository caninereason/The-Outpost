import time
import sys

def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
begin = ["play","p","y","yes","start","s"]
left = ["left","l","w","west"]
right =["right","r","east","e"]
straight = ["forward","f","north","n"]
back = ["back","b","south","s"]
dprint("What is your name ")
name = input()
dprint(f'Greetings {name}! welcome to the outpost')
dprint ('Do you wish to start the game or not ')
start = input()
if start in begin:
    dprint('let us begin')
    dprint('.')
    time.sleep(1)
    dprint('.')
    time.sleep(1)
    dprint('.')
    time.sleep(1)
    dprint
else:
    dprint('well I guess you better get on with your incredible existence then, Human..')
    quit()
 