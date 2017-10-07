##################################################
## Problem: predict.py
## Std: std09
## Name: Poon Shotateerawasu
## StudentId: 6010500109
##################################################
# You can edit the parameters in parenthesis ().
def predict(getData):
    if(type(getData) == list):
        for i in range(len(getData)):getData[i] = getData[i] * 200000 * (1.05**getData[i])
    else:getData = getData * 200000 * (1.05**getData)
    return getData

########## DON'T EDIT CODES BELOW ##########
print(predict(eval(input())))