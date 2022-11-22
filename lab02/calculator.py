"""Write a program that will act as a basic calculator for the user. The
program should first ask the user for two separate numerical values. It
should then give the user an option to perform one of four operations:
addition, subtraction, division or multiplication. Therefore, if the user
selects multiplication then your program should print out the product of
the two values."""

from enum import IntEnum

class ArithmeticOperation(IntEnum):
    """Arithmetic operations."""
    ADDITION = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4

class Calculator:
    """Calculator class."""
    def add(self, n1, n2):
        """Adds two numbers together.

        Args:
            n1 (float): n1
            n2 (float): n2

        Returns:
            float: sum
        """
        return n1 + n2

    def subtract(self, n1, n2):
        """Subtracts a number away from the other.

        Args:
            n1 (float): n1
            n2 (float): n2

        Returns:
            float: difference
        """
        return n1 - n2

    def multiply(self, n1, n2):
        """Multiplies two numbers together.

        Args:
            n1 (float): n1
            n2 (float): n2

        Returns:
            float: product
        """
        return n1 * n2

    def divide(self, n1, n2):
        """Divides a number from the other.

        Args:
            n1 (float): n1
            n2 (float): n2

        Returns:
            float: quotient
        """
        return n1 / n2

def get_inputs():
    """Gets two numbers for arithmetic operation.

    Returns:
        list: List of two numbers.
    """
    nums_list = list()
    for x in range(2):
        n = None
        while not isinstance(n, float):
            try:
                n = float(input(f"Enter a value {x + 1}: "))
                nums_list.append(n)
            except ValueError as err:
                print(err)
                n = None
    return nums_list

def operation_to_perform():
    """User selects which arithmetic operation to perform on numbers.

    Returns:
        ArithmeticOperation: User selected operation.
    """
    operation_selection = None
    while operation_selection is None:
        selection_input = input("What operation would you like to perform?\n"
                          "1. Addition\n"
                          "2. Subtraction\n"
                          "3. Multiplication\n"
                          "4. Division\n"
                          "-> ")
        try:
            operation_selection = ArithmeticOperation(int(selection_input))
            print(operation_selection)
        except ValueError as err:
            print(err)
            operation_selection = None
    return operation_selection

def calculate(nums_list, operation):
    """Calculates the result between the numbers based on the given operation.

    Args:
        nums (list): List of numbers.
        operation (ArithmeticOperation): Arithmetic operation to perform.

    Raises:
        ValueError: When invalid numbers are given.

    Returns:
        float: Result of arithmetic operation.
    """
    n1, n2 = nums_list

    if not isinstance(n1, float) or not isinstance(n2, float):
        raise ValueError(f"Expected float value as parameters, got {n1}, {n2}")

    calculator = Calculator()
    if operation == 1:
        return calculator.add(n1, n2)
    if operation == 2:
        return calculator.subtract(n1, n2)
    if operation == 3:
        return calculator.multiply(n1, n2)
    if operation == 4:
        return calculator.divide(n1, n2)

if __name__ == "__main__":
    while True:
        # numbers list
        nums = get_inputs()

        # arithmetic operation
        arithm_op = operation_to_perform()

        # calculate result of arithmetic operation
        result = calculate(nums, arithm_op)

        # operation sign
        sign = (
            "+" if arithm_op == 1
            else "-" if arithm_op == 2
            else "*" if arithm_op == 3
            else "/")

        # print expression
        print(f"{nums[0]} {sign} {nums[1]} = {result}")

        # quit program
        leave = input("Exit? [y/N] ")
        if leave.lower() == "y":
            break
