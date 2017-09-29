def t(n):
    nloop = (n*3)+2+1
    for _ in range(n):
        for i in range(1,nloop):
            if(i==n+1 or i==(n+1)*2):print('|',end='')
            else:print(' ',end='')
        print('\n')
def tt(n):
    nloop = (n*3)+2+1
    for i in range(1,nloop):
        if(i==n+1 or i==(n+1)*2):print('+',end='')
        else:print('-',end='')
    print('\n')
def tttt(n):
    t(n)
    tt(n)
    t(n)
    tt(n)
    t(n)
n = int(input())
tttt(n)