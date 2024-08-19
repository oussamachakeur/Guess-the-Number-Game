import random
from replit import clear

print('hello to guess the number game ')
level = input("choose the level u wanna play (easy/hard): ").lower()
print('i m thinking of a number between 1 and 100')

def computer_guess():
    guess = list(range(101))
    computer_pick = random.choice(guess)
    return computer_pick
x= computer_guess()

if level == "easy":
    att = 10
    for _ in range (10):
        user = int(input("guess ur number "))
        if user == x :
            print('wow , u guessed correctly the correct guess is : '+ str(x))
            break
        elif user < x :
            print("its lower")
        elif user > x :
            print('its higher')
        else :
            print('wrong input')
        att= att-1
        print("you have "+str(att)+ ' attempts left for you')
elif level == "hard":
    att2 = 5
    for _ in range (5):
        user = int(input("guess ur number "))
        if user == x :
            print('wow , u guessed correctly the correct guess is : '+ str(x))
            break
        elif user < x :
            print("its lower")
        elif user > x :
            print('its higher')
        else :
            print('wrong input')
        att2 = att2 -1
        print("you have "+str(att2)+ ' attempts left for you')
    

