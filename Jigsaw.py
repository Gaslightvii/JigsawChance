import sys,time,random

## Defines slowtype
typing_speed = 60 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

## Gets the total number of jigsaw pieces for the puzzle
totalNumberPieces = int(input("How many pieces: "))

## Stores the number of remaining pieces left to place
numberPiecesLeft = totalNumberPieces

## Displays the chance of correctly picking the correct piece at random
chance = "You have a 1 in " + str(numberPiecesLeft) + " chance of picking the right piece. "

## Displays the total at the start
slow_type("There are " + str(totalNumberPieces) + " pieces in total. ")
slow_type(chance)

## Checks if the user has succesfully placed a piece and displays the new chance
userInput = "Y"
while userInput == "Y" and numberPiecesLeft > 1:
    userInput = input("Have you succesfully placed a jigsaw piece? Y/N: ")
    numberPiecesLeft = numberPiecesLeft -1
    slow_type("You have a 1 in " + str(numberPiecesLeft) + " chance of picking the right piece. ")

slow_type("Thank you for playing.")






