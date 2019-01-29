"""
Write a program to capture any filename from the keyboard and display its filename and extension separately
Enter any filename : hello.py

Filename : hello
Extension : py
"""

filename = input("Enter the Filename with extention:")

data = (filename.split('.'))

print("Filename  :", data[0])
print("extention :", data[1])


"""
Write a program to capture two numbers separately from the keyboard and display its sum
Enter first number : 10
Enter second number : 20
Sum of the number : 30
"""


vala = int(input("Enter the first no.  :"))
valb = int(input("Enter the second no. :"))

total = sum([vala, valb])

print("Total sum of given numbers is :", total)


