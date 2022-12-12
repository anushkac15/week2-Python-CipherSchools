# # practice for loop
# # ask user name and count each character
# "Anushka Gupta"
# A : 1
# n : 1
# u : 2
# s : 1
# h : 1
# k : 1
# a : 2
#   : 1
# g : 1
# p : 1
# t : 1

name=input("Enter your name: ")
temp=""
for i in range(0,len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]
