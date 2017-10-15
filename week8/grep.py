import re

def fn1(name_list,relist=[]):
    # In Chiang Rai or Chiang Mai
    for i in name_list:
        if(re.search(r' Chiang ',i)):relist.append(i)
    return relist

def fn2(name_list,relist=[]):
    # Name begins with Kan
    relist=[]
    for i in name_list:
        if(re.search(r'Kan',i.split()[0])):relist.append(i)
    return relist
def fn3(name_list,relist=[]):
    # Name ends with chai
    relist=[]
    for i in name_list:
        if(re.search(r'chai',i.split()[0])):relist.append(i)
    return relist
def fn4(name_list,relist=[]):
    # Doesn't use mobile phone
    relist=[]
    for i in name_list:
        if((not re.search(r'08\d-\d\d\d-\d\d\d\d',i)) and (not re.search(r'09\d-\d\d\d-\d\d\d\d',i))):relist.append(i)
    relist.pop(0)
    return relist

def fn5(name_list,relist=[]):
    # Phone ends with odd number
    relist=[]
    for i in name_list:
        if(re.search(r'\d',i[len(i)-1])):
            if(int(i[len(i)-1]) % 2 == 1):relist.append(i)
    return relist
# Do not edit codes below.
name_list = open('contact_list.txt').read().strip().split('\n')
fn_list = [fn1, fn2, fn3, fn4, fn5]
n = int(input("Which function? (1-5): "))
fn = fn_list[n-1]
search_result = fn(name_list)
for result in search_result:
    print(result)