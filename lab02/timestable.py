"""Write a function that will print out the "times" table for a number up to a
specific limit. The function should take in two parameters. The first value, *num*, is the
number that we will multiply by 0, 1, 2, 3, etc. The second number, *limit*, is the
number at which we will stop multiplying."""

def times_tables(num, limit):
    """Multiplies num until it reaches the limit.

    Args:
        num (int): Timestable number.
        limit (int): Limit on multiplication.
    """
    for x in range(limit):
        print(f"{num} * {x} = {num * x}")

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
    multiplier = int_input("Enter multiplier: ")
    limiter = int_input("Enter limit: ")
    times_tables(multiplier, limiter)
