"""Write a Python program to map two lists into a dictionary."""
def map_to_dict(list1, list2):
    """Maps two lists into a dictionary.

    Args:
        list1 (list): List 1
        list2 (list): List 2

    Returns:
        dict: New dictionary
    """
    if not isinstance(list1, list) or not isinstance(list2, list):
        return

    new_dict = dict(zip(list1, list2))
    return new_dict


if __name__ == "__main__":
    first_list = ["abc", "def", "ghi"] # keys
    second_list = ["jkl", "lmn", "opq"] # values

    my_dict = map_to_dict(first_list, second_list)
    print(my_dict)
