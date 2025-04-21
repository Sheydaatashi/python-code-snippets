import random
RandS=input('type something: ')
def RandomString():
    test=''
    for elements in range(0,len(RandS)):
        my_list=['!','@','#','*','%','$','%','&',]
        test+=random.choice(my_list)
        
    print(test)

    

RandomString()