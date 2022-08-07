# Write a Python program to triple all numbers of a given list of integers. Use Python map.

#sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]

lst1 = []
r = int(input("Enter range:"))
for r in range(0, r):
    a = int(input())
    lst1.append(a)
def add(n):
    return n*3
result = map(add,lst1)
print(list(result))