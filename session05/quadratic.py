# Ex6
def quadratic(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    sn = (b**2) - (4*a*c)
    x1 = (-b+sn**(1/2)/2/a)
    x2 = (-b-sn**(1/2)/2/a)
    return(x1,x2)
quadratic(1,2,1)

