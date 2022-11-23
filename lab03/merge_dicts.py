"""Write a Python script to merge two Python dictionaries."""

def merge(dict1, dict2):
    """Merge two dictionaries.

    Args:
        dict1 (dict): Dictionary 1
        dict2 (dict): Dictionary 2

    Returns:
        dict: New dictionary
    """
    if not isinstance(dict1, dict) or not isinstance(dict2, dict):
        return

    new_dict = dict1
    new_dict.update(dict2)
    return new_dict

if __name__ == "__main__":
    first_dict = {123: "asd", 234: "fgh"}
    second_dict = {345: "jkl", 456: "mno"}

    my_dict = merge(first_dict, second_dict)
    print(my_dict)
