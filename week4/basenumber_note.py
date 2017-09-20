def conBase(number):
    print(number%2,end="")
    if(number == 1):return '1'
    else:return conBase(number//2)


conBase(int(input()))