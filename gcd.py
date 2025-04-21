def gcd(x,y):
    while y!=0:
        i=x%y
        x=y
        y=i
    return x

gcd=gcd(18,12)

print('The graetest common divisor of 18 and 12 is: ',gcd)