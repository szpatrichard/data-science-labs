"""Using list to set conversion, write a short function to only find the number of items that
are repeated more than once in the list."""

def find_repeats(my_list):
    """Finds the amount of repeated values in a list.

    Args:
        my_list (list): List to check.

    Returns:
        int: Number of repeats in given list.
    """
    print(my_list)
    my_set = set(my_list)
    print(my_set)
    rp = len(my_list) - len(my_set)
    return rp

if __name__ == "__main__":
    repeats = find_repeats([1, 32, 4, 56, 6, 6, 23, 1, 2, 12, 32, 3])
    print(repeats)
