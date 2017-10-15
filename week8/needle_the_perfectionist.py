def getF(txt):
    hmap={}
    for i in txt:
        if(i in hmap):
            hmap[i] += 1
        else:hmap[i] = 1
    return hmap

def travel_F(F):
    ch_promotion = True;can = F[0]
    for i in F:
        if(i != can):return False
    return True

def pef(txt):
    for i in range(-1,len(txt)):
        if(i==-1):txt_tmp = txt
        else:txt_tmp = txt[:i] + txt[i+1:]
        hach={};F=[]
        hach = getF(sorted(list(txt_tmp)))
        F = list(hach.values())
        if(travel_F(F)):return True
    return False

if(pef(input())):print('Perfect')
else:print('Imperfect')
