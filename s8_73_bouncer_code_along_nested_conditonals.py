# Section 8 | Lesson 73 | Bouncer Code-Alogn and Nested Conditionals
# Course: Modern Python 3 Bootcamp - Colt Steele
# Topic:    Bounder-Code-Along and Nested Conditionals

# --- Practice Code ---
# ask for age
age = input("How old are you: ")
if age:
    age = int(age)
    if (age) >= 18 and (age) < 21:
        # 18-21 wristband
        print("You can enter, but need a wristband!")

    elif (age) >= 21:
        # 21+ drink, normal entry 
        print("You are good to enter and can drink!")
    else:
        #too young sorry
        print("You can't conme in, little one! :(")
else:
    print("Please enter an age!")




