try:
    x=input('enter:')
except ValueError:
    print('value error!')
except ZeroDivisionError:
    print('Zero Division Error!')
except Exception:
    print('Exception!')