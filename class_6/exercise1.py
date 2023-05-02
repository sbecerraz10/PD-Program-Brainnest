import math
def generate_primes(n):
    for x in range(2, n + 1):
        a=2
        isPrime = True
        while a<=math.sqrt(x):
            if x%a<1:
                isPrime = False
            a=a+1
        if isPrime: yield x

for y in generate_primes(10):
    print(y)