#Assignment
def print_sum(n):
    sum =((n *(n+1))/2)**2
    print(f"Sum of cubes of first {n} Natural numbers = {sum}")

def main():
    n = int(input("Enter a number: "))
    print_sum(n)

main()