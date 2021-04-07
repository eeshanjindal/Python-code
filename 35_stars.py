def print_star_triangle(n):
    for i in range(n):
        print("*",end="") 
    print()  

"""
\n = new line character
\t =tab
"""
def main ():
    for i in range(10):
        print_star_triangle(i+1)

main()