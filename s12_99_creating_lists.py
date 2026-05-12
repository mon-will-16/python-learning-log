# Section 12 | Lesson 99 | Creating Lists
# Course: Modern Python 3 Bootcamp - Colt Steele
# Topic:    Creating Lists

#--- Practice Code ---
# A list is a collection or grouping of items
# A fundamental data structure for organizing collections of items 
# tasks = ["install Python", "Learn Python", "Take a break"]
# Seperate items with commas and enclose the entire list in square brackets
# Lists can contain any type of data, including strings, numbers, and even other lists
# A list can be empty, which is denoted by empty square brackets []
# Lists are mutable, meaning you can change their contents after they have been created

demo_list = ["a", 1, 45, True, 6.777]
len(demo_list) #5

#Another way to make a list is using the built in list() function
tasks = list(range(1, 4))
#The range() function generates a sequence of numbers, and when we pass it to list(), it creates a list from that sequence 