
"""
# Recursion
The most fundamental concept of the Data Structures. If you know this, you know data structures. 
If you don't know this, then you don't know DSA becasuse DSA is based on recursion. 

A basic model to implement recusion. A function calling itself within a function. This reduces the implementation of looping.

Following is the implementation of the famous "***Fibonacci Series***"
"""

def fib(n):
  series = []
  if n == 0 or n == 1:
    return n
  else:
    return fib(n-2) + fib(n-1)

if __name__ == "__main__":
  n = 8
  for i in range(n):
    print(fib(i))