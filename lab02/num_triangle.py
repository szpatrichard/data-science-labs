"""Implement a function called printNumTriangle. The function should ask the user to
enter a single integer. It should then print a triangle of that size specified by the
integer so that each row in the triangle is made up of the integer displayed."""

def print_num_triangle(size):
    """Prints out a triangle of specific size.

    Args:
        size (int): Size of triangle.
    """
    for x in range(1, size + 1):
        print(f"{x}" * x)

def int_input(prompt):
    """Prompt user for an integer value.

    Args:
        prompt (str): Prompt to display.

    Returns:
        int: An integer value.
    """
    int_in = None
    while int_in is None:
        try:
            int_in = int(input(prompt))
            return int_in
        except ValueError as err:
            print(err)
            int_in = None

if __name__ == "__main__":
    num = int_input("Enter triangle size: ")
    print_num_triangle(num)
