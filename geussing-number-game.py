import random
javab=random.randint(1,99)

hads=int(input('what is your hads? '))

while hads!=javab:
    if hads>javab:
        print('mine is smaller!')
    else:
        print('mine in larger!')
    hads=int(input('what is your hads? '))

print('wooow!you rock!!')
