def chup(i,ii):
    if(i[1] == ii[1]): return "It’s a tie!!\nPlease continue" 
    elif(i[1] == 'rock' and ii[1] =='paper'):return str(ii[0]) + " wins"
    elif(i[1] == 'rock' and ii[1] == 'scissors'):return str(i[0]) + " wins"
    elif(i[1] == 'paper' and ii[1] =='rock'):return str(i[0]) + " wins"
    elif(i[1] == 'paper' and ii[1] == 'scissors'):return str(ii[0]) + " wins"
    elif(i[1] == 'scissors' and ii[1] == 'paper'):return str(i[0]) + " wins"
    elif(i[1] == 'scissors' and ii[1] == 'rock'):return str(ii[0]) + " wins"
    else: return "Invalid input \nPlease try again!!!"
playerone = ['name','item']
playertwo = ['name','item']
playerone[0] = input("Player 1 name : ")
playertwo[0] = input("Player 2 name : ")
print("Please input (rock/scissors/paper)")
while(True):
    playerone[1] = input(str(playerone[0]) + " : ")
    playertwo[1] = input(str(playertwo[0]) + " : ")
    print(chup(playerone,playertwo))
    if(chup(playerone,playertwo) != "Invalid input \nPlease try again!!!"):
        if(input("Do you want to play another game (yes/no) : ") == 'yes'):
            continue
        else:break
