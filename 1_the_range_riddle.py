# 1. The Range Riddle

# Objective: The aim of this assignment is to deepen your understanding of Python's
# range () function. and its application in loops. You will correct a code snippet, simulate moods
#  for different days, and create a countdown timer.

# Task 1: Every Other Day Write a program that prints each day of the week,
#  but only if that day is on an even index.

# Example Outcome: An example output could be "Sunday", "Tuesday", "Thursday"

days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

for index in range(len(days_of_week)):
    if index % 2 == 0:
        print(days_of_week[index])