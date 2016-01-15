# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

def find_element_while(p, t):
	i = 0
	while i < len(p):
		if p[i] == t:
			return i;
		i = i + 1
	return -1	


def union(p,q):
    for e in q:
        index = find_element_while(p,e)
        if index == -1:
            p.append(e)
            


# To test, uncomment all lines 
# below except those beginning with >>>.

a = [1,2,3]
b = [2,4,6]
union(a,b)
print a 
#>>> [1,2,3,4,6]
print b
#>>> [2,4,6]






