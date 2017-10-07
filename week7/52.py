# Please do not forget to `genheader`

def satu_48(n,out = 0):
	# Write your `satu_48(n)` here
    txt_heap = str(n)
    if(len(txt_heap) == 0):return out
    else:
        if(txt_heap[0] == '5' or txt_heap[0] == '2'):out += 1
        return satu_48(txt_heap[1::],out)

########## DON'T EDIT CODES BELOW ##########
print(satu_48(int(input())))