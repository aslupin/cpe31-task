from collections import deque
def killb(wbee,sbee,kill,i):
    kill[i-1] -= ( sbee[i-1] + wbee[i-1] )
    if(kill[i-1] > 0):
        if(sbee[i] > kill[i-1]):sbee[i] -= kill[i-1]
        else:
            kill[i-1] -= sbee[i]
            sbee[i] = 0
            if(wbee[i] > kill[i-1]):wbee[i] -= kill[i-1]
            else:wbee[i] = 0
    return wbee,sbee,kill,i

kill=list();wbee = deque();sbee = deque()
sbee.append(int(input()))
wbee.append(int(input()))
year = int(input())
for i in range(year):
    kill.append(int(input()))
for i in range(1,year+1):
    wbee.append( wbee[i-1] + sbee[i-1] + 1 )
    sbee.append( wbee[i-1] )
    killb(wbee,sbee,kill,i)
print("{} {}".format(wbee.pop(),sbee.pop()))