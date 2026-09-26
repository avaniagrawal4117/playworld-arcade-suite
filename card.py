def Card_higher_or_lower():
  import random
  current_card = random.randint(1, 13)
   print(f"The current card value is {current_card} (from 1 to 13).")
  choice = input("Will the next card be Higher or Lower? (h/l): ").lower()
   next_card = random.randint(1, 13)

  print(f"The next card was: {next_card}")

   if (choice == 'h' and next_card > current_card) or (choice == 'l' and next_card < current_card):
     print("You got it right! ")
   elif next_card == current_card:
    print("It's a tie value!")
  else:
    print("Incorrect! Better luck next time.")