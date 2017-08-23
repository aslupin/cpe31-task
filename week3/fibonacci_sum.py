 def fibonacci_sum(n):
    # Code your fibonacci_sum(n) here
    def sumWithSol(n):
        if(n==1):return 1
        elif(n==0):return 0
        else:return sumWithSol(n-1) + sumWithSol(n-2)
    
     return sumWithSol(n+2)-1
### NO CODE AFTER THIS LINE SHOULD BE MODIFIED ###
inp = int(input())
print(fibonacci_sum(inp))