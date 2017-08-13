def comp_one(p,q):return not(ifso(p,not q))
def comp_two(r,s):return r or (not s)
def ifso(a,b):
  if(a == True and b == False):return False
  else:return True

def ans(p,q,r,s):return not(comp_one(p,q) != comp_two(r,s))

sqbool = list() # p q r s = 0 1 2 3
for i in range(4):
  boow = input()
  if boow == str(True):sqbool.append(True) 
  else:sqbool.append(False)
print("[~[%s -> ~ %s]<->[%s v ~%s]] -> ~%s == %s"%(sqbool[0],sqbool[1],sqbool[2],sqbool[3],sqbool[3],ifso(ans(sqbool[0],sqbool[1],sqbool[2],sqbool[3]),not sqbool[3])))
