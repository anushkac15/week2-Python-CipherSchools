# default parameters

def user_info(first_name, last_name, age):
    print(f"your first name is {first_name} ")
    print(f"your last name is {last_name} ")
    print(f"your age is {age} ")
user_info('Anushka', 'Gupta', 18)

def user_info(first_name, last_name, age = 18):
    print(f"your first name is {first_name} ")
    print(f"your last name is {last_name} ")
    print(f"your age is {age} ")
user_info('Anushka', 'Gupta')

def user_info(first_name, last_name, age = None):
    print(f"your first name is {first_name} ")
    print(f"your last name is {last_name} ")
    print(f"your age is {age} ")
user_info('Anushka', 'Gupta', 18)

def user_info(first_name, last_name = 'unknown', age = 'None'):
    print(f"your first name is {first_name} ")
    print(f"your last name is {last_name} ")
    print(f"your age is {age} ")
user_info('Anushka')

# def user_info(first_name, last_name = 'unknown', age): #error bcz we can only make last parameter default
#     print(f"your first name is {first_name} ")
#     print(f"your last name is {last_name} ")
#     print(f"your age is {age} ")
# user_info('Anushka', 18)

def user_info(first_name = 'unknown', last_name = 'unknown', age = 'None'):
    print(f"your first name is {first_name} ")
    print(f"your last name is {last_name} ")
    print(f"your age is {age} ")
user_info()