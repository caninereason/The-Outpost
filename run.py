begin = ["play","p","y","yes","start","s"]
left = ["left","l","w","west"]
right =["right","r","east","e"]
straight = ["forward","f","north","n"]
back = ["back","b","south","s"]
name = input("What is your name ")
print(f'Greetings {name}! welcome to the outpost')
start = input ('Do you wish to start the game or not ')
if start in begin:
    print('let us begin')
else:
    print('well I guess you better get on with your incredible existence then, Human..')
    quit()
