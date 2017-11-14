m = int(input())
n = int(input())
# m = 4
# n = 4
mm = [[int(i) for i in range(n)] for x in range(m)]
print(mm)
# for i in range(len(mm)):
for j in range(len(mm[0])-1):
    itr_r = j
    itr_c = 0
    while(itr_r != -1 and itr_c != len(mm)+1):
        print(mm[itr_c][itr_r],end=" ")
        itr_c += 1 
        itr_r -= 1
    print('')


for j in range(len(mm)):
    itr_r = len(mm[0])-1
    itr_c = j
    while(itr_c != len(mm) and itr_r != -1):
        print(mm[itr_c][itr_r],end=" ")
        
        itr_c += 1 
        itr_r -= 1
    
    print('')
