hisbox = list(map(int,input().split()))
wall = [0];sum_subwater=0;use=0
for i in wall:
    for b in range(hisbox[i],-1,-1):
        count = 0
        for j in range(i+1,len(hisbox)):
            if(b <= hisbox[j] and (i != j)): 
                if(not(j in wall)):wall.append(j)
                break
            count += 1
            if(j == len(hisbox)-1):count = 0
        sum_subwater += count
print(sum_subwater)