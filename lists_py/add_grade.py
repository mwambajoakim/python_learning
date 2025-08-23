#!/usr/bin/python3

def add_grade(*args):
    """Adds grades of a user

   Args:
        grade: Grade to add to list of grades.
    """
    grades = []
    for arg in args:
        if not isinstance(arg, int):
            raise TypeError("Grade must be an integer")
        else:
            grades.append(arg)
    return grades
