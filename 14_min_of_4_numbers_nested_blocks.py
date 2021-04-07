#Assignment
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a<b:
    if a<c:
        if a<d:
            print(f"Min = {a}")
        else:
            print(f"Min = {d}")
    else:
        if c<d:
            print(f"Min = {c}")
        else:
            print(f"Min = {d}")
else:
    if b<c:
        if b<d:
            print(f"Min = {b}")
        else:
            print(f"Min = {d}")
    else:
        if c<d:
            print(f"Min = {c}")
        else:
            print(f"Min = {d}")  
    