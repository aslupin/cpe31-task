def dining_table(n,x=1):
    # Code your dining_table(n) function here
    if(n==0):return 1
    elif(n//x <= x+1):return x+1
    else:return dining_table(n//x,x+1) 
    ### NO CODE AFTER THIS LINE SHOULD BE MODIFIED ###
n = int(input())
print(dining_table(n))