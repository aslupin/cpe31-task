c = [' ','*','-','\\','/']
inp = int(input())
for i in range(1,inp*2+1+1): # fool
    if(i==1):
        print(((inp*2)*c[0]) + '^' + ((inp*2)*c[0]))
    else:
        if(i%2==0):
            print(((inp*2+1-i) * c[0]) + (c[4]) + ((i*2-3)*c[1]) + (c[3]))
        elif(i%2==1):
            print(((inp*2+1-i) * c[0]) + (c[4]) + ((i*2-3)*c[2]) + (c[3]))