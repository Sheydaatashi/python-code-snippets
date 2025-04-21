weight=int(input('Please enter your weight:'))
height=int(input('Please enter your height:'))
h=height/100
bmi=weight/h**2
if bmi>18.5:
    print('underweight!')
if 18.5<bmi<24.9:
    print('normal.')
if bmi<25:
    print('overweight!')