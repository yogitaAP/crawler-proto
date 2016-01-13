# Procedure, replace_spy,
# that takes as its input a list of
# three numbers, and modifies the
# value of the third element in the
# input list to be one more than its
# previous value.


spy = [0,0,7]

def replace_spy(spy):
	spy[2] = spy[2] + 1

#tests

#expected output = 8
replace_spy(spy)
print spy

#expected output = 4
spy = [1,2,3]

replace_spy(spy)
print spy

