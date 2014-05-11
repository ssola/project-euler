'''
Problem 10
https://projecteuler.net/problem=10
'''
import math

def isPrime(num):
    if num <= 1:
        return False

    if num == 2:
        return True

    if num%2 == 0:
        return False

    root = int(math.sqrt(num))+1

    for i in xrange(3, root, 2):
        if num % i == 0:
            return False

    return True

summation = 2
index = 1

while index < 2000000:
    index += 2
    if(isPrime(index)):
        summation += index
        print index, summation

print summation