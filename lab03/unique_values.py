"""Write a Python program to print all unique values in a dictionary."""

import random_dict as rd

def get_unique_values(d):
    """Gets the unique values of a given dictionary.

    Args:
        d (dict): A dictionary

    Returns:
        set: Set of unique values
    """
    if not isinstance(d, dict):
        return
    values = set(d.values())
    return values

if __name__ == "__main__":
    my_dict = rd.create_dict()
    print(my_dict)

    my_unique_values = get_unique_values(my_dict)
    print(my_unique_values)
    print(len(my_unique_values))
