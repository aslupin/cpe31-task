def check_leap_y(y):
  if(y%4==0):
    if(y%100==0):
      if(y%400==0):
        return True
      else:return False
    else:return True
  else: return False

def get_year(year,n=0):
  for i in range(1,year):
    if(check_leap_y(i)):n+=1
  getyear = ((year - 1 - n) * 365 ) + (n * 366)
  return getyear

ans = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
lim_y = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,10:273,11:304,12:334}
day = 0;date = list(map(int,input().split()))
day = get_year(date[2])
if(date[1] >= 3 and check_leap_y(date[2])):day += (1 + lim_y[date[1]] + date[0])
else:day += (lim_y[date[1]] + date[0])   
print(ans[day % 7])