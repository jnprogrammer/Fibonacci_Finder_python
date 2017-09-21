import sys

fib_cache = {}
# this dictionary is to cache values to prevent slowdown from recursive calls
# this use of dictionary to prevent redundent computation is an example of Memoization
def fibonacci(n):
    if n in fib_cache:
       return fib_cache[n]
    #Normal fib sequence
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fib_cache[n] = value
    return value
# this doesn't work yet, it must take a command-line argument as the number to find in the fib sequence
n = sys.argv[1]
n = int(n)

if type(n) != int:
    raise TypeError("Argument must be a Positive INT")
if n < 1:
    raise ValueError("Argument must be a Positive INT")
i = 0
while True:
    print(n," : ", fibonacci(n))
    i = i + 1
    if(i > n):
        break