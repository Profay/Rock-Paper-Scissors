import random

print("""Welcome!
         This is the Rock-Paper-Scissors game.
        How to play?
        1. You are playing against the computer.
        2. You are to choose an option from,
           R for Rock, P for Paper and S for Scissors.
        3. Rock beats Scissors (Rock Wins)
           Paper beats Rock (Papper Wins)
           Scissors beats Paper (Scissors Wins)
           So if you choose R - Rock and Computer choose S - Scissors,
           YOU WIN.
           If you choose P - Paper and Computer choose S - Scissors,
           YOU LOSE.
           Have Fun playing!
             """)

while True:
    list = {
        "R" : "Rock",
        "P" : "Paper",
        "S" : "Scissors"}
    user_action = input("Enter a choice (R for Rock, P for Paper, S for Scissors): ")
    user_action = user_action.upper()
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    if user_action == computer_action:
        print(f"\nYou chose {list[user_action]}, Computer chose {list[computer_action]}.\n")
        print(f"The Computer and Player pick the same move. Player({list[user_action]}) : CPU({list[computer_action]}).\n")
    elif user_action == "R":
        if computer_action == "S":
            print(f"\nBoth Player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
            print("Rock smashes scissors! You win!")
            break
        else:
            print(f"\nBoth Player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
            print("""
            Paper covers rock! You lose
            CPU win """)
            break
    elif user_action == "P":
        if computer_action == "R":
            print(f"\nBoth Player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
            print("Paper covers rock! You win!")
            break
        else:
            print(f"\nBoth Player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
            print("""
            Scissors cuts paper! You lose.
            CPU win
             """)
            break
    elif user_action == "S":
        if computer_action == "P":
            print(f"\nBoth player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
            print("Scissors cuts paper! You win!")
            break
        else:
            print(f"\nBoth Player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
            print("""
            Rock smashes scissors! You lose.
            CPU win """)
            break
    else:
        print("""
                Error! You've entered the wrong input. 
                Did you want to try again? 
                
                """)
        continue
