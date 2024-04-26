"""
Below is code to find the smallest value from a list of values.
One line has an error that will cause the code to not work as expected.
Which line is it?:
=> break
"""

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        # break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)