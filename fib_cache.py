
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

for n in range(1,3010):
    print(n," : ", fibonacci(n))