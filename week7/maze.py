way = list()
control = ['U','D','L','R']
strpos = [0,0]
m,n = map(int,input().split())

def can(i,j):
    if(i<0 or i>=m or j<0 or j>=n):return False
    return True

def ezpass(i,j):
    if(can(i,j) and (way[i][j] == ' ' or way[i][j] == 'I')):return True
    return False

def fHere(i,j):
    if(way[i][j] == 'F'):return True
    return False

def showMyWay(txt):print(txt)

def go(i,j,went=''):
    if(can(i,j) and fHere(i,j)):showMyWay(went)
    else:
        if(ezpass(i,j)):
            # nine's algo :DDD
            way[i][j] = 'X' # Dont trash me 
            go(i,j+1,went + control[3])
            go(i,j-1,went + control[2])
            go(i+1,j,went + control[1])
            go(i-1,j,went + control[0])
            way[i][j] = ' ' # Get out
            
def get_chrline(i,txt):
    if(len(txt)==n):
        if('I' in txt):strpos[0],strpos[1] = i,txt.index('I')
        return txt

for i in range(m):way.append([j for j in get_chrline(i,input())])
go(strpos[0],strpos[1])