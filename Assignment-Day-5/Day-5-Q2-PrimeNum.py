# Make a Function for prime numbers and use Filter to filter out all the prime numbers from 1-2500
def prime(n):
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            return False
    else:
        return True


print(list(filter(prime, range(1, 2501))))
