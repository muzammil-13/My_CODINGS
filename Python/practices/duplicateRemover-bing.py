def remove_duplicates(arr):
    """
    This function removes duplicate elements from a given array.

    Args:
      arr: A list of integers.

    Returns:
      A new list with the duplicates removed.
    """

    # Create an empty set to store unique elements.
    unique_elements = set()

    # Iterate over the array.
    for element in arr:
        # If the element is not already in the set, add it.
        if element not in unique_elements:
            unique_elements.add(element)

    # Return the list of unique elements.
    return list(unique_elements)


# Example usage
arr = [10, 13, 10, 26, 10, 26, 8]
unique_arr = remove_duplicates(arr)
print(f"Original array: {arr}")
print(f"Array after removing duplicates: {unique_arr}")
