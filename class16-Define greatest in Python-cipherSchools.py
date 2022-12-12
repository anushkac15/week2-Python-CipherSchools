def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greatest(15,20,35))
print(greatest(123,467,88))