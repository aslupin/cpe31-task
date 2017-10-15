def ch_sp_mod(key,f,ans=[],save=None):
    if(not key):return False
    ans.append(key[f.index(max(f))])
    # print('first',key,f)
    key.pop(f.index(max(f)));save = f.pop(f.index(max(f)))
    # print('first',key,f)
    if(len(key) > 0):
        while(max(f) == save):
            if(not (key[f.index(max(f))] in ans)):ans.append(key[f.index(max(f))])
            key.pop(f.index(max(f)));f.pop(f.index(max(f)))
            if(not f or not key):break
    # print(ans)
    if(len(ans) <= 2):
        if(len(ans) == 1):print(ans[0])
        else:print(ans[0],ans[1])
        # for i in ans:print(i,end=" ")
        return True
    else:return False

key=[];f=[];i=0
txt = input()
while(txt != 'end'):
    if(not key):
        key.append(txt)
        f.append(1)
        i+=1
    else:
        if(txt == key[i-1]):f[i-1] += 1
        else:
            key.append(txt)
            f.append(1)
            i+=1
    # print(key,f)
    txt = input()
if(ch_sp_mod(key,f)):
    pass
else:print('Don’t have mode')
