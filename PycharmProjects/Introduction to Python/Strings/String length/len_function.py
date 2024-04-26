phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""

total_length = len(phrase)

index_to_slice = total_length // 2  # Get the index up to which you will slice.
first_half = phrase[:index_to_slice]  # Get the slice of the phrase.
print(first_half)
