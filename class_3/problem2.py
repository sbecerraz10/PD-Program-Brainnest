import math ##math.pow(2)


def main():
    message = "Enter a number: "
    n = int(input(message))
    generate_primes(n)
    

def generate_primes(n):
    for x in range(2, n + 1):
        a=2
        isPrime = True
        while a<=math.sqrt(x):
            if x%a<1:
                isPrime = False
            a=a+1
        
        if isPrime: print(x, end= " ")
        


if __name__ == "__main__":
    main()