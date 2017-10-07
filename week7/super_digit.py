def super_digit(txt):
    def cut(txt):
        if(len(txt)==1):return int(txt[0])
        else:return int(cut(txt[1:])) + int(txt[0])
    txt = str(cut(txt))
    if(len(txt) == 1):return txt
    else:return super_digit(txt)
print(super_digit(input()))