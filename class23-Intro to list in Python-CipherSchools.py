# data structures
# list ---> this chapter
# ordered collection of items
# you can store anything in lists : int, float, String

numbers = [1, 2, 3, 4]
print(numbers)

words = ["word1", "word2", "word3"]
print(words)

mixed = [1, 2, 3, 4, "five", "six", 6.5, None]
print(mixed)

numbers = [1, 2, 3, 4]
print(numbers[1])

words = ["word1", "word2", "word3"]
print(words[:2])

mixed = [1, 2, 3, 4, "five", "six", 6.5, None]
print(mixed[-1])

mixed[1] = "two"
print(mixed)

mixed[1:] = "two"
print(mixed)

mixed[1:] = ['three', 'four']
print(mixed)