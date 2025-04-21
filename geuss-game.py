import random
a=1
b=99
hads=random.randint(a,b)
print(hads)
javab=input('bigger,smaller or true?[b/s/t] ')
while javab!='t':
    if javab=='b':
        a=hads
        hads=(random.randint(a,b))
        print(hads)
        javab=input('bigger,smaller or true?[b/s/t]')

    else:
        b=hads
        hads=(random.randint(a,b))
        print(hads)
        javab=input('bigger,smaller,or true?[b/s/t] ')

print('I guess it!')
        
        