# Write a Python program to square the elements of a list using map() function.

#Sample List: [4, 5, 2, 9]
#Square the elements of the list:
#[16, 25, 4, 81]

lst1 = []
r = int(input("Enter range:"))
for r in range(0, r):
    a = int(input())
    lst1.append(a)
result = map(lambda n: n * n, lst1)
print(list(result))