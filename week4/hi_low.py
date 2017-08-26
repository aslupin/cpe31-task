from random import randint
dice = int(input())
mon = int(input())

mondy=mon;count_dic = 0;score = 0
while(True):
    count_dic += 1
    mondy -= 10*count_dic
    if(mondy < 0):
        print("not enough money to bet")
        break
    play = int(input())
    if(play > dice*6):break
    if(play == randint(1,dice * 6)):
        score = count_dic * (mon/mondy)
        print("%.2f"%score)
        print(count_dic)
        print(mondy)
        break