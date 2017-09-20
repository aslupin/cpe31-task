def get_top(topostack,stack,stackii,stackiii):
  if(len(stack) != 0):
    topostack.append(stack.index(len(stack)-1))
  if(len(stackii) != 0): 
    topostack.append(stackii.index(len(stackii)-1))
  if(len(stackiii) != 0):
    topostack.append(stackiii.index(len(stackiii)-1))
  topostack.sort()
  return topostack
#  print(topostack)
 
def pocess_swapval(stack,stackii,stackiii):	
	print(" ") 

# var
topostack = list()
# input
num = int(input())
#stack = stackii = stackiii = list()
stack = list()
stackii = list()
stackiii = list()
# get data
data = num
for i in range(num): stack.append(num-i)
topostack = get_top(topostack,stack,stackii,stackiii)

# travel stack
print("stack : "+str(stack))
print("stack ii : "+str(stackii))
print("stack iii : "+str(stackiii))
print("top of stack : "+str(topostack))
