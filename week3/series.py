def a(n):
    # Code your a(n) function here
    return 1+(n-1)*2
def b(n):
    # Code your b(n) function here
    if(n==1): return 1
    else:return b(n-1)*(n-1)
def sum_a(n):
    # Code your sum_a(n) function here
    sumsq=0
    for i in range(1,n+1):
        sumsq += a(i)
    return sumsq
def sum_b(n):
    # Code your sum_b(n) function here
    sumsq = 0
    for i in range(1,n+1):
        sumsq += b(i)
    return sumsq
### NO CODE AFTER THIS LINE SHOULD BE MODIFIED ###
n = int(input())
print("a({}) = {}".format(n,a(n)))
print("b({}) = {}".format(n,b(n)))
print("sum_a({}) = {}".format(n,sum_a(n)))
print("sum_b({}) = {}".format(n,sum_b(n)))