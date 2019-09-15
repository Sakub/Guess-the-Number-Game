import random

print("""
<<<Welcome in Guess the Number Game!>>>
<<<Try to guess the number from 1 to 100>>>
""")
randomNumer = random.randint(1, 100)
numberOfTries = 1

def game():
    global numberOfTries
    try:
        userGuess = int(input("Try to guess: "))
    except ValueError:
        print("Error! Number expected")
        game()
    else:
        if userGuess > randomNumer:
            print("Too high!")
            numberOfTries += 1
            game()
        elif userGuess < randomNumer:
            print("Too low!")
            numberOfTries += 1
            game()
        elif userGuess == randomNumer:
            print("You won! Number of tries: ",numberOfTries)
            print("\n\n\n<<<Made by SakubDev>>>>")

   
game()