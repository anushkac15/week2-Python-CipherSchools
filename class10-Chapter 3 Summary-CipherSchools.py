# if statement
name = "Anushka"
if name == "Anushka":
    print("you are Anushka")
else:
    print("you are not Anushka")

name = "Anushka"
if name == "anushka":
    print("you are Anushka")
else:
    print("you are not Anushka")

name = "Anushka"
if name == "Anushka" or name == "anushka":
    print("you are Anushka")
else:
    print("you are not Anushka")

name = input("Enetr your name : ")
if name == "Anushka" or name == "anushka":
    print("you are Anushka")
elif name == "Sizuka" or name == "sizuka":
    print("you are Sizuka")
else:
    print("you are not Anushka or Sizuka")

# while loop
i = 0
while i < 10:
    print("Hello World")
    i += 1

i = 1
while i <= 10:
    print("Hello World")
    i += 1

i = 1
while i <= 10:
    print(i)
    i += 1

i = 0
while i < 10:
    print(i)
    i += 1

# for loop
for i in range(1,11):
    print(i)

for i in range(1,11,2):
    print(i)

# break keyword
for i in range(1,11):
    if i == 5:
        break
    print(i)

# continue keyword
for i in range(1,11):
    if i == 5:
        continue
    print(i)

# for loop in string
for i in "Anushka":
    print(i)