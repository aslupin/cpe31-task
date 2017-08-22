def my_ceiling(x):
    return int(x)+1
def my_floor(x):
    return int(x)-1
def my_fabs(x):
    if(x<0):return x*(-1)
    else:return x
def my_factorial(x):
    if(x==0):return 1
    else:return my_factorial(x-1) * x
def my_exp(x):
    e = 1
    if(x==0):return e
    else:
        for i in range(x):
            e *= 2.71828
        return e
def my_pow(x,y):
    if(y == 0):return 1
    elif(y == 1):return x
    else:
        for i in range(y-1):
            x *= x
        return x
#https://en.wikipedia.org/wiki/Methods_of_computing_square_roots
def my_sqrt(x,xpro = 1):
    if(x < 10):xpro =  2 * my_pow(10,x//10)
    else:xpro = 6 * my_pow(10,x//10)
    for i in range(10):
        xpro = (1/2) * (xpro + (x / xpro))
    return xpro
        
def my_cos(x,summ=0,i=0):
    for j in range(0,11):
        getplus = my_pow(x,i)/my_factorial(i)
        if(j%2!=0):getplus*=-1
        summ += getplus
        i += 2
    return summ
def my_sin(x,summ=0,i=1):
    for j in range(0,11):
        getplus = my_pow(x,i)/my_factorial(i)
        if(j%2!=0):getplus*=-1
        summ += getplus
        i += 2
    return summ
def my_tan(x):
    return my_sin(x)/my_cos(x)
def my_degree(x):
    return x*(180/my_pi())
def my_radian(x):
    return x*(my_pi()/180)
def my_pi():
    return 3.14159265359
def my_e():
    return 2.71828
print(my_sqrt(3))