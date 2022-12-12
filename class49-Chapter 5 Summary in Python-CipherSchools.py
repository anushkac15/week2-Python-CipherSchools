def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print('you cannot divide a number by zero')
print(divide(10,0))

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
print(divide(10,0))

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print(err)
print(divide(10,'2'))

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as err:
        print("numbers must be int or floats")
    except:
        print("unexpected error")
print(divide(10,'2'))