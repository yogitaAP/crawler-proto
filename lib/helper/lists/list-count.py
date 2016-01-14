# This procedure takes as its input a list of strings,
# and returns a number that is a count
# of the number of elements in the input
# list that start with the uppercase 
# letter 'U'.

def measure_udacity(strs):
	uCount = 0
	for string in strs:
		if(string[0] == 'U'):
			uCount += 1
	return uCount

#test cases

print  measure_udacity(['Dave','Sebastian','Katy'])

print  measure_udacity(['Umika','Umberto'])
