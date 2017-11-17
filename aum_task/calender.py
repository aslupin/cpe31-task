m = int(input())
n = int(input())
Day = [31,28,31,30,31,30,31,31,30,31,30,31]
LeDay = [31,29,31,30,31,30,31,31,30,31,30,31]
def leap(n):
    if n%4 == 0:
        if n%100 == 0:
            if n%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def day(m,n):
    D = 0
    for i in range(1970,n):
        if leap(i) == True :
            D += 366
        else : 
            D += 365
    return D

def year(m):
    if leap(n) == True :
        month = [['sun','mon','tue','wed','thu','fri','sat']]
        count = 0
        for i in range(LeDay[m-1]//7+2):
            month.append([])
            for j in range(7):
                count += 1
                if count <= LeDay[m-1] :
                    month[i+1].append(count)
                else :
                    break
        return month
    elif leap(n) == False :
        month = [['sun','mon','tue','wed','thu','fri','sat']]
        count = 0
        for i in range(Day[m-1]//7+2):
            month.append([])
            for j in range(7):
                count += 1
                if count <= Day[m-1] :
                    month[i+1].append(count)
                else :
                    break
        return month
def BeCal(month):
    for i in range(len(month)):
        for j in range(len(month[i])):
            print(f'{month[i][j]:3}',end=' ')
        print()
print(leap(n))
print(year(m))
BeCal(year(m))
print(day(m,n))