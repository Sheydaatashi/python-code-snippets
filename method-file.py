with open('StudentNumber.txt','r+') as file:
    file.write('02044022:mona')
    file.seek(9)
    print(file.tell())
    print(file.readline())
    file.close()
    