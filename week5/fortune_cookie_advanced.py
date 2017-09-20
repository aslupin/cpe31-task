import threading
def left_threading(sum,data):
    for i in range(1,(len(data)+1)//2):
        if((str((sum - int(data[i-1]))) in data ) and ( data.index(str(sum - int(data[i-1]))) !=  i-1)):
            print(i,end=" ")
            exit
def right_threading(sum,data):
    for i in range((len(data)+1)//2,len(data)+1):
        if((str((sum - int(data[i-1]))) in data ) and ( data.index(str(sum - int(data[i-1]))) !=  i-1)):
            print(i,end=" ")
            exit

sum = int(input())
data = input().split(' ')
left_th = threading.Thread(name = 'left_threading',target=left_threading,args=(sum,data))
right_th = threading.Thread(name = 'right_threading',target=right_threading,args=(sum,data))
left_th.start()
right_th.start()
# sum = int(input())
# data = input().split(' ')
# for i in range(1,len(data)+1):
#     if((str((sum - int(data[i-1]))) in data ) and ( data.index(str(sum - int(data[i-1]))) !=  i-1)):
#         print(i,end=" ")

# # import math
# sum = int(input())
# min = [9999,0]   
# data = input().split(' ')
# dp_sum = list()
# for i in range(len(data)):
#     if(len(dp_sum) == 0):dp_sum.append(0 + int(data[i]))
#     else:dp_sum.append(int(data[i]) + dp_sum[i-1])
#     if(abs(sum - dp_sum[i]) < min[0]):min[0],min[1] = sum - dp_sum[i],i
#     if(min == 0):
#         if((sum - data[i]) in data != -1):print(data[i],(sum - data[i]) in data)
# # print(dp_sum)
# print(min[1])
# # print(sum - int(data[min[1]]))
# print(data[min[1]],sum - int(data[min[1]]))

    # print(data[i-1])
    # print(((sum - int(data[i-1])) in data ) )
    # print(data.index(sum - int(data[i-1])))
        