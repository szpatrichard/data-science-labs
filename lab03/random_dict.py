"""Write a function that creates a dictionary using a for loop. Keys being the numbers staring from
1 to 10 inclusive and values are being some random values in the range [1 - 20] inclusive.
Then separate the keys from values and add them in two lists."""

import random as rnd

def create_dict():
    """Creates a dictionary of 10 items with random values.

    Returns:
        dict: A dictionary
    """
    new_dict = dict()
    for i in range(10):
        new_dict[i + 1] = rnd.randint(1, 20)
    return new_dict

def get_keys(d):
    """Gets the keys of a given dictionary.

    Args:
        dict (dict): A dictionary

    Returns:
        list: List of keys
    """
    if not isinstance(d, dict):
        return
    keys = list(d.keys())
    return keys

def get_values(d):
    """Gets the values of a given dictionary.

    Args:
        dict (dict): A dictionary

    Returns:
        list: List of values
    """
    if not isinstance(d, dict):
        return
    values = list(d.values())
    return values

if __name__ == "__main__":
    my_dict = create_dict()
    print(my_dict)

    my_keys = get_keys(my_dict)
    print(my_keys)

    my_values = get_values(my_dict)
    print(my_values)
