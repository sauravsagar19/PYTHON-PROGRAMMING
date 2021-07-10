"""n=int(input("enter number"))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return (n*factorial(n-1))
print(factorial(5))"""

# 2nd method
"""import math
def factorial(n):
    return(math.factorial(n))
z=int(input("enter the number"))
print(factorial(z))"""

#3rd method
def factorial(x):
    if x<0:
        return(-1)
    elif(x==0 or x==1):
        return(1)
    else:
        fact=1
        while x>1:
            fact=fact*x
            x=x-1
        return fact
print(factorial(5))
