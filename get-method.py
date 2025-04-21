string='Hi bobby is here and testing python for fun'

counter=dict()

for letter in string:
    counter[letter]=counter.get(letter,0)+1
    
for this_one in list(counter.keys()):
    print('%s appeared %s times'%(this_one,counter[this_one]))