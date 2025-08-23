#!/usr/bin/python3

def remove_grades(grades=[]):
    """Returns a list with scores above 80.
       Adds 5 to the grades in this list

    args:
         grades: List of grades.

    Return:
           A list of grades greater than or equal to 80.
    """
    above_eighty = []
    for grade in grades:
        if grade > 80:
            grade += 5
            above_eighty.append(grade)
    return above_eighty
