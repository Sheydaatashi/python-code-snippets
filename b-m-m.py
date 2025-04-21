def bmm(x,y):
    while y!=0:
        remainder=x%y
        x=y
        y=remainder 
    return x

print(bmm)