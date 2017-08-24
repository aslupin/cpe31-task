def hdraw(n):
    for i in range((n*4) - (n-1)):print("*",end="")
    print('')
    for i in range(2):
        for i in range((n*4) - (n-1)):
            if(i % 3 == 0):print("*",end="")
            else:print(" ",end="")
        print('')
    for i in range((n*4) - (n-1)):print("*",end="")
def vdraw(n):
    for i in range(n):
        if(i==0):
            print("****")
            print("*  *")
            print("*  *")
            print("****")
        else:
            print("*  *")
            print("*  *")
            print("****")
while(True):
    vh = input("Select mode (v or h): ")
    if(vh == 'v' or vh == 'h'):break
while(True):
    n = int(input("Input n (1-15): "))
    if(n >= 1 and n <= 15):break

if(vh == 'v'):vdraw(n)
elif(vh == 'h'):hdraw(n)