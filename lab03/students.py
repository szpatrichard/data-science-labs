"""Write a function that asks end-user to enter name and studentID for each student and
store them in a dictionary where the studentID is the key and the name is its value. The
program should generate appropriate message if end-user tried to provide a key that is
already existing in the dictionary"""

students = dict()

def add_student(student):
    """Adds student to student dictionary.

    Args:
        student (list): List containing student's details.

    Raises:
        KeyError: If key already exists in dictionary.
    """
    if not isinstance(student, list):
        return
    sid = student[0]
    sname = student[1]
    if sid not in students:
        students[sid] = sname
    else:
        raise KeyError(f"Student with id {sid} already exists")

def name_input():
    """Prompts user to provide student's name.

    Returns:
        str: Student name value.
    """
    sname = None
    while not sname:
        sname = input("Student name: ")
    return sname

def id_input():
    """Prompts user to provide student's ID.

    Raises:
        ValueError: When ID value is invalid.

    Returns:
        int: Student ID value.
    """
    sid = 0
    while isinstance(sid, int) and sid <= 0:
        try:
            sid = int(input("Student ID: "))
            if sid <= 0:
                raise ValueError(f"invalid id value: {sid}")
            return sid
        except ValueError as verr:
            print(verr)
            sid = 0

def print_students():
    """Prints out values in students dictionary.
    """
    for sid, sname in students.items():
        print(sid, sname)

if __name__ == "__main__":
    while True:
        student_name = name_input()
        student_id = id_input()

        try:
            add_student([student_id, student_name])
        except KeyError as kerr:
            print(kerr)

        print_students()
