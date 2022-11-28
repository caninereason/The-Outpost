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


r5 =room(5,"""room5 """,[[0,0],[0,0],[0,0],[0,0],[1,1],[1,2],[1,3]],"")
r4 =room(4,"""room4 """,[[0,0],[0,0],[0,0],[0,0],[1,1],[1,2],[1,3]] ,"")
r3 =room(3,"room3",[[0,0],[0,0],[0,0],[0,0],[1,1],[1,2],[1,3]],"pickup")
r2 =room(2,"room2",[[0,0],[0,0],[0,0],[0,0],[1,1],[1,2],[1,3]],"pickup")
r1 =room(1,"""room1 """,[[0,0],[0,0],[0,0],[0,0],[1,1],[1,2],[1,3]] ,"")
r0 =room(0,"room0", [[0,0],[0,0],[0,0],[0,0],[1,1],[1,2],[1,3]],"")
rooms =[r1,r2,r3,r4,r5]

location = 0

def logic():
            global location
            goal = input()
            if goal in left and rooms[location].options[0][0] == 1:
                location = rooms[location].options[0][1]
                loop()
            elif  goal in right and rooms[location].options[1][0] == 1:
                location = rooms[location].options[1][1]
                loop()
            elif  goal in straight and rooms[location].options[2][0] == 1:
                location = rooms[location].options[2][1]
                loop()
            elif  goal in back and rooms[location].options[3][0] == 1:
                location = rooms[location].options[3][1]
                loop()
            elif  goal in one and rooms[location].options[4][0] == 1:
                location = rooms[location].options[4][1]
                loop()
            elif  goal in two and rooms[location].options[5][0] == 1:
                location = rooms[location].options[5][1]
                loop()
            elif  goal in three and rooms[location].options[6][0] == 1:
                location = rooms[location].options[6][1]
                loop()
            else:
                dprint("please choose a valid direction ")
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