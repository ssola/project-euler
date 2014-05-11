'''
Problem 25
1000-digit Fibonacci number
https://projecteuler.net/problem=25
'''

def fib(n):
    fibValues = [0,1]
    for i in xrange(2,n+1):
        fibValues.append(fibValues[i-1] + fibValues[i-2])
    return fibValues[n]

currentValue = 0
index = 0

while len(str(currentValue)) < 1000:
    index += 1
    currentValue = fib(index)

print index