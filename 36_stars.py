def print_star_triangle(n):
    for i in range(n):
        print("*",end="") 
    print()  

"""
\n = new line character
\t =tab
"""
def main ():
    for i in range(5,0,-1):
        print_star_triangle(i)

main()