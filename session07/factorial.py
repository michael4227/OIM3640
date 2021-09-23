def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("please enter a number for factorial computting:"))
print(factorial(n))
