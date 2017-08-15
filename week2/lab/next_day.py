import sys
def check_leap_y(y):
  if(y%4==0):
    if(y%100==0):
      if(y%400==0):
        return True
      else:return False
    else:return True
  else: return False
def bye():
  sys.exit("Invalid input!")
lim_y = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} 
y = int(input())
m = int(input())
if(m<= 0 or m>12):bye()
d = int(input())
if(check_leap_y(y) and m==2 and d>29):bye()
elif(d > lim_y[m] and not check_leap_y(y)):bye()
if(d == lim_y[m] or (d==29 and m==2)): 
  if(check_leap_y(y) and m==2): #y+1
    if(d == 29):print("The next date is %d-%02d-%02d"%(y ,m+1,1))
    else:print("The next date is %d-%02d-%02d"%(y ,m,d+1)) #y+1
  elif(m == 12):print("The next date is %d-%02d-%02d"%(y+1,1,1))
  else:
    print("The next date is %d-%02d-%02d"%(y,m+1,1)) #y+1
else:
  print("The next date is %d-%02d-%02d"%(y,m,d+1))
if(check_leap_y(y)):print("Year %d is leap year."%y)
else:print("Year %d is not leap year."%y)
