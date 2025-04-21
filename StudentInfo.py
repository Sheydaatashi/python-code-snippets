NameLastname=input('enter your full name: ')
StudentNumber=input('enter your student number: ')

try:
    with open('StudentInfo.txt','w+') as file:
        file.write(f'name and last name:{NameLastname}/n')
        file.write(f'student number:{StudentNumber}')

except ValueError:
    print('enter a number!')

