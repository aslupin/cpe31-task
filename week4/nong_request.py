import random
def attack(typee,hp,ber_chk):
    if(random.randint(1,10) > 3):
        damage = random.randint(350,450)
        if(typee == 'me' and ber_chk): damage *= 2
        hp -= damage
        if(typee == 'me'):print("The monster loses %d hp"%damage)
        else:print("The hero loses %d hp"%damage)
    else:
        if(typee == 'me'):print("You missed!")
        else:print("Monster missed!")
    return hp
def defend():
    if(random.randint(1,10) > 3):
        print("Defend success!!!")
        return True
    else:
        return False
def heal(hp):
    healing = random.randint(350,700)
    print("Hero's hp was restored by %d points"%healing)
    return hp + healing

hp_me = 1500;hp_mon = 2000
count_heal = 2;ber_chk=False
while(True):
    defs = False
    print("Your hero has {} hp and the monster has {} hp".format(hp_me,hp_mon))
    item = input()
    if(item == 'A'):hp_mon = attack('me',hp_mon,ber_chk)
    elif(item == 'D'):defs = defend()
    elif(item == 'U'):
        item = input()
        if(item == 'H'):
            if(count_heal > 0):
                hp_me = heal(hp_me)
                count_heal -= 1
                print("%d healing potion left"%count_heal)
            else:print("hero cannot heal (no healing potion left)")
            print("Your hero has %d hp"%hp_me)
        if(item == 'B'):
            print("Berserk mode : on")
            ber_chk = True
    if(ber_chk):
        print("The hero loses 150 hp from berserk mode")
        hp_me -= 150
    if(not defs):hp_me = attack('mon',hp_mon,ber_chk)

    if(hp_me <= 0 or hp_mon <= 0):
        if(hp_mon <= 0 and hp_me <= 150 and ber_chk):
            print("Draw")
            break
        else:
            break