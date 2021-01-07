#---------------------
import random
#---------------------

print('--------------------')
name = input("Enter your name: ")
print("Welcome", name, "to the Text-based Adventure Game -_-")
print('--------------------')

#---------------------------------

#math room
def math_room():
    print(' You have chosen the math room\n',
    'Simply there is a question answer it\n',
    'if you choose a incorrect answer more than 3 times\n' ,
    'your score well be bad Good luck ',name)
    
    print('------------------')
    again = "y"
    while again == "y":          
        global score
        global questionnum
        score = 0
        questionnum = 0

        while questionnum < 5:
            questionnum = questionnum+1
            operatorlist = ['+', '-', '*']
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            ope = random.choice(operatorlist)

            if ope == '-' and num2 > num1:
                expr = "{}{}{} \n".format(num2, ope, num1)
            else:
                expr = "{}{}{} \n".format(num1, ope, num2)
            answer = eval(expr)
            enter_answer = 1

            while enter_answer == 1:
                try:
                    useranswer = int(input(expr))
                    enter_answer = 0
                except ValueError:
                    print("that was not a number re enter your answer")
            answer = int(answer)

            if useranswer == answer:
                print("well done")
                score = score+1
                print(" ")
            else:
                print("incorrect the correct answer is {} ".format((answer)))
        if score >= 3:
            print("finished, " + name + ". You got ", score, ' answers correct out of 5 (★‿★) Well Done!')
        else:
            print("finished, " + name + ". You got ", score, ' answers correct out of {} (That is bad!!)'.format(questionnum))
        again = input("Enter y to restart again in the math room or any thing else to end: ")
        print('---------------------------')

#---------------------------------
# forest room
directions = ["left", "right", "forward", "backward"]
answer_list = ["yes", "no"]
def forest_room():  
    rerun = "y"
    while rerun == "y":

        print(' You have chosen the forest room\n',
        'You are in a forest!!!'
        'Simply there are questions that help you where to go  \n',
        'try to go find your way through '
        'Good luck ',name)

        user_answer = ""
        while user_answer not in answer_list:
            user_answer = input(" Would you like to step into the forest?\n (yes/no)\n")
            if user_answer == "yes":
                print("You head into the forest. You hear crows cawwing in the distance.")
            elif user_answer == "no":
                print("You are not ready! Goodbye, " , name )
                print('-----------------------------')
                rerun = input("Enter y to rerun the forest room or any thing else to end: ")
                print('-----------------------------')
                if rerun == "y":
                    user_answer = ""
            else:
                print("Answer yes or no only.\n")

        user_answer_ = ""
        while user_answer_ not in directions:
            print("To your left There is a lion!.")
            print("If you go right you will go deeper in the forest.")
            print("There is a wall in front of you.")
            print("If you go backwards you well exit.\n")
            print('-----------------')
            print('read the above words then answer')
            user_answer_ = input("What direction do you want to go to?\nleft/right/forward/backward\n")
            if user_answer_ == "left":
                print("The lion eats you!! hahah you are died " + name)
                print('-----------------------------')
                rerun = input("Enter y to rerun the forest room or any thing else to end: ")
                print('-----------------------------')
            elif user_answer_ == "right":
                print("You went deeper into the forest.\n")
                print('-----------------------------')
                rerun = input("Enter y to rerun the forest room or any thing else to end: ")
                print('-----------------------------')
            elif user_answer_ == "forward":
                print("You can't go there is a wall.\n")
                print('-----------------------------')
                rerun = input("Enter y to rerun the forest room or any thing else to end: ")
                print('-----------------------------')
            elif user_answer_ == "backward":
                print("You are now out the forest Goodbye, " + name )
                print('-----------------------------')
                rerun = input("Enter y to rerun the forest room or any thing else to end: ")
                print('-----------------------------')
            else:
                print("please enter left/right/forward/backward(you can the first letter only) .\n")
                print('-----------------------------')

#---------------------------------
#one question room
def one_question_room():
    repeat = 'y'
    while repeat == 'y':        
        print(' You have chosen the one question room\n',
            'Simply there is a question answer it\n',
            '------------------')
        programming = input('Do you like programming with python: (answer yes or no only!) ')  
        if programming == 'yes':
            print('Good me too!!')
            print('---------------')
            repeat = input("Enter y to rerun the one question room or any thing else to end: ")
            print('---------------')
        elif programming == 'no':
            print('why it is a good langauge tho!!')
            print('---------------')
            repeat = input("Enter y to rerun the one question room or any thing else to end: ")
            print('---------------')
        else:
            print('I said yes or no only did i!')  
            print('---------------')
            repeat = input("Enter y to rerun the one question room or any thing else to end: ")
            print('---------------')

#---------------------------------
#questions room
def questions_room():
    i = 'y'
    while i == 'y':
        print('You have chosen the questions room\n',
        'Simply there is some questions answer them\n',
        'Good luck ',name)
        print('-------------')   
        first = input('what is your fav food? ')
        if first != '':
            print('Good')
        else:
            print('No answer!')  
        print('-------------')
        second = input('do you whatch football? ')
        if second != '':
            print('Good')
        else:
            print('No answer!')
        print('-------------')
        third = input('Realy this is a math expretion so answer --\n  33 - 12? ')  
        if third == '21':
            print('well done! that is correct')        
        else:
            print('that is a wrong answer')
        print('-------------')
        fourth = input('do you like ice cream? ')
        if fourth != '':
            print('Good')
        else:
            print('No answer!')
        print('-------------')      
        last_question = input('did you enjoy this room? (answer yes or no only) ')    
        if last_question == 'yes':
            print('good you can restart it!')
        elif last_question == 'no':
            print('why! never mind you can choose a diffrent room!')
        else:
            print('I said yes or no only!!!!!!!!!!!!!!')
        i = input("Enter y to rerun the question room or any thing else to end: ")
        print('---------------')

#---------------------------------

again_ = 'y'
while again_ == 'y':
    user_choice = ''
    while user_choice != '1' or '2' or '3' or '4':
        print(' math room = 1 \n',
        'forest room = 2\n',
        'one_question_room = 3\n',
        'questions_room = 4\n',
        'end to exit!\n')
        user_choice = input("Enter option number(from 1-4 only) or end to exit!: ")
        if user_choice == '1':
            math_room()
            print('===========================')
            again_ = input("Enter y to rerun the whole game or any thing else to end: ")
            if again_ != 'y':
                exit()
        elif user_choice == '2':
            forest_room()
            print('===========================')
            again_ = input("Enter y to rerun the whole game or any thing else to end: ")
            if again_ != 'y':
                exit()
        elif user_choice == '3':
            one_question_room()
            print('===========================')
            again_ = input("Enter y to rerun the whole game or any thing else to end: ")
            if again_ != 'y':
                exit()
        elif user_choice == '4':
            questions_room()
            print('===========================')
            again_ = input("Enter y to rerun the whole game or any thing else to end: ")
            if again_ != 'y':
                exit()
        elif user_choice == 'end':
            exit()        
        else:
            print('did you enter from 1-4!!!! no promblem try again\n')






