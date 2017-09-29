##################################################
## Problem: matrix_multiplication.py
## Std: std09
## Name: Poon Shotateerawasu
## StudentId: 6010500109
##################################################
def matrix_multiplication(a,b,c=list()):

	# Write your programme here.
    n=len(a);m=len(b[0])
    if(n==m):
        for i in range(n):
            c.append([])
            for j in range(m):
                temp = 0
                for k in range(m):
                    temp += (a[i][k] * b[k][j])
                c[i].append(temp)
        return c    
# Code further from this line must NOT be edited.
a = []
b = []
a_line_len = int(input())
for _ in range(a_line_len):
	a.append([int(x) for x in input().split()])
b_line_len = int(input())
for _ in range(b_line_len):
 	b.append([int(x) for x in input().split()])
print(matrix_multiplication(a,b))