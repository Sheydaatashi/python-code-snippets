import random
random.seed
i=[]
for dice in range(0,10000):
    dice=random.randrange(1,7)
    i.append(dice)
print(i)