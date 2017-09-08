def bye():
    exit("Error: Wrong input")

headTail = {"t":0,"h":0}
txt = input().lower()
for i in txt:
    if(not (i in headTail)):bye()
    else:headTail[i] += 1
print("H: {:.2f}%".format(( headTail["h"] / (headTail["t"] + headTail["h"]))*100))
print("T: {:.2f}%".format(( headTail["t"] / (headTail["t"] + headTail["h"]))*100))