string='hi bobby is here and testing python for fun'

counter=dict()

for letter in string:
    print(letter)
    if letter in counter:
        counter[letter]+=1
    else:
        counter[letter]=1
    
    print(letter,counter)