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
dprint('.')
time.sleep(1)
dprint('.')
dprint ('Do you wish to start the game or not ? ')
start = input()
if start in begin:
    dprint('then let us begin')
    dprint('.')
    time.sleep(1)
    dprint('.')
    time.sleep(1)
    dprint('.')
    time.sleep(1)
    dprint('You awake from stasis, a flash of blinding light, your memory is fogged and cloudy. "Welcome back Captain, I have some troubling news, we have docked with an unknown outpost, it seems the outpost had a tractor beam which overpowered my engines. I am currently helpless to move the ship, and the outpost is not responding to our communications."')
else:
    dprint('well I guess you better get on with your incredible existence then, Human..')
    quit()
 