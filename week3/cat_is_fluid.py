import math
def gettime(t):
    if(t%5!=0): 
        if(t%5 < 3):return process(t//5*3) + process(t%5)
        else:return process(t//5*3) + process(3)
    else:return process(t//5*3)
def process(t):
    if t==0 :return 0
    elif(t > 3):return (t//3)*((27*3-(3**4)/4)/10-0.075)
    else:return ((27*t-(t**4)/4)/10-0.075)
    
t = int(input())
print("%g"%gettime(t))