# Section 10 | Lesson 88 | Introducing While Loops
# # Course: Modern Python 3 Bootcamp - Colt Steele
# Topic:    Introducing While Loops

#--- Practice Code ---
# With the while loop we can execute a set of statements as long as a condition is true.
# A while loop is basically: check condition > run code > update something > repeat
# if you don't update something, the loop never ends.
msg = input("whats the secret password?")
while msg != "bananas":
    print("WRONG!")
    msg = input("whats the secret password?")
print("CORRECT!")
