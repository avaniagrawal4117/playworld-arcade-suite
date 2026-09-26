def snake_water_gun():
   #Snake drinks Water (Snake wins)
   #Water douses Gun (Water wins)
   #Gun kills Snake (Gun wins)
    import random
     choices = ["snake", "water", "gun"]
     computer = random.choice(choices)

     player = input("Choose Snake, Water, or Gun: ").strip().lower()

     if player not in choices:
         print("Invalid choice! Choose snake, water, or gun.")
         return

    print(f"Computer chose: {computer.capitalize()}")

     if player == computer:
        print("It's a tie! ")
    elif (player == "snake" and computer == "water") or \
          (player == "water" and computer == "gun") or \
          (player == "gun" and computer == "snake"):
         print("You win! ")
    else:
         print("You lose!")