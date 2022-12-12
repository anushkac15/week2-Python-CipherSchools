# list inside list

matrix = [[1,2,3], [4,5,6], [7,8,9]] # 2d list (when list inside list)
# 3 items ---> 3 list
print(matrix[0])
print(matrix[1])
print(matrix[2])

matrix = [[1,2,3], [4,5,6], [7,8,9]]
for sublist in matrix:
    for i in sublist:
        print(i)

matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(matrix[1][1])
print(matrix[2][0])

# type function
s = "string"
print(type(s))
print(type(matrix))