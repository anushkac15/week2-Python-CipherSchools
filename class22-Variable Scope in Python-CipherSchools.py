# sope

x = 5 # global variables
def func():
    x = 7 # local variables
    return x
print(func())
print(x)

x = 5 # global variables
def func():
    global x
    x = 7 # local variables
    return x
print(func())
print(x)

x = 5 # global variables
def func():
    global x
    x = 7 # local variables
    return x
print(x)
print(func())
print(x)