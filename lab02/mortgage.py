"""Using conditional statements and logical operators write a Python code that satisfies the
following conditions:
-   If salary more than 40 and you are older than 25 or if you have worked 25 years and
    have kid you can apply for mortgage."""

class Mortgage:
    """Bank mortgage."""
    def __init__(self, customer):
        handler = MortgageHandler(customer)
        self.eligible = handler.mortgage_applicable()

    def __str__(self):
        if self.eligible:
            return "You are eligible for a mortgage"
        return "You aren't eligible for a mortgage"

class MortgageHandler:
    """Handling mortgage application process."""
    def __init__(self, customer):
        self.customer = customer
        self.mortgage_applicable()

    def mortgage_applicable(self):
        """Determines if customer is applicable for a mortgage based on conditions.

        Returns:
            bool: Customer applicability for a mortgage.
        """
        customer = self.customer
        if customer.salary > 40 and customer.age > 25:
            return True
        if customer.years_employed > 25 and customer.has_kids:
            return True
        return False

class Customer:
    """Bank customer class."""
    def __init__(self, name, salary = float, age = int, years_employed = int, has_kids = bool):
        if isinstance(name, str):
            self.name = name
        if isinstance(salary, (float, int)) and salary >= 0:
            self.salary = salary
        if isinstance(age, int) and 0 < age < 150:
            self.age = age
        if isinstance(years_employed, int) and years_employed > 0:
            self.years_employed = years_employed
        if isinstance(has_kids, bool):
            self.has_kids = has_kids
        self.mortgages = []
    
    def __str__(self):
        return f"Hello {self.name}!"
    
    def check_eligibility(self):
        """Checks if customer is eligible for a mortgage."""
        mortgage = Mortgage(self)
        self.mortgages.append(mortgage)
        
    def print_mortgages(self):
        """Prints the mortgages which the customer has applied for."""
        for mortgage in self.mortgages:
            print(mortgage)
    
if __name__ == "__main__":
    # Instantiate new customer
    c = Customer("Bean", salary=45, age=26, years_employed=1, has_kids=False)
    # Greet customer
    print(c.__str__())
    
    c.check_eligibility()
    c.print_mortgages()
