def print_line(n):
    for i in range(n):
        print("_",end="") 
    print()  

"""
\n = new line character
\t =tab
"""
def main ():
    for i in range(10):
        print_line(i+1)

main()