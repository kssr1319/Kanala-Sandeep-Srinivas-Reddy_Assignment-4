# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

# sample input: 10
# sample output: 35

a = int(input("Enter any number: "))
b = lambda x: x + 25
print(b(a))