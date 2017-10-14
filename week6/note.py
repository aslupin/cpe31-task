lim_y = {0:0,1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
summ = 0
for i in range(1,13):
    
    if(i==1):print(f"{i}:0,",end="")
    else:
        summ += lim_y[i-1]
        print(f"{i}:{summ},",end="")

