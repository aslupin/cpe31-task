def getchr(plus,txt,it=97):
    if(txt.isupper()):it=65
    tmp = ord(txt) - it # 0-25 input
    tmp = (tmp+plus)%26 # 0-25 ans
    return chr(tmp + it)
plus = int(input())
txt = input()
print(getchr(plus,txt))