movement = {"U":1,"R":1,"L":-1,"D":-1}
x = 0;y = 0;check = False
fly = input()
here_x = int(input())
here_y = int(input())
while(True):
    for i in fly:   
        if(i == 'U' or i == 'D'):y += movement[i]
        if(i == 'R' or i == 'L'):x += movement[i]
        if(x == here_x and y == here_y):check=True
    if(check):
        print('Y')
        break
    if((x < -10000000 or x > 10000000) and (y < -10000000 or y > 10000000)):
        print('N')
        break