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
if _name_ == "_main_":
    main()