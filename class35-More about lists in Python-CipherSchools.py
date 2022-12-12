# generate lists with range functions
# pass list to a function

numbers = list(range(1,11))
print(numbers)

numbers = list(range(1,21))
print(numbers)

# something more about pop method
numbers = list(range(1,11))
popped_itmes = numbers.pop()
print(numbers)
 
numbers = list(range(1,11))
print(numbers.pop())

# index method
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 5, 7, 8, 1]
print(numbers.index(1))
print(numbers.index(1, 3))
print(numbers.index(1, 11))
# print(numbers.index(1, 11, 14))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 5, 7, 8, 1]
def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))