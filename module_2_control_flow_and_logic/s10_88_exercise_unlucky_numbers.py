# Section 10 | Lesson 88 | Exercise: Unlucky Numbers
# Course: Modern Python 3 Bootcamp - Colt Steele
# Topic:    Exercise: Unlucky Numbers

#--- Practice Code ---
for num in range(1,21):
    if num == 4 or num == 13:
        print(f"{num} is unlucky")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

   
