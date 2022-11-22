"""There are three seating categories at a stadium. For a football games, Class A seat's cost €25,
Class B seat's cost €20 and Class C seat's cost €30. Write a program that asks how many tickets
for each class of seats were sold, and then display the amount of income generated from ticket
sale"""

from enum import IntEnum

class CategoryPrice(IntEnum):
    """Pricing of game tickets by class."""
    CLASS_A = 25
    CLASS_B = 20
    CLASS_C = 30

class Ticket:
    """Football game ticket."""
    def __init__(self, ticket_class, price = int, sold = int):
        self.ticket_class = ticket_class
        self.price = price
        self.sold = sold

    def __str__(self):
        return f"Class {self.ticket_class}"

    def set_price(self, price):
        """Sets the price of a ticket.

        Args:
            price (int): Price of a ticket
        """
        self.price = price

    def get_price(self):
        """Gets the price of a ticket.

        Returns:
            int: Price of a ticket
        """
        return self.price

    def set_sold(self, sold):
        """Sets the amount of tickets sold.

        Args:
            sold (int): Amount of tickets sold.
        """
        self.sold = sold

    def get_sold(self):
        """Gets the amount of tickets sold.

        Returns:
            int: Amount of tickets sold.
        """
        return self.sold

    def calc_income(self):
        """Calculates income generated from sale of tickets.

        Returns:
            float: Total income
        """
        return self.price * self.sold

def sold_tickets_input(categories_list):
    """Asks user to input amount of total tickets sold for each category.

    Args:
        categories_list (list): List containing the different seating categories.
    """
    for category in categories_list:
        total_sold = -1
        while isinstance(total_sold, int) and total_sold < 0:
            try:
                total_sold = int(input(f"Amount of {category} tickets sold: "))
            except ValueError as err:
                print(err)
                total_sold = -1
        category.set_sold(total_sold)

def calc_total_income(categories_list):
    """Calculates the total income across categories.

    Args:
        categories_list (list): List containing the different seating categories.

    Returns:
        float: Total income.
    """
    income = 0
    for category in categories_list:
        income += category.calc_income()
    return income
        
def print_summary(categories_list):
    """Prints a summary report

    Args:
        categories_list (list): List containing the different seating categories.
    """
    total_income = calc_total_income(categories_list)
    print(f"Total income: \u20ac {total_income:.2f}")

if __name__ == "__main__":
    # create tickets
    CLASS_A = Ticket("A", CategoryPrice.CLASS_A)
    CLASS_B = Ticket("B", CategoryPrice.CLASS_B)
    CLASS_C = Ticket("C", CategoryPrice.CLASS_C)

    # group ticket categories
    categories = [CLASS_A, CLASS_B, CLASS_C]

    # tickets sold per each category
    sold_tickets_input(categories)
    
    print_summary(categories)
