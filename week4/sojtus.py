def findpirmeBT(n):
    if(n==1):return False
    for i in range(1,n+1):
        if(n%i == 0):
            if(i != 1 and i != n):
                return False
    return True
ans = 0;ignorePair = list()
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if( i+j == n and findpirmeBT(i) and findpirmeBT(j)):
            if(not(i in ignorePair)):
                ignorePair.append(j)
                ans += 1
print(ans)