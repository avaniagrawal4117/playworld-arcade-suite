def Guess_the_number():
     import random
     number = random.randint(1,100)
     while True:
         guess = int(input("Guess a number between 1 to 100:"))
        if guess  == number:
           print("congrats!you guessed the number.")
             break
             play_world()
         elif guess > number:
             print ("lower")
         elif guess < number:
             print ("higher")
         else:
             print("invalid input!")