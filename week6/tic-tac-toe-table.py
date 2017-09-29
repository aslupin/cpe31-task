def t(n):
    for _ in range(n):
        for i in range(n+3):
            if(i <= n):print('-',end='')
            elif(i==n+1 or i==(n+1)*2):print('|',end='')
            elif(i>n+1):print('-',end='')
            else:print('-',end='')
def tttt(n):
    t(n)
    # tt(n)
    # ttt(n)
    # tttt(n)
n = int(input())
tttt(n)



#  || 
# -+-+-
#  || 
# -+-+-
#  ||