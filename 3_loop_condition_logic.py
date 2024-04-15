# Objective: The aim of this assignment is to explore the importance of the loop condition in while loops. 
# You will create loops with different conditions to see how they influence the behavior of the loop.

# Task 1: Loop Condition Exploration Write a while loop with a condition that will never be true
#  (an infinite loop).  Ask the user a series of questions until their answer triggers a break statement.

cake = []

while True:
    answer = input ("What kind of cake will you have at your party?")
    if answer == "carrot cake":
        break

# Task 2: Conditional Exit 
# Create a while loop that will terminate after 5 iterations,
#  and each iteration you print which iteration it is on. (use a control variable)

everest_peak = []

while len(everest_peak) < 5:
    print('This person summited!')
    everest_peak.append('Person')