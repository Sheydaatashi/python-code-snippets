def divisor(n):
    for i in range(1, number):
     if number % i == 0:
        print(i)

number = int(input('Enter your number: '))
divisor(number)
print(number)