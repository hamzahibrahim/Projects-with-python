print('--------------------')
name = input("Enter your name: ")
print("Welcome", name, "to my number guessing game -_-\n"
"you start and your score is 100 and every mistake you will lose 10 points good luck -_- ")
print('--------------------')

import random
score = 100
the_number = random.randint(1,10)
rerun = "y"
while rerun == "y":
    try:
        user_guess = int(input('guess a number between 1 to 10: '))
        while True:
            if score <= 0 : 
               print('sorry you lost your score is: ',score)
               break
            if (user_guess == the_number):
                print('--------------------')
                print('well done that\'s correct! the number was: ', the_number)
                print('Your score is: (',score,') well done!')
                break
            if (user_guess > the_number):
                print("Wrong! You guessed too high!!!!!")
                score -= 10
                print('--------------------')
                user_guess = int(input("Try to guess the number:"))
            if (user_guess < the_number):
                print("Wrong! You guessed too low!!!!!")
                score -= 10
                print('--------------------')
                user_guess = int(input("Try to guess the number:"))
        rerun = input("Enter y to rerun or any thing else to end: ")
        if rerun == 'y':
            score = 100
            the_number = random.randint(1, 10)
    except:
        print('you didint enter a number!!!!')
        print('--------------------')





