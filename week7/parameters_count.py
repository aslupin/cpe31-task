def parameters_count(*argv):
    return len(argv)
	# Write your `parameters_count(n)` here

########## DON'T EDIT CODES BELOW ##########

n = int(input())

if n == 1:
	print(parameters_count(1))
elif n == 2:
	print(parameters_count(1,2,3))
elif n == 3:
	print(parameters_count(1,2,3,4,5))
elif n == 4:
	print(parameters_count([1,2,3]))
elif n == 5:
	print(parameters_count())