# Ex6
a = input('Please enter a:')
b = input('Please enter b:')
c = input('Please enter c:')
sn = (b**2) - (4*a*c)
def quadratic(a,b,c):
    x1 = (-b+sn**(1/2)/2/a)
    x2 = (-b-sn**(1/2)/2/a)
    print(a,b,c)
    return(a,b,c)