"""Write a program that asks the user to enter his/her name and age in year and
then calculate the number of months and days."""

from enum import IntEnum

class TimeConverter(IntEnum):
    """Time conversion rates."""
    YEAR_TO_MONTHS = 12
    YEAR_TO_DAYS = 365

class Person:
    """Person with name and age."""
    def __init__(self, name, age):
        if name:
            self.name = name
        if age >= 0:
            self.age = age

    def __str__(self):
        return f"{self.name}"

    def get_name(self):
        """Gets the name of person.

        Returns:
            str: Name of person.
        """
        return self.name

    def get_age(self):
        """Gets the age of person.

        Returns:
            int: Age of person.
        """
        return self.age

    def convert_age_to_month(self):
        """Converts person's age from years to months.

        Returns:
            int: Person's age in months.
        """
        return self.age * TimeConverter.YEAR_TO_MONTHS

    def convert_age_to_day(self):
        """Converts person's age from years to days.

        Returns:
            int: Person's age in days.
        """
        return self.age * TimeConverter.YEAR_TO_DAYS

def str_input(prompt):
    """Asks user to input a string value.

    Args:
        prompt (str): A prompt to display.

    Returns:
        str: User's string input.
    """
    str_in = None
    while not str_in:
        str_in = input(prompt)
    return str_in

def pos_int_input(prompt):
    """Asks user to input a positive integer value.

    Args:
        prompt (str): A prompt to display.

    Returns:
        str: User's positive integer input.
    """
    int_in = -1
    while isinstance(int_in, int) and int_in < 0:
        try:
            int_in = int(input(prompt))
            if int_in >= 0:
                return int_in
        except ValueError as err:
            print(err)
            int_in = -1

def print_conversion_result(person):
    """Prints the summary result of the age conversion.

    Args:
        person (Person): Person object.
    """
    name = person.get_name()
    months_age = person.convert_age_to_month()
    days_age = person.convert_age_to_day()
    print(f"{name} is {months_age} months old.")
    print(f"{name} is {days_age} days old.")

if __name__ == "__main__":
    # person details
    person_name = str_input("Enter name: ")
    person_age = pos_int_input("Age: ")
    # instantiate a new person object
    person = Person(person_name, person_age)
    print_conversion_result(person)
