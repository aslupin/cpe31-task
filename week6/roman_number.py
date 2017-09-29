txt = ''
roman = {1000:'M',900:'CM',500:'D',100:'C',90:'XC',50:'L',10:'X',9:'IX',5:'V',1:'I'}
number = int(input())
for i in roman:
    if(number // i == 4):txt += (roman[i]+roman[i*5])
    else:txt += (roman[i] * (number // i))
    number = number % i
print(txt)