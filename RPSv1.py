# This is my first game in python bruv I'M REALLY HAPPY ABOUT THIS YAAAY
print("Rock...")
print("Paper...")
print("Scissors...")
print("Player 1, make your move")
player1 = input()
print("*** NO CHEATIING! ***\n\n" * 34)
print("Player 2, make your move")
player2 = input()

if player1 == player2:
    print("it's a tie")
elif player1 == "rock":
    if player2 == "scissors":
        print("player1 wins!")
    elif player2 == "paper":
        print("player2 wins!")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins!")
    elif player2 == "scissors":
        print("player2 wins!")
elif player1 == "scissors":
    if player2 == "paper":
        print("player1 wins!")
    elif player2 == "rock":
        print("player2 wins!")
else:
    print("something went wrong!")
