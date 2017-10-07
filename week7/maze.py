mapie = list()
walk = ['U','D','L','R']
pos = [[0,0],[0,0]]
m,n = map(int,input().split())

def out_map(i,j):
    if(i < 0 or i >= m):return False
    if(j < 0 or j >= n):return False
    else:return True

def gogo(i,j,ans=''):
    # if(i == pos[1][0] and j == pos[1][1]):
    if(mapie[i][j] == 'F'):
        print(ans)
        walker(pos[0][0],pos[0][1])
    if(out_map(i,j+1) and (mapie[i][j+1] == ' ' or mapie[i][j+1] == 'F')): #R
        if(mapie[i][j+1] != 'F'):mapie[i][j+1] = 'X'
        ans += walk[3]
        gogo(i,j+1,ans)
    if(out_map(i,j-1) and (mapie[i][j-1] == ' ' or mapie[i][j-1] == 'F')): #L
        if(mapie[i][j-1] != 'F'):mapie[i][j-1] = 'X'
        ans += walk[2]
        gogo(i,j-1,ans)
    if(out_map(i+1,j) and (mapie[i+1][j] == ' ' or mapie[i+1][j] == 'F')): #U
        if(mapie[i+1][j] != 'F'):mapie[i+1][j] = 'X'
        ans += walk[1]
        gogo(i+1,j,ans)
    if(out_map(i-1,j) and (mapie[i-1][j] == ' ' or mapie[i-1][j] == 'F')): #D
        if(mapie[i-1][j] != 'F'):mapie[i-1][j] = 'X'
        ans += walk[2]
        gogo(i-1,j,ans)
    else:walker(pos[0][0],pos[0][1])
def ch_cantwalk(i = pos[0][0],j = pos[0][1]):
    if(out_map(i,j+1) and (mapie[i][j+1] == ' ' or mapie[i][j+1] == 'F')):return 3
    if(out_map(i,j-1) and (mapie[i][j-1] == ' ' or mapie[i][j-1] == 'F')):return 2
    if(out_map(i+1,j) and (mapie[i+1][j] == ' ' or mapie[i+1][j] == 'F')):return 1
    if(out_map(i-1,j) and (mapie[i-1][j] == ' ' or mapie[i-1][j] == 'F')):return 0
    else:return -1
        
def walker(i,j):
    if(n == 1 or m == 1):
        print(walk[ch_cantwalk()])
        exit()
    if(ch_cantwalk() != -1):gogo(i,j)
    else:exit()

def get_chrline(i,txt):
    if(len(txt)==n):
        if('I' in txt):pos[0][0],pos[0][1] = i,txt.index('I')
        if('F' in txt):pos[1][0],pos[1][1] = i,txt.index('F')
        return txt

for i in range(m):mapie.append([j for j in get_chrline(i,input())])
walker(pos[0][0],pos[0][1])
