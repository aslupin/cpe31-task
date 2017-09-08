def initiationCheck(txt):
    if(txt == 'AUG'):return True
    else: return False
def terminationCheck(txt):
    ignore = ['UAA','UAG','UGA']
    if(txt in ignore):return True
    else: return False
def process(mRna,count_codon=1,codon=0,i=0,stopCodon=False,startCodon=False):
    while i < len(mRna):
            if(startCodon):
                if(mRna[i] == 'U' and count_codon==1):stopCodon = terminationCheck(mRna[i:i+3])
                if(stopCodon):
                    break
                count_codon += 1
                if(len(mRna) - i < 2):
                    codon += 1
                    break
                if(count_codon == 4):
                    codon += 1
                    count_codon = 1
            else:
                startCodon = initiationCheck(mRna[i:i+3])
                if(startCodon):i+=2
            i += 1
    print("Codon: {} \nFound stop codon: {}".format(codon,stopCodon))

mRna = str(input("Enter RNA: "))
if(input("Left side is (5' or 3'): ") == '3'):
    process(mRna[::-1])
else:process(mRna)
    
    
    
