import time
import sys

delay = 0
tdelay = 0

condition =True
def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)

class room:
    def __init__(self,number,desc,options,extra):
        self.number = number
        self.desc =desc
        self.options=options
        self.extra=extra
       

begin = ["play","p","y","yes","start","s"]
left = ["left","l","w","west"]
right = ["right","r","east","e"]
straight = ["forward","f","north","n"]
back = ["back","b","south","s"]
one =["1","one","door one"]
two =["2","two","door two"]
three =["3","three","door three","door 3"]

r14=room(14,"""room14 """,[0,0,0,0,0,0,0],"")
r13=room(13,"""room13 """,[7,12,0,0,0,6,14],"")
r12=room(12,"""room12 """,[11,0,13,0,9,10,0],"")
r11=room(11,"""room11 """,[0,12,0,8,0,0,0],"")
r10=room(10,"""room10 """,[0,0,0,0,5,12,0],"")
r9=room(9,"""room9 """,[8,0,0,0,5,12,0],"")
r8=room(8,"""room8 """,[11,3,2,9,0,0,0],"")
r7=room(7,"""room7 """,[0,0,13,4,0,0,0],"")
r6 =room(6,"""You decide to explore the airvents which lead you to a large circular room lit by powerful energy crystals hanging from the wall. Some kind of equipment is bolted to the floor here, but most of it lies broken and twisted. There is a narrow passage leading north through the center of the room. To the east you can see broken machinary littered around and to the west is a dark room with a small flashing light""",[0,2,13,0,4,0,0],"")
r5 =room(5,"""room5 """,[3,10,9,0,0,0,0],"")
r4 =room(4,"""You follow the hall to the left and enter a large room filled with ancient, battered machinery. The walls and ceiling are covered in flickering blue energy crystals that pulse with strange patterns. A narrow catwalk runs along the top of this chamber. A long corridor continues west, to the north is a small passage through some airvents and to the east is the landing pad, which direction would you like to take?\n  """,[7,1,6,0,0,0,0] ,"")
r3 =room(3,"room3",[1,0,8,5,0,0,0],"pickup")
r2 =room(2,"It's too dark to see anything clearly, so you activate your flashlight. The room seems mostly empty until you notice something moving in the shadows. Something is crouched on one of the shelves lining the back wall; it looks like a huge spider made of metal. It scuttles forward suddenly and lunges at you! You swing your pistol wildly, missing the creature completely. The gun fires again and blasts a chunk out of the wall behind you.The spider scurries off to the east, with a noise that leaves your heart pounding. There are exits to the west and east and a door to the south which looks like it returns you to the landing bay.which way would you like to go?\n",[4,3,0,1,0,0,0],"pickup")
r1 =room(1,"The Crystal Palace looms high above you as you step out onto its vast landing bay. The lights glow softly inside the enormous structure, casting long shadows across the crystalline walls. You can see nothing else around you or anywhere near the ship. There are three doors here, each marked with some alien hieroglyphics you have never seen before. Which door would you like to choose 1,2 or 3?\n ",[0,0,0,0,4,2,3] ,"")
r0 =room(0,"You exit your stasis pod and look out the ships window to see a huge crystalline palace before you. There is no sign of any movement, and the place seems eerily quiet. If you would like to leave the ship and investigate the outpost press 1, if you would like to search the ship for any valuable supplies press 2\n ",
 [0,0,0,0,1,1,0],"")
rooms =[r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14]

location = 0

def logic():
            global location
            goal = input()
            if goal in left and rooms[location].options[0] != 0:
                location = rooms[location].options[0]
                loop()
            elif  goal in right and rooms[location].options[1] != 0:
                location = rooms[location].options[1]
                loop()
            elif  goal in straight and rooms[location].options[2] != 0:
                location = rooms[location].options[2]
                loop()
            elif  goal in back and rooms[location].options[3] != 0:
                location = rooms[location].options[3]
                loop()
            elif  goal in one and rooms[location].options[4] != 0:
                
                location = rooms[location].options[4]
                loop()
               
            elif  goal in two and rooms[location].options[5] != 0:
                if location !=0:
                    location = rooms[location].options[5]
                    loop()
                else:
                     dprint("after much searching you find a small lazer device with enough charge for 2 uses, it may come in handy. You decide to leave the ship and investigate the outpost\n")
                     location=1
            elif  goal in three and rooms[location].options[6] != 0:
                location = rooms[location].options[6]
                loop()
            else:
                dprint("please choose a valid option ")
                logic() 
def loop():
        
        dprint(rooms[location].desc)
        dprint(rooms[location].extra)
        logic()
        loop()
        
        
        
    

# dprint("What is your name ")
# name = input()
# dprint(f'Greetings {name}! welcome to the outpost')
# dprint('.')
# time.sleep(1)
# dprint('.')
# dprint ('Do you wish to start the game or not ? ')
# start = input()
# if start in begin:
while (condition):
    dprint('then let us begin')
    dprint('.')
    time.sleep(tdelay)
    dprint('.')
    time.sleep(tdelay)
    dprint('.')
    time.sleep(tdelay)
    dprint("""You awake from stasis, a flash of blinding light, your memory is fogged and cloudy. "Welcome back Captain" the familiar voice of the ships AI echoes " I have some troubling news, we have docked with an unknown outpost, it seems the outpost had a tractor beam which overpowered my engines. I am currently helpless to move the ship, and the outpost is not responding to our communications."
    """)
    condition=False
# else:
#     dprint('well I guess you better get on with your incredible existence then, Human..')
#     quit()
loop()