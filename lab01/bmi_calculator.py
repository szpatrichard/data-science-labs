"""Write a program to calculate and display a person's body mass index (BMI).
A persons BMI is calculated with the following formula:
BMI = (weight/ height2 ) * 703
Where weight in in pounds and height is in inches."""

def positive_int_input(prompt = str):
    """Ensures that user input is returned as a positive integer.

    Args:
        prompt (str): Prompt to ask the user. Defaults to str.

    Returns:
        int: Positive integer.
    """
    int_in = 0
    while isinstance(int_in, int) and int_in <= 0:
        try:
            int_in = int(input(prompt))
        except ValueError as err:
            print(err)
            int_in = 0
    return int_in

def weight_input():
    """Asks user for weight.

    Returns:
        int: Weight in lbs.
    """
    w = positive_int_input("Enter weight (lbs): ")
    return w

def height_input():
    """Asks user for height.

    Returns:
        int: Height in inches.
    """
    h = positive_int_input("Enter height (in): ")
    return h

def calc_bmi(weight = int, height = int):
    """Calculates Body Mass Index based on supplied weight and height.

    Args:
        weight (int, optional): Weight. Defaults to int.
        height (int, optional): Height. Defaults to int.

    Returns:
        float: BMI
    """
    if not isinstance(weight, int) or not isinstance(height, int):
        return 0
    if weight < 0 or height < 0:
        return 0
    return (weight / pow(height, 2)) * 703

def print_bmi(index = float):
    """Prints result.

    Args:
        index (float, optional): BMI. Defaults to float.
    """
    print(f"BMI: {index:.2f}")

if __name__ == "__main__":
    # base parameters
    WEIGHT = weight_input()
    HEIGHT = height_input()
    # body mass index calculation
    bmi = calc_bmi(WEIGHT, HEIGHT)
    print_bmi(bmi)
