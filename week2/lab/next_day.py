import sys
def check_leap_y(y):
  if(y%400 == 0 or (y%100 == 0 and y%4 == 0)):
    return True
  else: return False
def bye():
  sys.exit("Invalid input!")
  
lim_y = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31} 
y = input()
m = input()
if(m<= 0 or m>12):bye()
d = input()
if(check_leap_y(y) and m==2 and d>29):bye()
elif(d > lim_y[m]):bye()
if(d == lim_y[m]): 
  if(check_leap_y(y+1) and m==2):
    print("The next date is %d-%d-%d"%(y+1,m,d+1))
  elif(m == 12):print("The next date is %d-%d-%d"%(y+1,1,1))
  else:
    print("The next date is %d-%d-%d"%(y+1,m+1,1))
else:
  print("The next date is %d-%d-%d"%(y+1,m+1,d+1))
if(check_leap_y(y)):print("Year %d is leap year."%y)
else:print("Year %d is not leap year."%y)
