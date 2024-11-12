def f(b,c):
    a=int(input("number a:"))
    if a>=0:
        if a> b and a>c:
            return a
        elif b>c:
            return b
        else:
            return c
    else:
        return -1
b=int(input("number b:"))
c=int(input("number c:"))
print(f(b,c))