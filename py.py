import random
playing = True
number = str(random.randint(10,20))
print("I will generate a number from 10 to 20, and you have to guess the number one digit at a time")
print("THE GAME ENDS WHEN U GET 1 HERO")
while playing:
    guess = input('give me your best guess OR ELSE ;c \n')
    if number == guess:
        print("YOU MAY OR MAY NOT WIN THE GAME STOP ASKING ME") 
        print("THE NUMBER WAS",number) 
        break

    else:
        print("YOUR GUESS IS WRONG TRY AGAIN DUMMY \n ")