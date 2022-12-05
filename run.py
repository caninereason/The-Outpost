import sys
import time
import random
import os

delay = 0.02
tdelay = 1


# main game loop,  printing rooms description and options
def loop():
    dprint(rooms[location].desc)
    logic()
    loop()


# delay print time
def dprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)


# initial room definition
class room:
    def __init__(self, number, desc, options, extra):
        self.number = number
        self.desc = desc
        self.options = options
        self.extra = extra


# clear screen
clear = True
# inventory bools
key = False
lazer = False
inv = [key, lazer]
rand = [7, 12, 6]

# direction bools
begin = ["play", "p", "y", "yes", "start", "s"]
left = ["left", "l", "w", "west"]
right = ["right", "r", "east", "e"]
straight = ["forward", "f", "north", "n", "up"]
back = ["back", "b", "south", "s", "down"]
one = ["1", "one", "door one" "z", "first", "1st"]
two = ["2", "two", "door two", "second", "2nd"]
three = ["3", "three", "door three", "door 3", "third", "3rd"]
pickup = ["take", "pickup", "grab", "use", "p", "examine", "book"]
ship = ["return", "ship", "enter"]
go = ["go", "walk", "run"]

# room number, description, connections array and extra options
r14 = room(14, """ You enter the room and the door shuts tight behind you
'Hello captain, I have been watching you for quite some time. If you can answer
this riddle I will allow you to leave 
'What is greater than God,
More evil than the devil,
The poor have it,
The rich don't need it,
And if you eat it, you'll die?'\n""", [0, 0, 0, 0, 0, 0, 0], "",)
r13 = room(
    13,
    """This room seems to be the central control room of this facility. In the
middle of the room is a large console, surrounded by switches, dials and knobs.
There is a door to the EAST and another to the WEST.you can see two doors on a
lower platform ,  you may enter door 1 or door 2. """, [7, 12, 0, 0, 6, 14, 0],
    "",
)
r12 = room(
    12,
    """You find yourself in a corridor with 2 doors leading off to the EAST
and a hatch leading SOUTH. The corridor ends in an open doorway leading NORTH.
Would you like to take the FIRST or SECOND door on the near wall, or head NORTH
or SOUTH\n""",
    [0, 0, 13, 11, 9, 10, 0],
    "",
)
r11 = room(
    11,
    """You find yourself in a room containing shelves packed with crates,boxes,
barrels and other containers. It smells damp and musty here. On one shelf\n
stands a metal box, seemingly empty.
There is a small hatch in the bottom of the box. You openthe box and find that
it contains a large collection of vials, each labeled with a different chemical
compound. You recognise the compounds to be highly radioactive and decide it 
would be best to leave them here.
To the EAST looks like a long corridor,  and a circular room is visable to the
SOUTH\n """, [0, 12, 0, 8, 0, 0, 0], "",)
r10 = room(
    10,
    """you enter a small room with an old wooden desk. On top of the desk sits 
a book that looks like it might contain useful information. There is a ladder to
the WEST and an exit heading NORTH\n """,
    [5, 0, 12, 0, 0, 0, 0],
    """You suddenly find yourself engulfed in light and find yourself transported
to a new location in the station...\n""",
)
r9 = room(
    9,
    """Here you discover a room containing rows of shelves crammed with crates, 
barrels,  boxes and other containers. It smells damp and musty here. In the
middle of the room is a large metal cylinder with a door set into its side
labeled Z. There appears to be a long corridor to the EAST.There is also a
passage leading WEST to the upper level.\n """,
    [8, 12, 0, 0, 5, 0, 0],
    "",
)
r8 = room(
    8,
    """A large dome shaped room,  full of floating globes of glowing jelly. They
wave gently in the air currents,  occasionally bumping into each other. Some of
them glow brightly,  making the entire room throb with an eerie green light.
Your flashlight barely penetrates the gloom,  illuminating only the nearest
jelly globe. This one pulses with a soft red light. The others seem to be
inactive. There are several more jelly globes beyond this one. Most of them
appear to be inert,  but one glows dimly with a yellowish light. It appears to
notice your presence and slowly moves toward you. Another jelly globe pokes out
of the far corner of the room,  and moves quickly to get out of sight. The whole
chamber is filled with a low hissing noise. There are 4 exits here NORTH, 
SOUTH,  WEST and to the EAST\n""",
    [2, 9, 11, 3, 0, 0, 0],
    "",
)
r7 = room(
    7,
    """You enter the opening and find yourself facing a narrow corridor. Its 
walls are decorated with strange carvings,  each one depicting some kind of 
bizarre monster. There is a door to the NORTH and another to the EAST.\n """,
    [0, 4, 13, 0, 0, 0, 0],
    "",
)
r6 = room(
    6,
    """You decide to explore further which leads you to a large circular room
lit by powerful energy crystals hanging from the wall. Some kind of equipment
is bolted to the floor here,  but most of it lies broken and twisted. There is a
narrow passage leading NORTH through the center of the room. To the WEST you
can see broken machinary littered around and to the EAST is a dark room with a
small flashing light\n""",
    [4, 2, 13, 0, 0, 0, 0],
    "",
)
r5 = room(
    5,
    """The room seems empty except for an oddly shaped piece of machinery resting
on the floor. The machine is made of a dull gray metal and looks vaguely
humanoid. It resembles a mechanical man standing upright,  with four long legs, 
a torso,  and a cylindrical head. The machine has been broken into pieces. A few
gears and wheels remain intact,  along with a couple of wires that run down its
spine. All the other parts lie scattered across the floor.There is a ladder to
the WEST,  and exits to the NORTH and EAST \n """,
    [3, 10, 9, 0, 0, 0, 0],
    "",
)
r4 = room(
    4,
    """You follow the hall and enter a large room filled with ancient, 
battered machinery. The walls and ceiling are covered in flickering blue energy
crystals that pulse with strange patterns. A narrow catwalk runs along the top
of this chamber. A long corridor continues WEST,  to the NORTH is a small
passage through some airvents and to the EAST is the landing pad,  which
direction would you like to take?\n  """,
    [7, 1, 6, 0, 0, 0, 0],
    "",
)
r3 = room(
    3,
    """You have entered a large room where a pair of doors face each other across a
wide chasm. To the WEST lies the landing bay and your ship. Beyond the doors is
darkness.The two doors are identical. Each is made of a solid block of metal, 
about three feet thick. The stone is carved with a strange language that you
cannot read. One door to the NORTH has an iron ring set into its surface,  while
the other EAST door appears to be hollow.\n""",
    [1, 5, 8, 0, 0, 0, 0],
    "",
)
r2 = room(
    2,
    """It's too dark to see anything clearly,  so you activate your flashlight. The
room seems mostly empty until you notice something moving in the shadows.
Something is crouched on one of the shelves lining the back wall; it looks like
a huge spider made of metal. It scuttles forward suddenly and lunges at you!
You fire your lazer wildly,  missing the creature completely and blasting a
chunk out of the wall before you. The spider scurries off to the EAST,  with a
noise that leaves your heart pounding. There are exits to the WEST and EAST and
a door to the SOUTH which looks like it returns you to the landing bay. Which
way would you like to go?\n""",
    [6, 8, 0, 1, 0, 0, 0],
    "",
)
r1 = room(
    1,
    """The Crystal Palace looms high above you as you step out onto its vast
landing bay. The lights glow softly inside the enormous structure,  casting long
shadows across the crystalline walls. You can see a small flashing object on
the ground in front of you.This place has a cold ominous prescence and you fear 
if you do not find a way out soon,  you will be stuck here forever. 
There are three doors here,  each marked with some alien hieroglyphics you 
have never seen before.
You may return to the SHIP or would you like to choose 1,  2 or 3?\n """,
    [0, 0, 0, 0, 4, 2, 3],
    """you take the object
which looks much like a key of some sort.You may return to the SHIP or would
you like to choose door 1,  2 or 3?\n""",
)
r0 = room(
    0,
    """There is no sign of any movement,  and the place seems eerily quiet.
If you would like to leave the ship and investigate the
outpost press 1,  if you would like to search the ship for any valuable supplies
press 2. If you would like to speak to the AI press 3\n """,
    [0, 0, 0, 0, 1, 1, 1],
    "",
)

# array of rooms
rooms = [r0, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14]

# current room location and checker to clear screen
location = 0
check = 1


# deals with input, room choices, extra options and pickups
def logic():

    global location
    global rooms
    global r1
    global clear
    global check
    goal = input().strip().lower()
    global key, lazer
    
    if clear is not True:
        os.system("cls" if os.name == "nt" else "clear")
        clear = True

    if check is not location:
        clear = False
        check = location
    
    if " " in goal:
        dprint("please only use 1 word commands with no spaces\n")
        logic()

    if goal in go:
        dprint("please don't use that word,  just pick an option OK\n")
        logic()

    if goal in left and rooms[location].options[0] != 0:
        location = rooms[location].options[0]
        loop()

    elif goal in right and rooms[location].options[1] != 0:
        if location == 5:
            location = 10
            dprint(
                """You climb the ladder and enter a small room with an old wooden desk. On top of the desk sits a book that looks like it might contain useful information.The ladder leads DOWN to where you came from,  and NORTH there lies a long corridor
with many doors"""
            )
            logic()

        else:
            location = rooms[location].options[1]
            loop()

    elif goal in straight and rooms[location].options[2] != 0:
        if location == 12 and inv[0] is not True:
            dprint("the door is locked,  there must be another way around")
            loop()

        elif location == 12 and inv[0] is True:
            dprint(
                """as you approach the door the object in your pocket begins to pulse and
vibrate. Suddenly there is a loud piercing sound and the door slides open
revealing a huge central control station. You enter cautiously..."""
            )
            location = rooms[location].options[2]
            loop()

        else:
            location = rooms[location].options[2]
            loop()

    elif goal in back and rooms[location].options[3] != 0:
        location = rooms[location].options[3]
        loop()

    elif goal in one and rooms[location].options[4] != 0:

        location = rooms[location].options[4]
        loop()

    elif goal in two and rooms[location].options[5] != 0:
        if location == 13 and lazer:
            dprint(
                """As you approach the door you hear a sharp metalic sound and what looks like
a gun turret comes up from the floor. You stand back and fire your lazer and
the turret disintegrates,  leaving you free passage to the room. You enter
cautiously"""
            )
            location = 14
            loop()

        elif location == 13 and lazer is not True:
            dprint(
                """As you approach the door you hear a sharp metalic sound and what looks like
a gun turret comes up from the floor. It starts firing wildly in your direction
and you run for the nearest exit,  barely escaping being vaporised\n"""
            )
            location = random.choice(rand)
        elif location != 0:
            location = rooms[location].options[5]
            loop()

        else:
            dprint(
                """after much searching you find a small lazer device with enough charge for a few uses,  it may prove to be useful.\n"""
            )
            lazer = True
            rooms[0].desc = (
                """  There is no sign of any movement,  and the place seems eerily quiet.If you
would like to leave the ship and investigate the outpost press 1,  if you would
like to speak to the AI press 3\n """,
            )
            rooms[0].options = [0, 0, 0, 0, 1, 0, 1]
            loop()

    elif goal in three and rooms[location].options[6] != 0:
        if location != 0:
            location = rooms[location].options[6]
            loop()

        else:
            dprint(
                """'captain I believe I have been infected with a complex virus,  I only have
nothing left to say,  I only have nothing left to say'... The computer continues
as you wonder how you can fix this mess.\n"""
            )
    elif goal in pickup and rooms[location].extra != "":
        if location == 1 and inv[0] is False:
            dprint(rooms[location].extra)
            inv[0] = True
            rooms[
                1
            ].desc = """The Crystal Palace looms high above you as you step out onto its vast
landing bay. The lights glow softly inside the enormous structure,  casting long
shadows across the crystalline walls.This place has a cold ominous prescence and
you fear if you do not find a way out soon,  you will be stuck here forever. 
There are three doors here,  each marked with some alien hieroglyphics you have
never seen before.
You may return to the SHIP or would you like to choose 1,  2 or 3?\n """
            logic()

        elif location == 1 and inv[0] is True:
            dprint("you already took the object\n")
            logic()

        elif location == 10:
            dprint(rooms[location].extra)
            location = random.choice(rooms).number
            loop()

        else:
            dprint(rooms[location].extra)

    elif goal in ship and location == 1:
        location = 0
        dprint(rooms[0].desc)
        logic()

    elif location == 14 and goal == "nothing":
        dprint(
            """'That is the correct answer,  I wish you luck on your journey captain' You
suddenly find yourself transported back to your ship,  with all systems
apparently functioning.'glad to see you captain,  I sense a large anti matter
buildup in the outposts main engine room,  I have full control of our vessel now
and am initiating the undocking sequence,  we must escape quickly' The ship
rattles wildly as the main engines power up. You see the outpost move away from
you rapidly,  and in a matter of seconds there is a blinding light as the
outpost explodes with a huge shockwave jolting the ship. 'I am glad for your
safe return captain,  I feared our journey might have ended there, please resume
your position in your statis pod and I will continue our course home' You climb
into your statis pod and think of what may have become of you had you not kept
your wits about you. The stasis pod closes and you smell the familiar odor of
stasis gases. ' We shall find home soon captain, sleep well"""
        )
        time.sleep(tdelay)
        dprint(".")
        time.sleep(tdelay)
        dprint(".")
        time.sleep(tdelay)
        dprint("""congratulations on completing the outpost, many adventurers 
have fallen here.We commend you for your wit, skill and expertise..
See you in the next adventure.""")
        time.sleep(tdelay)
        dprint(".")
        time.sleep(tdelay)
        dprint(".")
        time.sleep(tdelay)
        quit()

    elif location == 14 and goal != "nothing":
        dprint(
            """'that is incorrect,  I am sorry captain you have not worthy.'The room starts
to fill with a noxious gas,  you try to find some way out but you soon lose
consciousness.GAME OVER"""
        )
        quit()

    else:
        dprint("please choose a valid option\n ")
        clear = True
        logic()


# initial welcome and beginning
dprint("Welcome\n")
dprint("What is your name:  ")
name = input().strip()
while name == "":
    dprint("please enter your first name only\n")
    dprint("What is your name:  ")
    name = input().lower().strip()
dprint(f"Greetings {name}!\n Welcome to the Outpost")
time.sleep(1)
dprint(".")
time.sleep(1)
dprint(".\n")
dprint("Do you wish to start the game?\n ")
start = input().lower().strip()
if start in begin:
    dprint("Then let us begin")
    dprint(".")
    time.sleep(tdelay)
    dprint(".")
    time.sleep(tdelay)
    dprint(".\n")
    time.sleep(tdelay)
    dprint(
        """You awake from stasis, a flash of blinding light,  your memory is fogged and
cloudy. "Welcome back Captain" the familiar voice of the ships AI echoes " I
have some troubling news, we have docked with an unknown outpost, it seems the
outpost had a tractor beam which overpowered my engines. I am currently
helpless to move the ship, and the outpost is not responding to our
communications."\n"""
    )
    dprint(".")
    time.sleep(tdelay)
    dprint(".")
    time.sleep(tdelay)
    dprint(".\n")
    time.sleep(tdelay)
    dprint(
        """You exit your stasis pod and see a huge crystalline palace out the window."""
    )
else:
    dprint(
        "Well I guess you better get on with your incredible existence then, Human.."
    )
    quit()
loop()
