"""Write a program that will ask a student for their first name and then for their surname.
It should then ask the student to enter the int numerical grade they received in each of
their three subjects."""

def names_input():
    """Asks user to give their first name and surname.

    Returns:
        str: Student's first name.
        str: Student's surname.
    """
    fname = None
    sname = None
    while not fname:
        fname = input("First name: ")
    while not sname:
        sname = input("Surname: ")
    return fname, sname

def grades_input():
    """Asks user to supply their grades for three subjects.

    Returns:
        list: A list of grades.
    """
    grades_list = []
    for _ in range(3):
        grade = float()
        while isinstance(grade, float) and grade <= 0:
            grade = input("Enter your grade: ")
            try:
                grade = float(grade)
                grades_list.append(grade)
            except ValueError as err:
                print(err)
                grade = float()
    return grades_list

def calc_average(grades_list = list):
    """Calculates the average from a list of grades.

    Args:
        grades_list (list, optional): A list of grades. Defaults to list.

    Returns:
        float: The average
    """
    grades_avg = 0
    grades_sum = 0
    for g in grades:
        grades_sum += g
    grades_avg = grades_sum / len(grades_list)
    return grades_avg

def print_summary(names = list, average = float):
    """Prints a summary report.

    Args:
        names (list, optional): Names of student in a list. Defaults to list.
        average (float, optional): The average of the student's grades. Defaults to float.
    """
    fname, sname = names
    print(f"{fname} {sname}'s average: {average:.2f}%")

if __name__ == "__main__":
    firstname, surname = names_input()
    grades = grades_input()
    average_grade = calc_average(grades)
    print_summary([firstname, surname], average_grade)
