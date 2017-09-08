def bfine(var_txt,sub_txt):
    for i in range(len(var_txt)):
        if(var_txt[i] == sub_txt[0] and len(var_txt) - i >= len(sub_txt) and var_txt[i:i+len(sub_txt)] == sub_txt):return True
    return False
def nlove(love,n=0):
    for i in love:
        if(i):n+=1
    return n

lovena = list()
for i in range(5):lovena.append(bfine(input().lower(),'somrak'))
if(lovena[0] and lovena[1] and lovena[2]):print('Love Love Somsri\n"somrak" :: {} sentences'.format(nlove(lovena)))
elif(lovena[1] and lovena[2] and lovena[3]):print('Love Love Somsri\n"somrak" :: {} sentences'.format(nlove(lovena)))
elif(lovena[3] and lovena[4] and lovena[5]):print('Love Love Somsri\n"somrak" :: {} sentences'.format(nlove(lovena)))
else:print('Mai rak mai tong ma care\n"somrak" :: {} sentences'.format(nlove(lovena)))