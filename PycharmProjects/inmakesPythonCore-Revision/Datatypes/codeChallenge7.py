"""
List out all the even numbers from 2 to 222 using lists in Python.
List out all the odd numbers from 3 to 99 using lists in Python
"""

even = [i for i in range(2, 223) if i % 2 == 0]
print("Even numbers:", even, end=" ")

odd = [j for j in range(3, 100) if j % 2 == 1]
print("\nOdd numbers: ", odd, end=" ")
