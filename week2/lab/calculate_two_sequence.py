import sys
def seqii(a,n,d):
  if n==1 : 
    print("Your answer is "+str(a))
  else:
    seqii(a+d,n-1,d*2)

a = input("First order: ")
b = input("Second order: ")
c = input("Third order: ")
ans = input("What order you want to find: ")
# basic task
if(ans == 1):print("First order: %d"%a)
elif(ans ==2):print("Second order: %d"%b)
elif(ans ==3):print("Third order: %d"%c)
else:
  # check input
  if(ans > 15 or ans <= 0):sys.exit("Error")
  # check sqe
  if(a-b == b-c):print("Your answer is %d"%(a+((ans-1)*(b-a))) )
  else:seqii(a,ans,b-a)
