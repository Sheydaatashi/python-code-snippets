l=[]
a=0
while a<4:
    numbers=input('enter a number: ')
    l.append(numbers)
    a=a+1
    
    

print('how do you want to sort your list? 1.small to big  2.big to small.')
user=input('1 or 2: ')

if user=='1':
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and l[j]>key:
            l[j+1]=l[j]
            j-=1
            l[j+1]=key
    print(l)

if user=='2':
    for i in range(1,len(l)):
        key=l[i]
        j=i-1
        while j>=0 and l[j]<key:
            l[j+1]=l[j]
            j-=1
            l[j+1]=key
    print(l)


    