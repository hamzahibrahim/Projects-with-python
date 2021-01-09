import random

print('--------------------')
name = input("Enter your name: ")
print("Welcome", name, "to the Rock Paper Scissors game -_-")
print('--------------------')

rules = '''
            ---
            This is the rules:
            if Rock and Paper Paper wins
            if Paper and Scissors Scissors wins
            if Rock and Scissors Rock wins

            You can only Enter:
            ['Rock','Paper','Scissors','r','p','s']
            anything from this list only
            if you want to see the rules just type rules
            ---
'''
print(rules)

list_for_user = ['Rock','Paper','Scissors','r','p','s']
list_for_computer = ['Rock','Paper','Scissors']

rerun = 'y'
while rerun == "y":
    try:
        com_choice = random.choice(list_for_computer)
        user_choice = input('Your turn \nRock, Paper, Scissors?: ')

        if com_choice == user_choice or com_choice[0].lower() == user_choice[0]:
            print('========================')
            if user_choice =='s':
                print('Draw\ncomputer was: ',com_choice,'and you was: Scissors')
                print('========================')
            if user_choice == 'r':
                print('Draw\ncomputer was: ',com_choice,'and you was: Rock')
                print('========================')
            if user_choice == 'p':
                print('Draw\ncomputer was: ',com_choice,'and you was: Paper')
                print('========================')
            else:
                print('Draw\ncomputer was: ',com_choice,'and you was: ',user_choice)
                print('========================')

        elif com_choice == 'Rock' and user_choice == 'Scissors' or com_choice == 'Rock' and user_choice == 's':
            print('========================')
            print('You lost!\ncomputer won\ncomputer was: ',com_choice,'and you was: Scissors')
            print('========================')
        elif com_choice == 'Scissors' and user_choice == 'Paper' or com_choice == 'Scissors' and user_choice == 'p':
            print('========================')
            print('You lost!\ncomputer won\ncomputer was: ',com_choice,'and you was: Paper')
            print('========================')
        elif com_choice == 'Paper' and user_choice == 'Rock' or com_choice == 'Paper' and user_choice == 'r':
            print('========================')
            print('You lost!\ncomputer won\ncomputer was: ',com_choice,'and you was: Rock')
            print('========================')

        elif com_choice == 'Scissors' and user_choice == 'Rock' or com_choice == 'Scissors' and user_choice == 'r':
            print('========================')
            print('You Won!\ncongratulations ',name,'\ncomputer was: ',com_choice,'and you was: Rock')
            print('========================')
        elif com_choice == 'Paper' and user_choice == 'Scissors' or com_choice == 'Paper' and user_choice == 's':
            print('========================')
            print('You Won!\ncongratulations ',name,'\ncomputer was: ',com_choice,'and you was: Scissors')
            print('========================')
        elif com_choice == 'Rock' and user_choice == 'Paper' or com_choice == 'Rock' and user_choice == 'p':
            print('========================')
            print('You Won!\ncongratulations ',name,'\ncomputer was: ',com_choice,'and you was: Paper')
            print('========================')


        elif user_choice not in  list_for_user and user_choice != 'rules':
            print('========================')
            print('Did u entr any of:\n[Rock,paper,Scissors] or [s,p,r] or rules\nCheck your spelling!')
            print('========================')

        rerun = input("Enter y to rerun or any thing else to end: ")
        print('=======================')
    except:
        print('somthing went wrong!!')
        rerun = input("Enter y to rerun or any thing else to end: ")
