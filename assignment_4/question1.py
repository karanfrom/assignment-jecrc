# 1. Write a Python program to calculate the factorial of a non-negative integer entered by the user.

def factorial(n):
    count=1
    for  i in range(1,n+1):
        count*=i
    return count

a=int(input("enter the number of which you have to find the factorial:"))
print(factorial(a))
