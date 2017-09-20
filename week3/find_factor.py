def findFacBt(a,pairi,pairii):
    if(a>-1):end = a+1
    if(a>-1):a *= -1
    for i in range(a,end):
        for j in range(a,i+1):
            if(i*j == a):
                pairi.append(i)
                pairii.append(j)
            #if(i*j > a):break
    return pairi;pairii

pairi_a = list();pairii_a= list()
pairi_c = list();pairii_c= list()

print("Standard form is ax**2+bx+c")
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

findFacBt(a,pairi_a,pairii_a)  
findFacBt(c,pairi_c,pairii_c)
print(pairi_a)
print(pairii_a)
print(pairi_c)
print(pairii_c)
print(len(pairi_a))
# print(pairi_a[0])
# for i in range(0,len(pairi_a)):
    # print("({} {}) ({} {})".format(pairi_a[i],pairi_c[i],pairii_a[i],pairii_c[i]))    
    # if(b == (pairi_a[i]*pairii_c[i]) + (pairii_a[i]*pairi_c[i]) ):
    #     print("({} {}) ({} {})".format(pairi_a[i],pairi_c[i],pairii_a[i],pairii_c[i]))
        