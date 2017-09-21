
#fib_cache = {}

def fibonacci(n):
  #  if n in fib_cache:
   #     return fib_cache[n]
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,110):
    print(n," : ", fibonacci(n))