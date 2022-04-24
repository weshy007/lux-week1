import math

# This is a func that returns true if the num passed is a perfect square

def perfectSquare(num):
    square = int(math.sqrt(num))
    return square * square == num

''' 
To know a number belongs to the Fibonacci squence,
the number has to pass either of the formulas(luck of a better word).
Either one of (5*n*n + 4) or (5*n*n - 4) or BOTH
'''

def isFibonacci(x):
    # Returns true if x is a Fibonacci Number, else false
    return perfectSquare(5*x*x + 4) or perfectSquare(5*x*x - 4)


# Getting User's Input on the number they want to be checked
num = int(input("Enter any number: "))

# Conditional loop which will test the number on the functions initiated
if (isFibonacci(num) == True):
    print(num, 'is a Fibonacci Number')
else:
    print(num, 'is not a Fibonacci Number')