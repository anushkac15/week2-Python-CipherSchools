# for loop and tuple
mixed = (1,2,3,4.0)
for i in mixed:
    print(i)
# NOTE - You can use while loop too

# tuple with one element
nums = (1)
words = ('word')
print(type(nums))
print(type(words))
print(type(mixed))

nums = (1,)
words = ('word',)
print(type(nums))
print(type(words))

# tuple without parenthesis
guitars = 'yamaha', 'baton rouge', 'taylor'
print(type(guitars))

# tuple unpacking
guitarists = ('Maneli Jamal', 'Eddie van der Meer', 'Andrew Foy')
guitarist1, guitarist2, guitarist3 = (guitarists)
print(guitarist1)

# list inside tuple
favorites = ('southern magnolia',['Tokyo Ghoul Theme', 'landscape'])
favorites[1].pop()
favorites[1].append("we made it")
print(favorites)

# min(), max(), sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))