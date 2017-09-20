import random
def checktxt(txt,mom):
    boxX="";boxO="";boxN="";txt_box = [mom[i] for i in range(len(mom))]
    for i in range(len(txt)):
        if(txt[i] == txt_box[i]):
            boxX += "X"
            txt_box[i] = 'X'
        elif(txt[i] in txt_box):boxO += "O"
    strplus= 4 - (len(boxX) + len(boxO))
    if(len(boxX) + len(boxO) < 4):boxN = "-" * strplus
    print(boxX+boxO+boxN)
    if(boxX+boxO+boxN == "XXXX"):return False
    else:return True

played=0;GO=True
txt_mom = input('#')
# txt_mom = str(random.randint(0,9999)).rjust(4,'0')
while GO:
    played += 1
    GO = checktxt(input("Guess : "),txt_mom)
print(f"You win the game after {played} guess!!!\nThe number was {txt_mom}")