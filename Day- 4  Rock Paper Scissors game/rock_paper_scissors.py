import random

# ASCII art for Rock, Paper, Scissors
game_options = [
    # Rock
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """,

    # Paper
    """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
    """,

    # Scissors
    """
    _______
---'   ____)____
          ______)
       __________)
      -----)
---.____)
    """
]

# Get user input safely
try:
    user_input = int(input("Enter 0 for Rock, 1 for Paper, or 2 for Scissors: "))

    if user_input < 0 or user_input > 2:
        print("❌ Invalid choice. Please enter 0, 1, or 2 only.")
    else:
        # Generate computer's choice
        generator = random.randint(0, 2)

        # Compare results
        if generator == user_input:
            # Case 1: Draw
            print("🤝 It's a draw!")
        elif (user_input == 0 and generator == 2) or \
             (user_input == 1 and generator == 0) or \
             (user_input == 2 and generator == 1):
            # Case 2: User wins
            print("🎉 You win!")
        else:
            # Case 3: Computer wins
            print("😢 You lose!")

        # Show choices
        print(f"\nYou chose:\n{game_options[user_input]}")
        print(f"Computer chose:\n{game_options[generator]}")

except ValueError:
    print("❌ Invalid input. Please enter a number (0, 1, or 2).")
