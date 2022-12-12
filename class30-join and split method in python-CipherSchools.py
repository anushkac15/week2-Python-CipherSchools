# split method
# convert string to list

user_info = 'Anushka  18'.split()
print(user_info)

user_info = 'Anushka,18'.split(',')
print(user_info)

name, age = 'Anushka,18'.split(',')
print(name)
print(age)

name, age = input("Enter your name and age : ").split(',')
print(name)
print(age)

# join method
user_info = ['Anushka', '18']
print(','.join(user_info))