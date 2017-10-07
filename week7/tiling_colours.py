def til(n,txt):
    if(n==0):return 1
    else:
        if(txt == 'r'):return til(n-1,'x') + til(n-1,'x')
        else:return til(n-1,'x') + til(n-1,'x') + til(n-1,'r')
n = int(input())
print(til(n-1,'r') + til(n-1,'x') + til(n-1,'x'))