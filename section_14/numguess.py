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
else:
    print("enter numbers properly")

   

