import random
from os import system, name

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

answer = random.randrange(1,10)
guesses = ""
msg = ""
low = 0
high = 99

while 1:    
    number = ""    
    proceed = False
    while not proceed:
        clear()
        print("A random number has been picked between 1 and 10. Can you guess it?\n"+"-"*50)
        if guesses != "":
            print(guesses)
        if msg != "":
            print(msg)
        number = input("Guess between 1 and 10: ")
        if not number.isnumeric():
            msg = number + " is not a number. Try again."
        else:
            guess = int(number)
            if guess < 1 or guess > 10:
                msg = number + " is not a choice. Try again."
            else:                
                proceed = True    
    if guess == answer:
        break
    elif guess > answer:
        if guess < high:
            high = guess        
        #msg = "Guess lower!"
    else:
        if guess > low:
            low = guess
        #msg = "Guess higher!"
    guesses = "The answer is " + (("greater than " + str(low)) if low > 0 else "") + ((" and ") if low > 0 and high < 99 else "") + (("less than "+str(high)) if high < 99 else "")

print("You got it!")
