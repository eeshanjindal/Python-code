n = int(input("Enter n: "))
def star_triangle(n):
    t = 0
    for i in range(n,0,-1):
        for j in range(0,t):
            print(end=" ")
        t=t+1

        for j in range(i):
            print("* ",end="")
        print("\r")
    

star_triangle(n)
