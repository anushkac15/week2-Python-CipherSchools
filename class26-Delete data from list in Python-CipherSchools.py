# common methods to delete data from list

# pop method
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']
fruits.pop()
print(fruits)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']
fruits.pop(1)
print(fruits)

# delete operator
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']
del fruits[1]
print(fruits)

# remove method
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi']
fruits.remove('banana')
print(fruits)

fruits = ['orange', 'apple', 'pear', 'banana', 'apple', 'kiwi']
fruits.remove('banana')
print(fruits)

# append, extend, insert (for add data)
# pop, remove, delete (for delete data)