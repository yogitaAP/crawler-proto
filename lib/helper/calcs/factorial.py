# Define a procedure, factorial, that
# takes one number as its input
# and returns the factorial of
# that number.

def factorial(n):
    fact = 1
    while(n >= 1):
        fact = fact * n
        n = n - 1

    return fact




print factorial(0)
#>>> 24
#print factorial(5)
#>>> 120
#print factorial(6)
#>>> 720


