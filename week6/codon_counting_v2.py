

rna = input("Enter RNA:\n")
if(input("Left side is (5' or 3'): ") == '3'):process(rna[::-1])
else:process(rna)