def repl():
    repl = input()
    if(repl == 'Y'):return True
    else:return False

point = [0,0,0,0]
while(True):
    print("Dating with Emilia ?:")
    if(repl()):
        point[0] += 1
        print("Run into Stella ?:")
        if(repl()):continue
    print("Dating with Rem?:") 
    if(repl()):
        point[1] += 1
        print("Run into Stella ?:")
        if(repl()):continue
    print("Dating with Stella ?:")
    if(repl()):
        point[2] += 1
        continue    
    print("Dating with Roswaal?:")
    if(repl()):
        point[3] += 1
        break
    break
print("Subari : %d\nEmilia : %d\nRem : %d\nStella : %d\nRoswaal : %d"%(point[0]+point[1]+point[2]+point[3],point[0],point[1],point[2],point[3]))