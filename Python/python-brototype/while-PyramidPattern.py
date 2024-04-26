"""
pattern:

     *
    * *
   * * *
  * * * *

"""
N = 4

# Outer loop for rows
i = 1
while i <= N:
    # Print spaces
    j = 1
    while j <= N - i:
        print(" ", end="")
        j += 1

    # Print stars
    j = 1
    while j <= 2 * i - 1:
        print("*", end="")
        j += 1

    # Move to the next row
    print()
    i += 1
