# This is my first game in python bruv I'M REALLY HAPPY ABOUT THIS YAAAY
print("Rock...")
print("Paper...")
print("Scissors...")
print("Player 1, make your move")
player1 = input()
print("Player 2, make your move")
player2 = input()

if player1 == "rock" and player2 == "scissors":
    print("player1 wins!")
elif player1 == "rock" and player2 == "paper":
    print("player2 wins!")
elif player1 == "paper" and player2 == "rock":
    print("player1 wins!")
elif player1 == "paper" and player2 == "scissors":
    print("player2 wins!")
elif player1 == "scissors" and player2 == "rock":
    print("player2 wins!")
elif player1 == "scissors" and player2 == "paper":
    print("player1 wins!")
elif player1 == player2:
    print("it's a tie")
else:
    print("something went wrong!")
