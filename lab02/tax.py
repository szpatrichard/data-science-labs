"""Write a program that determine the tax rate based on two factors:
salary and having kids or not."""

class Tax:
    """Employee's tax rates."""
    def __init__(self, rate):
        if isinstance(rate, int) and rate >= 0:
            self.rate = rate

    def __str__(self):
        return f"Tax rate is {self.rate}"

    def get_rate(self):
        """Gets tax rate of employee.

        Returns:
            int: Tax rate.
        """
        return self.rate

    def set_rate(self, rate):
        """Sets tax rate of employee.

        Args:
            int (float): Tax rate.
        """
        if isinstance(rate, int) and rate >= 0:
            self.rate = rate

class Employee:
    """Employee details."""
    def __init__(self, name, salary = float, has_kids = bool):
        if isinstance(name, str):
            self.name = name
        if isinstance(salary, (float, int)) and salary >= 0:
            self.salary = salary
        if isinstance(has_kids, bool):
            self.has_kids = has_kids
        self.tax = Tax(self._determine_tax_rate())

    def __str__(self):
        return f"{self.name}"

    def get_name(self):
        """Gets employee name.

        Returns:
            str: Employee name.
        """
        return self.name

    def get_salary(self):
        """Gets employee salary.

        Returns:
            float: Employee salary.
        """
        return self.salary

    def get_kids(self):
        """Gets whether employee has kids or not.

        Returns:
            bool: Does employee have kids?
        """
        return self.has_kids

    def _determine_tax_rate(self):
        """Determines the tax rate for an employee

        Returns:
            float: Employee tax rate.
        """
        if 30 <= self.salary < 50:
            if self.has_kids:
                return 35
            else:
                return 40
        if 50 <= self.salary < 70:
            if self.has_kids:
                return 45
            else:
                return 50
        if self.salary >= 70:
            return 55
        return 0

def employee_input():
    """Prompts user to provide employee details.

    Raises:
        ValueError: When invalid salary value is given.

    Returns:
        str: Employee name.
        float: Employee salary.
        bool: Does employee have kids?
    """
    name = None
    salary = float("-inf")
    has_kids = False

    # name validation
    while not name:
        name = input("Enter your name: ")

    # salary validation
    while (isinstance(salary, (float, int)) and salary < 0):
        try:
            salary = float(input("Your salary: "))
            if salary < 0:
                raise ValueError(f"invalid salary value: {salary}")
        except ValueError as err:
            print(err)
            salary = float("-inf")

    # kids validation
    kids = input("Do you have kids (y/N): ")
    if kids.lower() == "y":
        has_kids = True

    return name, salary, has_kids

def print_tax_rate(employee):
    """Prints tax rate results for an employee.

    Args:
        employee (Employee): An employee.
    """
    name = employee.get_name()
    salary = employee.get_salary()
    kids = employee.get_kids()
    tax_rate = employee.tax.get_rate()
    print(f"\n{name}'s Employment details:\n"
          f"Salary: \u20ac{salary:.2f}\n"
          f"Has kids: {kids}\n"
          f"Tax rate: {tax_rate}%")

if __name__ == "__main__":
    # details of employee
    e_name, e_salary, e_kids = employee_input()
    # instantiate new employee object
    e = Employee(e_name, e_salary, e_kids)

    print_tax_rate(e)
