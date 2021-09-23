'''the nth digit in the fibonacci sequence'''
def fibonacci(n):
    n = int(n)
    if n <= 0:
        print('error') 
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
n=input('which digit in the fibonacci sequence do you want to know?')
print(fibonacci(n))
        