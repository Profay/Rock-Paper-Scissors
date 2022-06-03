import random


while True:
    list = {
        "R" : "Rock",
        "P" : "Paper",
        "S" : "Scissors"}
    user_action = input("Enter a choice (R for Rock, P for Paper, S for Scissors): ")
    x = user_action
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    y = computer_action
    if user_action == computer_action:
        print(f"\nYou chose {list[user_action]}, computer chose {list[computer_action]}.\n")
        print(f"The computer and player pick the same move. Player({list[user_action]}) : CPU({list[computer_action]}).\n")
    elif user_action == "R":
        if computer_action == "S":
            print(f"\nBoth player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
            print("Rock smashes scissors! You win!")
            break
        else:
            print(f"\nBoth player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
            print("""
            Paper covers rock! You lose
            CPU win """)
            break
    elif user_action == "P":
        if computer_action == "R":
            print(f"\nBoth player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
            print("Paper covers rock! You win!")
            break
        else:
            print(f"\nBoth player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
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
            print(f"\nBoth player's moves in the format: Player({list[user_action]}) : CPU({list[computer_action]}).\n")
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
