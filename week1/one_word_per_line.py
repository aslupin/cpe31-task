## Problem: one_word_per_line.py
## Std: std09
## Name: Poon Shotateerawasu
## StudentId: 6010500109
##################################################
txt = input()
#print(str(txt.replace(" ","\n")))
for i in txt:
    if(i == ' ' and  i != txt[len(txt)-1]):
        print('\n')
    else:    
        print(i,end = "")
