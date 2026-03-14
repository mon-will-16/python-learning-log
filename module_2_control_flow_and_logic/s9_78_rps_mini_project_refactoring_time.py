# Section 9 | Lesson 78 | RPS Mini Project: Refactoring Time
# Course: Modern Python 3 Bootcamp - Colt Steele
# Topic:    RPS Mini Project: Refactoring Time

# --- Practice Code ---
print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("player 1, make yor move: ")
player2 = input("player 2, make your move: ")

if player1 == player2:   
    print("It's a tie!")
elif player1 == "rock":
    if player2 == "scissors":
        print("player 1 wins!")
    elif player2 == "paper":
        print("player2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("player 1 wins!")
    elif player2 == "scissors":
        print("player 2 wins!")
elif player1 == "scissors":
    if player2 == "paper": 
        print("player 1 wins!")
    elif player2 == "rock":
        print("player 2 wins!")
else:
    print("something went wrong") 







