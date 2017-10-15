import re

def fn1(name_list):
    # In Chiang Rai or Chiang Mai
    lis = []
    for s in name_list:
        if re.search(r' Chiang ',s):
            lis.append(s)
    return lis

def fn2(name_list):
    # Name begins with Kan
    lis = []
    for s in name_list:
        if re.search(r' Kan',s):
            continue
        if re.search(r'Kan',s):
            lis.append(s)
    return lis

def fn3(name_list):
    # Name ends with chai
    lis = []
    for s in name_list:
        if re.search(r'chai',s.split()[0]):
            lis.append(s)
    return lis

def fn4(name_list):
    # Doesn't use mobile phone
    lis = []
    for s in name_list:
        if re.search(r'08\d-\d\d\d-\d\d\d\d',s) or re.search(r'09\d-\d\d\d-\d\d\d\d',s):
            continue
        lis.append(s)
    lis.pop(0)
    return lis

def fn5(name_list):
    # Phone ends with odd number
    name_list.pop(0)
    lis = []
    for s in name_list:
        if int(s[len(s)-1])%2==1:
            lis.append(s)
    return lis

# Do not edit codes below.
name_list = open('contact_list.txt').read().strip().split('\n')
#name_list = open('/home/public/week_8/contact_list.txt').read().strip().split('\n')        
fn_list = [fn1, fn2, fn3, fn4, fn5]
n = int(input("Which function? (1-5): "))
fn = fn_list[n-1]
search_result = fn(name_list)
for result in search_result:
    print(result)