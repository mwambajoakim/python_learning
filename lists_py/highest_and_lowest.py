#!/usr/bin/python3

def high_and_low(grades=[]):
    """Gets the gighest and lpwest grades.

    args:
         grades: List of grades.
    """
    lowest = grades[0]
    highest = grades[0]
    for grade in grades:
        if grade < lowest:
            lowest = grade
        elif grade > highest:
            highest = grade
    print(f"Lowest grade is {lowest}")
    print(f"Highest grade is {highest}")
