#!/usr/bin/python3

def average_grade(grades=[]):
    """Prints the average grade from
      a list of grades.
    """
    total = 0
    for num in grades:
        total += num
    avg = total / len(grades)
    print(f"The average grade is {avg:.2f}")
