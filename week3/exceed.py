while(True):
    distance = float(input("Input distance (m) : "))
    if(distance == 0):
        print("You have 100%% internet signal [0.0 m]")
        break
    elif(distance > 0 and distance <= 1):
        print("You have 75%% internet signal [In 0 - 1 : %.5f m]"%distance)
    elif(distance > 1 and distance <= 2):
        print("You have 50%% internet signal [In 1 - 2 : %.5f m]"%distance)
    elif(distance > 2 and distance <= 10):
        print("You have 25%% internet signal [In 2 - 10 : %.2f m]"%distance)
    else:print("You : I need healing!!!\nYou do not have internet signal [%d m]"%distance)
print("You : GG Ez kid")