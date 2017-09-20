count_wet=0;ans=0;count_ppl=0
ppl = list();wet = list()
ppl.append(int(input())) # at index 0 = max ppl
wet.append(float(input())) # at index 0 = max weigth
while(True):
    n = int(input())
    if(n == -1):break
    w = float(input())
    if(w == -1):break
    if(w <= wet[0]):
        ppl.append(n)
        wet.append(w)
print(wet,ppl)
for i in range(1,len(ppl)):
    while(True):
        count_wet += wet[i]
        ppl[i] -= 1
        count_ppl += 1
        if(count_wet + wet[i] > wet[0] or count_ppl == ppl[0] or (ppl[i] == 0 and i == len(ppl)-1)):
            ans += 1
            count_wet = 0
            count_ppl = 0
        if(ppl[i] == 0):break
print(ans)