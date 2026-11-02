# Rock-Paper-Scissors Game
# This program allows a player to play Rock-Paper-Scissors
# against the computer until the player decides to quit.

# Import randint to generate the computer's random choice.
from random import randint

# Display the game rules.
print("===== ROCK PAPER SCISSORS GAME =====")
print("Game Rules:")
print("1. Rock defeats Scissors")
print("2. Scissors defeats Paper")
print("3. Paper defeats Rock")
print("4. Same choices result in a draw")

# Store the available choices in a list.
choices = ["Rock", "Paper", "Scissors"]

# Start a loop so the player can play multiple rounds.
while True:

    # Display the available options.
    print("\nChoose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    # Accept the player's choice.
    player_input = input("Enter your choice (1-3): ")

    # Validate the player's input.
    if player_input not in ["1", "2", "3"]:
        print("Invalid choice! Please enter 1, 2, or 3.")
        continue

    # Convert the player's input from a string to an integer.
    player_number = int(player_input)

    # Find the player's choice using list indexing.
    # Subtract 1 because Python list indexes start at 0.
    player_choice = choices[player_number - 1]

    # Generate a random integer between 1 and 3.
    computer_number = randint(1, 3)

    # Convert the computer's number into its corresponding choice.
    computer_choice = choices[computer_number - 1]

    # Display both selections.
    print("\nYou chose:", player_choice)
    print("Computer chose:", computer_choice)

    # Compare the choices to determine the winner.
    if player_choice == computer_choice:

        # Both players selected the same option.
        print("It's a draw!")

    elif (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or
        (player_choice == "Scissors" and computer_choice == "Paper")
        or
        (player_choice == "Paper" and computer_choice == "Rock")
    ):

        # The player wins if one of the three winning conditions is true.
        print("Congratulations! You win!")

    else:

        # If it is not a draw and the player did not win,
        # the computer must be the winner.
        print("Computer wins! Better luck next time.")

    # Ask whether the player wants another round.
    play_again = input("\nDo you want to play again? (Y/N): ").strip().upper()

    # Exit the loop if the player enters N.
    if play_again == "N":
        print("Thanks for playing! Goodbye!")
        break

    # Continue playing if the player enters Y.
    elif play_again == "Y":
        continue

    # Exit if the player enters anything other than Y or N.
    else:
        print("Invalid response. Ending the game.")
        break