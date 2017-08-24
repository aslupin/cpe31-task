def fac(n):
    if(n==0):return 1
    else:return fac(n-1)*n

n = int(input())
k = int(input())
for i in range(1,fac(n)+1):
    if(i%n == 0 and i%k == 0):
        print(i)
        