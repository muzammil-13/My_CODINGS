"""
Write Python code which Accept the student name and in turn
returns their respective Mark. Make sure to use dictionaries to store
student name and their respective mark. The dictionary should
include at least 7 elements
"""
students = {
    "appu": 80,
    "akku": 90,
    "achu": 50,
    "allu": 60,
    "suku": 77,
    "dhamu": 89,
    "kuttu": 88
}


def mark(name):
    return students.get(name, "Not found")


name = input("Enter the student's name:")
marks = mark(name)
print(f"Student's Name: {name}, Marks = {marks}/100")
