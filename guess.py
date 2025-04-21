import random
import time
print('choose a number between 1 to 100:')
start=0
end=100
middle=(end+start)//2
guess=random.randint(1,100)
guessed=False
tryed=0
db=[]
try:
    with open('guess.txt','r')as file:
        lines=file.readlines()
        if lines:
            db=eval(lines[0].strip())
except:
    pass
start_time=time.time()
def save_file():
    with open('guess.txt','w')as file:
        file.write(str(db))
while guessed==False:
    number=int(input(f'if your number is {start} to {middle}:(type 1) and if your number is {middle} to {end}:(type 2) and if your number is the {middle}:(type 0) and if the number is the {start}:(type 3) and if the number is the {end}:(type 4)'))

    
    if number==0:
        end=middle
        middle=(start+end)//2
        tryed+=1
    elif number==1:
        start=middle
        middle=(start+end)//2
        tryed+=1
    elif number==2:
        guessed=True
        print(start)
        end_time=time.time()
        total_time=end_time-start_time
        try:
            shomareh=(db[-1][0])+1
        except:
            shomareh=1
        karbar=[shomareh,tryed,total_time]
        db.append(karbar)
        save_file()
    elif number==3:
        guessed=True
        print(middle)
        end_time=time.time()
        total_time=end_time-start_time
        try:
            shomareh=(db[-1][0])+1
        except:
            shomareh=1
        karbar=[shomareh,tryed,total_time]
        db.append(karbar)
        save_file()
    elif number==4:
        guessed=True
        print(end)
        end_time=time.time()
        total_time=end_time-start_time
        try:
            shomareh=(db[-1][0])+1
        except:
            shomareh=1
        karbar=[shomareh,tryed,total_time]
        db.append(karbar)
        save_file()