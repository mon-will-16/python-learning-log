# Section 9 | Lesson 77 | RPS Mini Project Basic Version Solution
# Course: Modern Python 3 Bootcamp - Colt Steele
# Topic:    RPS Mini Project Basic Version Solution

# --- Practice Code ---
print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("player 1, make yor move: ")
player2 = input("player 2, make your move: ")

if player1 == "rock" and player2 == "scissors":
    print("player 1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("player 1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("player 2 wins!") 
elif player1 == "scissors" and player2 == "rock": 
    print("player 2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("player 1 wins!")
elif player1 == player2:
    print("It's a tie!")
else:
    print("something went wrong") 







