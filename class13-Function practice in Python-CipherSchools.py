#functions practice

def last_char(name):
    return name[-1]
print(last_char("Anushka"))
# last_char(7) #error

def odd_even(num):
    if num%2 == 0:
        return "even"   
    else:
        return"odd"
print(odd_even(15))
print(odd_even(20))

def odd_even(num):
    if num%2 == 0:
        return "even"   
    return"odd"
print(odd_even(15))
print(odd_even(20))

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
print(is_even(20))
print(is_even(15))

def is_even(num):
    if num%2==0:
        return True
    return False
print(is_even(20))
print(is_even(15))

def is_even(num):
    return num%2 == 0 # True
print(is_even(15))
print(is_even(20))

def song():
    return "Happy Birthday song"
print(song())