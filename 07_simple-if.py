age = input("Enter you age: ")
name = input("Enter you Name: ")

age=int(age)

if age >= 18:
    print(f"Hello {name} you are eligible to vote.")

print("Thank you.")

"""
python 07_simple-if.py
Enter you age: 56
Enter you Name: jj
Hello jj you are 56 years old.
Thank you.

python 07_simple-if.py
Enter you age: 11
Enter you Name: gg
Thank you.
"""