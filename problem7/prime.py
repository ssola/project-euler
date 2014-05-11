'''
Problem 7
https://projecteuler.net/problem=7
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

numChecked = 0
index = 0

while numChecked < 10001:
    index += 1
    if(isPrime(index)):
        numChecked += 1
        print index, numChecked