import random

play = True
while play:

    easyNumber = random.randrange(1, 10)
    mediumNumber = random.randrange(1,20)
    hardNumber = random.randrange(1,50)

    level = input("Enter level; Easy, Medium or Hard: ")

    if level.upper() == "EASY":
        tries = 6
        while tries != 0:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                print("invalid number")
            elif guess == easyNumber:
                print("You got it right")
                break
            else:
                print("That was wrong")
            tries -= 1
            print("You have " + str(tries) + " attempt left!")
            if tries == 0:
                print("Game Over!")

    if level.upper() == "MEDIUM":
        tries = 4
        while tries != 0:
            guess = int(input("Guess a number between 1 and 20: "))
            if guess < 1 or guess > 20:
                print("invalid number")
            elif guess == mediumNumber:
                print("You got it right")
                break
            else:
                print("That was wrong")
            tries -= 1
            print("You have " + str(tries) + " attempt left!")
            if tries == 0:
                print("Game Over!")
               
    if level.upper() == "HARD":
        tries = 3
        while tries != 0:
            guess = int(input("Guess a number between 1 and 50: "))
            if guess < 1 or guess > 50:
                print("invalid number")
            elif guess == hardNumber:
                print("You got it right")
                break
            else:
                print("That was wrong")
            tries -= 1
            print("You have " + str(tries) + " attempt left!")
            if tries == 0:
                print("Game Over!")
    
    play_again = input("Would you like to play again? Yes/No: ")
    if play_again.upper() == "NO":
        play = False
    else:
        play = True
        
    
           
    
 
         




       


