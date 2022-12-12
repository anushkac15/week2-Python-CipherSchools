# min and max functions
numbers = [15,20,35]
print(min(numbers))
print(max(numbers))

def greatest_diff(l):
    return max(l) - min(l)
print(greatest_diff(numbers))