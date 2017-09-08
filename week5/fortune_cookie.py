sum = int(input())
n = input().split(' ')
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if(int(n[i]) + int(n[j]) == sum):
            print(i+1,j+1)
            exit()