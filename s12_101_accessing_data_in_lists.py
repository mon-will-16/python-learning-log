# Section 12 | Lesson 101 | Accessing Data in Lists
# Course: Modern Python 3 Bootcamp - Colt Steele
# Topic:    Accessing Data in Lists

#--- Practice Code ---
# Like ranges, lists always start counting at zero. So the first element lives at index 0.

colors = ["purple", "teal", "orange"]
print(colors[0]) # purple
print(colors[1]) # teal
print(colors[2]) # orange 

# You can access values from the end. 
# You can use a negative number to index backwards. So -1 is the last element, -2 is the second to last, and so on.
print(colors[-1]) # orange
print(colors[-2]) # teal
print(colors[-3]) # purple

# To check if a value is in a list, we can use the in keyword. This will return True or False.
print("purple" in colors) # True
print("blue" in colors) # False 
