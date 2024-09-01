# Begin the game and choose either "Easy" or "Hard" level.
# A number between 1 to a 100 is selected by the computer.
# You make an effort to guess within the specified limits.
# Feedback is provided for each attempt made by the player (for example, was the guess too high, too low, or exactly correct).
# Guess until the number has been guessed accurately or until there are no more chances.
# If the number has not been guessed, then the game displays the number that was not guessed to the player.
import random
flag=False
def numguess(i):
    if i==answer:
        print("you win !")
        flag=True
    elif i>answer:
        print("your guess is too high")
    elif i<answer:
        print("your guess is too low")
        
level = int(input("press 1 for easy and 2 for hard : "))
answer= random.randint(1,100)
if level == 1:
    chances_available = 10
    while chances_available > 0:
        i=int(input("guess a number : "))
        print(f"you have {chances_available-1} chances left")
        numguess(i)
        chances_available-=1
        if flag== True:
            break
    if flag==False:
        print("better luck next time")
        print(f"the number was {answer}")
    
elif level == 2:
    chances_available = 5
    while chances_available > 0:
        i=int(input("guess a number : "))
        print(f"you have {chances_available-1} chances left")
        numguess(i)
        chances_available-=1
        if flag== True:
            break
    if flag==False:
        print("better luck next time")
        print(f"the number was {answer}")
else:
    print("enter numbers properly")

   

