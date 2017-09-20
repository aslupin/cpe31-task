##################################################
## Problem: 365_day_advanced.py
## Std: std05
## Name: Wattanai Sathuphan
## StudentId: 6010500117
##################################################
def checkMeet(fx,dx,fy,dy):#First of X, D of X, First of Y, D of Y
    xpass = False   #X pass XR
    ypass = False   #Y pass YR
    nx = ny = -1
    if(dx==0 and fx==xr):
        xpass = True
    elif(dx!=0):
        nx = (xr-fx)/dx
    if(dy==0 and fy==yr):
        ypass = True
    elif(dy!=0):
        ny = (yr-fy)/dy
    if(nx == ny and nx != -1):
        return True
    elif(xpass and (yr-fy)/dy%1==0):
        return True
    elif(ypass and (xr-fx)/dx%1==0):
        return True
    if(xpass and ypass):
        return True
move = input()      #input movement pattern
xr = int(input())   #X request
yr = int(input())   #Y request
x = 0               #X&Y starter
y = 0
Find = False
if(x==xr and y==yr):
    Find = True
else:
    l1 = []
    l2 = []
    for i in move:
        if(i=='U'):
            y+=1
        elif i=='D':
            y-=1
        elif i=='R':
            x+=1
        elif i=='L':
            x-=1
        if(x==xr and y==yr):
            Find = True
            break
        l1.append((x,y))
    for i in move:
        if(i=='U'):
            y+=1
        elif i=='D':
            y-=1
        elif i=='R':
            x+=1
        elif i=='L':
            x-=1
        if(x==xr and y==yr):
            Find = True
            break
        l2.append((x,y))
    for i in range (0,len(l1)):
        Find = checkMeet(l1[i][0],l2[i][0]-l1[i][0],l1[i][1],l2[i][1]-l1[i][1])
        if(Find):
            break
if(not Find):
    print("N")
else:
    print("Y")
