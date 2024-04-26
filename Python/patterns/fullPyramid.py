"""
    1
   232
  34543
 4567654
567898765
"""

rows = 5
k = 0
count = 0

for i in range(1, rows + 1):
    for s in range(1, rows - i + 1):
        print(" ", end=" ")
        count += 1

    while k < (2 * i) - 1:
        if count < rows - 1:
            print(i + k, end=" ")
            count += 1
        else:
            c1 += 1
            print(i + k - (2 * c1), end=" ")
            k += 1
            c1 = c = k = 0
    print()
