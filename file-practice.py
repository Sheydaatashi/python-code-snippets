userpass=[]

username=input('Please enter your username: ')
password=input('Please enter your password: ')

userpass.append(username)
userpass.append(password)
 


with open('file.txt','r') as f:
    for lines in f.readlines():
        u,p=lines.split()
        if u =="['"+username+"',":
            #print("Erorr")
            raise Exception('this username already exist')


file=open('file.txt','a')
file.write(f'{userpass}\n')
