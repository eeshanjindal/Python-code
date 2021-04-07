a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a>b:
    if a>c:
        if a>d:
            print(f"Max = {a}")
        else:
            print(f"Max = {d}")
    else:
        if c>d:
            print(f"Max = {c}")
        else:
            print(f"Max = {d}")
else:
    if b>c:
        if b>d:
            print(f"Max = {b}")
        else:
            print(f"Max = {d}")
    else:
        if c>d:
            print(f"Max = {c}")
        else:
            print(f"Max = {d}")  
    