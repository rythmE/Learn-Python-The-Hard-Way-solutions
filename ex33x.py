c = raw_input("Please enter the ceil:")
d = raw_input("Please enter the delta:")

def numb(ceil, delta):
	i = 0
	numbers = []
	
	while i < ceil:
		print "At the top i is: %d" % i
		numbers.append(i)

		i = i + delta
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
		
	print "The numbers: "

	for num in numbers:
		print num

	return numbers

print "Finally, we got the number list: "
print numb(int(c), int(d))