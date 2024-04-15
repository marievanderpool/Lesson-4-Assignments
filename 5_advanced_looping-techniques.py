# Objective: Advance your looping skills by exploring more complex list manipulations. 
# You will learn to selectively loop through parts of a list, use list comprehensions 
# for concise code, and generate numerical lists with Python's range and len function.

# Task 1: Ice Cream BO-GO Your local ice cream shop is running a buy-one-get-one on scoops today,
# create a list of your five favorite scoops. Using a nested for loop print out all 
# the combinations you can make

scoops = ['chocolate', 'strawberry', 'Mint choc. chip', 'vanilla', 'neopolitan']

for scoop_1 in scoops:
    for scoop_2 in scoops:
        if scoop_1 == scoop_2:
            print('Double', scoop_1)
        else:
            print(scoop_1, scoop_2)


