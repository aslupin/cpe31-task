count_ppl=0;count_wet=0;ans=0
ppl = list();wet = list()
ppl.append(int(input())) # at index 0 = max ppl
wet.append(int(input())) # at index 0 = max weigth
while(True):
    n = int(input())
    if(n == -1):break
    w = int(input())
    if(w == -1):break
    ppl.append(n)
    wet.append(w)
# loop in each group-ppl
for i in range(1,len(ppl)):
    while(True):
        ppl[i] -= 1
        count_ppl += 1
        count_wet += wet[i]
        if(count_wet + wet[i] > wet[0] or count_ppl == ppl[0]):
            print("{} {} {}".format(count_ppl,count_wet,ppl[i]))
            ans += 1
            count_ppl = 0
            count_wet = 0
        if(ppl[i] == 0):break
print(ans)


        




    



