import sys
ppl = list()
count = 0;mdthree = 0;do = 0
n = int(input())

for i in range(n):
    ppl.append(int(input()))
    if(ppl[i] > 8):sys.exit("error")
ppl.sort()
for i in range(n):
    mdthree += 1
    if(ppl[i] - ppl[i-1] > 1 and i != 0):
        do+=1
        mdthree = 1
    elif(mdthree == 1):do+=1
    elif(mdthree == 3):mdthree = 0
print(do)