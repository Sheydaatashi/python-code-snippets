a=int(input())
digit3=(a%10)
digit2=(a//10)%10
digit1=a//100

revers=digit3*100+digit2*10+digit1
print(revers*2)