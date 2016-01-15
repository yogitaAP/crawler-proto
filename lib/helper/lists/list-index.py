# The procedure, find_element,
# that takes as its inputs a list
# and a value of any type, and
# returns the index of the first
# element in the input list that
# matches the value.

# If there is no matching element,
# return -1.

def find_element(nums, el):
    result = -1
    for e in nums:
        if e == el:
            result = nums.index(el)
            
    print result
        

def find_element_while(nums, el):
	i = 0
	while i < len(p):
		if p[i] == t:
			return i;
		i = i + 1
	return -1		

def find_element_for(nums, el):
	i = 0
	for e in p:
		if e == t:
			return i
		i = i + 1
	return -1

print find_element(['flower', 'petal', 'tree', 'grass'],'flower')
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1