"""Write a program that goes through a list and extract only integer values and add them in a new
list.
Extract unique integer values too."""

def extract_ints(l):
    """Extracts integers from a list.

    Args:
        l (list): List

    Returns:
        list: List of integer values
    """
    if not isinstance(l, list):
        return

    temp = list()

    for i in l:
        if isinstance(i, int):
            temp.append(i)
    return temp

def extract_unique_ints(l):
    """Extracts unique integers from a list.

    Args:
        l (list): List

    Returns:
        set: Set of integer values
    """
    if not isinstance(l, list):
        return
    
    temp = set()
    for i in l:
        if isinstance(i, int):
            temp.add(i)
    return temp

if __name__ == "__main__":
    my_list = [1, 4, 5.5, "da", 4, "aa"]
    
    my_ints = extract_ints(my_list)
    print(my_ints)
    
    my_unique_ints = extract_unique_ints(my_list)
    print(my_unique_ints)
