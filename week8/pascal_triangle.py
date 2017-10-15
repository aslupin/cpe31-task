def pascal_triangle(row, col,table=[[1]]):
    
    for i in range(1,row+1):
        table.append([1])
        for j in range(1,i+1):
            if(j == i):table[i].append(1)       
            else:table[i].append(table[i-1][j] + table[i-1][j-1])
    return table[row][col]            
    
    
print(pascal_triangle(int(input()),int(input())))