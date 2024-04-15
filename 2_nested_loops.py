# 2. Nested Loops

# Objective: The aim of this assignment is to practice using nested loops in Python.
# You will correct a nested loop code snippet, simulate a mood tracker, and generate a
#  multiplication table.

# Task 1: Meal Planner Simulate a meal planner that picks a random meal from a meal list 
# for breakfast lunch and dinner for each day of the week. Use nested loops to implement this: 
# the outer loop should iterate over the days, and the inner loop should iterate over the meals of the day.
# For each time, randomly select a meal from a predefined list and print it.

# Output: ..."Tuesday for Breakfast I'm having Yogurt" "Tuesday for Lunch I'm having Chicken" 
# "Tuesday for Dinner I'm having Pizza" "Wednesday for Breakfast I'm having Tacos" ...

import random

days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
breakfast = ['Bacon & Eggs', 'Pancakes', 'Croissant', 'Yogurt', 'Waffles', 'Avo Toast', 'Donut']
lunch = ['Beet Salad', 'Turkey Sandwich', 'Tacos', 'Caesar Salad', 'Buffalo Chic. Salad', 'Chicken & Greens', 'Italian Sandwich']
dinner = ['Spicy Pepperoni Pizza', 'Al Pastor Tacos', "Fried Chicken", "Steak & Potatoes", "Fish Tacos", "Grilled Salmon", "Hawaiian Pizza" ]


for day in days_of_week:
    print(day)
    
    for meal_time in ["Breakfast", "Lunch", "Dinner"]:
        if meal_time == "Breakfast":
            meal = random.choice(breakfast)
        elif meal_time == "Lunch":
            meal = random.choice(lunch)
        elif meal_time == "Dinner":
            meal = random.choice(dinner)
        

