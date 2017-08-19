def my_ceiling(x):
    return int(x)+1
def my_floor(x):
    return int(x)-1
def my_fabs(x):
    if(x<0):return x*(-1)
    else:return x
def my_factorial(x):
    if(x==1):return 1
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
# def my_sqrt(x):
# def my_cos(x):
# def my_sin(x):
# def my_tan(x):
# def my_degree(x):
# def my_radian(x):
# def my_pi():
# def my_e():
print(my_exp(2))
print(2.71828**2)