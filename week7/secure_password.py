# 32 - 47 hyperchar
# 48 - 57 number
# 58 - 64 hyperchar
# 65 - 90 char-bigger
# 91 - 96 hyperchar
# 97 - 122 char-litle
# 123 - 126 hyperchar

def ch_hyperchar(order):
    if(order >= 32 and order <=47): return True
    if(order >= 58 and order <=64): return True
    if(order >= 91 and order <=96): return True
    if(order >= 123 and order <=126): return True
    return False

def ch_number(order):
    if(order >=48 and order <= 57): return True
    return False

def ch_bigchar(order):
    if(order >= 65 and order <= 90): return True
    return False

def ch_litchar(order):
    if(order >= 97 and order <= 122): return True
    return False

def ch_hexlen(txt):
    if(len(txt) >= 8): return True
    return False

def ch_fourlen(txt):
    if(len(txt) >= 4): return True
    return False

def secure_pass(password,chbig=False,chlit=False,chnum=False,chhy=False):
    if(ch_hexlen(password)):
        for i in password:
            i = ord(i)
            if(ch_bigchar(i)):chbig = True
            if(ch_litchar(i)):chlit = True
            if(ch_number(i)):chnum = True
            if(ch_hyperchar(i)):chhy = True
    if(chbig and chlit and chnum and chhy): return True
    else: return False

def ch_each_word(password):
    words = password.split()
    if(len(words) < 4): return False
    else:
        for i in words:
            if(len(i) < 5): return False
        return True

def good_pass(password,chbig=False,chlit=False,chnum=False,chhy=False):
    if(ch_each_word(password)): return True
    return False

def main_secure(password):
    if(secure_pass(password)): return 'secure password'
    elif(good_pass(password)): return 'good password'
    else:return 'bad password'
        

print(main_secure(input()))