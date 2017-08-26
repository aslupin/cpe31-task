import math
movement = {"U":1,"R":1,"L":-1,"D":-1} # Const of movement
x = [0];y = [0] # list container for pattern
lastx=0;lasty=0;tmpx=0;tmpy=0 # declare var
check = False
fly = input()
here_x = int(input())
here_y = int(input())
for i in fly: # get each of pattern
    if(i == 'U' or i == 'D'):tmpy += movement[i]
    if(i == 'R' or i == 'L'):tmpx += movement[i]
    if(not(tmpx in x and tmpy in y)):
        x.append(tmpx)
        y.append(tmpy)
if(here_x <= 0 and here_y <=0):bignum = math.fabs(min(here_x,here_y))
else:bignum = max(here_x,here_y) # big-number
for i in range(len(x)):
    lastx = x[i] * bignum ;lasty = y[i] * bignum    
    for j in range(len(x)):
        if(lastx + x[j] == here_x and lasty + y[j] == here_y):check = True
if(check):print('Y')
else:print('N')