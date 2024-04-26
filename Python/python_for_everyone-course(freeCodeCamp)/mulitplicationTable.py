"""
creating a maths multiplication table
"""

num=int(input("Enter which number's table is needed: "))

print(f"MULTIPLICATION TABLE FOR {num}")

for n in range(1,11):
    sum=num*n
    print(f"{n} x {num} = {sum}")
