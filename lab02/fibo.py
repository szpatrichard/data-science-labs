"""Create a program that prints the first 40 Fibonacci numbers.
The program should then ask the user to enter a positive integer value between
greater than 1 (n) and show the first n Fibonacci numbers."""

class Fibonacci:
    """Fibonacci class"""
    def __init__(self):
        self.cache = [0, 1]

    def __call__(self, n):
        if not (isinstance(n, int) and n >= 0):
            raise ValueError(f"Positive integer number expected, got \"{n}\"")
        if n < len(self.cache):
            return self.cache[n]
        fib_num = self(n - 1) + self(n - 2)
        self.cache.append(fib_num)
        return self.cache[n]

def print_n_fib(f, n):
    """Prints out Fibonacci sequence up to n.

    Args:
        f (Fibonacci): Fibonacci object.
        n (int): Limit on sequence.
    """
    for x in range(n):
        print(f(x))

def int_input(prompt):
    """Prompts user to supply integer value.

    Args:
        prompt (str): Prompt to display.

    Returns:
        int: Integer value.
    """
    int_in = int()
    while isinstance(int_in, int) and int_in <= 0:
        try:
            int_in = int(input(prompt))
            return int_in
        except ValueError as err:
            print(err)
            int_in = int()

if __name__ == "__main__":
    # instantiate new fibonacci object
    fib = Fibonacci()

    print_n_fib(fib, 40)
    num = int_input("Enter a number: ")
    print_n_fib(fib, num)
