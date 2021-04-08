#Assignment
def simple_interest(p,n,r):
    si = p*n*r/100
    print(f"Interest for principal {p} at a rate {r} and for a time {n} is {si}")

def main():
    p = int(input("Enter p: "))
    r = int(input("Enter r: "))
    n = int(input("Enter n: "))
    simple_interest(p,n,r)

main()