import random


# 1. Rock, Paper, Scissors
def rock_paper_scissors():
    print("\n--- Rock, Paper, Scissors ---")
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Returning to menu.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")


# 2. Snake, Water, Gun
def snake_water_gun():
    print("\n--- Snake, Water, Gun ---")
    choices = ["snake", "water", "gun"]
    user_choice = input("Enter snake, water, or gun: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Returning to menu.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Snake drinks Water, Water douses Gun, Gun kills Snake
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "snake" and computer_choice == "water")
        or (user_choice == "water" and computer_choice == "gun")
        or (user_choice == "gun" and computer_choice == "snake")
    ):
        print("You win!")
    else:
        print("You lose!")


# 3. Roll a Dice
def roll_a_dice():
    print("\n--- Roll a Dice ---")
    user_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print(f"You rolled: {user_roll}")
    print(f"Computer rolled: {computer_roll}")

    if user_roll > computer_roll:
        print("You win!")
    elif computer_roll > user_roll:
        print("You lose!")
    else:
        print("It's a tie!")


# 4. Card Higher or Lower
def card_higher_or_lower():
    print("\n--- Card Higher or Lower ---")
    current_card = random.randint(1, 13)
    print(f"Current card rank: {current_card} (1=Ace, 13=King)")

    guess = (
        input("Will the next card be 'higher' or 'lower'? ").strip().lower()
    )
    next_card = random.randint(1, 13)

    print(f"Next card was: {next_card}")

    if (
        guess == "higher"
        and next_card > current_card
        or guess == "lower"
        and next_card < current_card
    ):
        print("You win!")
    elif next_card == current_card:
        print("It's a tie!")
    else:
        print("You lose!")


# 5. Guess the Number
def guess_the_number():
    print("\n--- Guess the Number ---")
    secret_number = random.randint(1, 100)
    attempts = 5
    print("I have chosen a number between 1 and 100. You have 5 attempts!")

    while attempts > 0:
        try:
            guess = int(input(f"\nAttempts left ({attempts}). Enter guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number}!")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1

    print(f"Game over! The number was {secret_number}.")


# Main Control Loop
def main():
    while True:
        print("\n==============================")
        print("Welcome to Playworld!")
        print("==============================")
        print("What do you want to play?")
        print("1. Rock paper and scissors")
        print("2. Snake gun and Water")
        print("3. Roll a dice")
        print("4. Card higher or lower?")
        print("5. Guess the number")

        choice = input("\nEnter choice (1-5 or game name): ").strip().lower()

        if choice in ["1", "rock paper and scissors", "rock"]:
            rock_paper_scissors()
        elif choice in ["2", "snake gun and water", "snake"]:
            snake_water_gun()
        elif choice in ["3", "roll a dice", "dice"]:
            roll_a_dice()
        elif choice in ["4", "card higher or lower?", "card"]:
            card_higher_or_lower()
        elif choice in ["5", "guess the number", "guess"]:
            guess_the_number()
        else:
            print("Invalid selection! Please try again.")
            continue

        play_again = (
            input("\nDo you want to play more? (yes/no): ").strip().lower()
        )
        if play_again not in ["yes", "y"]:
            print("\nThanks for playing! Goodbye!")
            break


# Run the program
if __name__ == "__main__":
    main()