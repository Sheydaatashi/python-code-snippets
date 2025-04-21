while True:
    try:
        file=open('example.txt','r')
        break
    except FileNotFoundError:
        print('File doesnt exist')
        break
    

    finally:
        print('Do somthing anyway!')
        break