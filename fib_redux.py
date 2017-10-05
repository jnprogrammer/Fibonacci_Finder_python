from functools import lru_cache

@lru_cache(maxsize = 30000)
def fibonacci(n):

    #checking for correct data type.
    #If not recevied the user will be alerted in the error message

    if type(n) != int:
        raise TypeError("n Must be a positive Int, Silly humans")
    if n < 1:
        raise ValueError("n must be a positive Int, So human")

    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for n in range(1,185):
    print(n," : ", fibonacci(n))
    
    #this shows that the squence is close to the golden ratio
for n in range(1,2000):
    print(fibonacci(n+1) / fibonacci(n))

