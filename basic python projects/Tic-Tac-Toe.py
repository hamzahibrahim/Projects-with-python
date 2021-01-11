import random

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']       
       
def Draw_Board():    
    print(" {} | {} | {} ".format(board[0],board[1],board[2]))    
    print("___|___|___")    
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("___|___|___")    
    print(" {} | {} | {} ".format(board[6],board[7],board[8]))    
    print("   |   |   ")      

def is_victory(l,b=board):
    return ((b[0] == l and b[1] == l and b[2] == l) or
            (b[3] == l and b[4] == l and b[5] == l) or
            (b[6] == l and b[7] == l and b[8] == l) or
            (b[2] == l and b[3] == l and b[6] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[0] == l and b[4] == l and b[8] == l) or
            (b[2] == l and b[4] == l and b[6] == l))

def is_tie(b=board):
    return ((b[0] != ' ' and b[1] != ' ' and b[2] != ' ' and b[3] != ' ' and b[4] != ' ' and b[5] != ' ' and b[6] != ' ' and b[7] != ' ' and b[8] != ' ' )\
            and(not is_victory('X') and not is_victory('O')))

def space_is_free(pos):
    return board[pos] == ' '

def Player_move(): 
    go = True
    while go: 
        user_choice = input('Please enter a number between [1-9]: ')
        try:
            user_choice = int(user_choice)
            if user_choice > 0 and user_choice < 10:
                user_choice -= 1
                if space_is_free(user_choice):
                    board[user_choice] = 'X'
                    go = False
                else:
                    print('This space is Taken!')    
            else:
                print('Did you type between [1-9]?')    

        except :
            print('Did you type a number Please type a number: ')

def computer_move():
    go = True
    while go: 
        computer_choice = random.randint(1,9)
        computer_choice -= 1
        if is_tie():
            go = False
            break  
        elif is_victory('X') or is_victory('O'):
            go = False
            break
        elif space_is_free(computer_choice):   
            board[computer_choice] = 'O'
            go = False
            break

def one_player_mode():
    print('You have picked the one player mode, you are X computer is O -_-')
    i = input('Do you want to start y for yes anything else computer will start: ')
    if i.lower() == 'y':
        while True:
            Draw_Board()
            Player_move()
            if is_victory('X')and is_tie() :
                Draw_Board()
                print("\nYou win Well Done!")
                break
            elif is_victory('O') and is_tie():
                Draw_Board()
                print("\nYou lost!")
                break               
            if is_victory("X"):
                Draw_Board()
                print("\nYou win Well Done!")
                break
            elif is_tie():
                Draw_Board()
                print("Its a Tie Game!")
                break
            computer_move()
            if is_victory("O"):
                Draw_Board()
                print("\nYou lost!")
                break
            elif is_tie():
                Draw_Board()
                print("Its a Tie Game!")
                break
            elif is_victory('O') and is_tie():
                Draw_Board()
                print("\nYou lost!")
                break  
    else:
        while True:
            computer_move()
            Draw_Board()
            if is_victory('O') and is_tie():
                Draw_Board()
                print("\nYou lost!")
                break  
            elif is_victory("O"):
                Draw_Board()
                print("\nYou lost!")
                break
            if is_victory("X"):
                Draw_Board()
                print("\nYou win Well Done!")
                break
            elif is_tie():
                Draw_Board()
                print("Its a Tie Game!")
                break
            Player_move()
            if is_victory('X') and is_tie():
                Draw_Board()
                print("\nYou win Well Done!")
                break
            if is_victory("X"):
                Draw_Board()
                print("\nYou win Well Done!")
                break
            elif is_victory("O"):
                Draw_Board()
                print("\nYou lost!")
                break
            elif is_tie():
                Draw_Board()
                print("Its a Tie Game!")
                break

 

def player_move_in_two_player_mode(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2      
    print("Your turn player {}".format(number))
    while True:
        choice = input("Enter your move (1-9): ")
        try:
            choice = int(choice)
            if choice > 0 and choice < 10:
                choice -= 1
                if space_is_free(choice):
                    board[choice] = icon
                    break
                else:
                    print("That space is taken!")
            else:
                print('Did you type between [1-9]?')
        except :
            print('Did you type a number Please type a number: ')    


def two_player_mode():
    print('You have picked the Two player mode, First one is: (X) And second one is: (O) -_-')
    while True:
        Draw_Board()
        player_move_in_two_player_mode("X")
        Draw_Board()
        if is_victory("X"):
            print("X Wins! Congratulations!")
            break
        elif is_tie():
            print("Its a Tie Game!")
            break
        player_move_in_two_player_mode("O")
        if is_victory("O"):
            Draw_Board()
            print("O Wins! Congratulations!")
            break
        elif is_tie():
            print("Its a Tie Game!")
            break

#==============================
name = input('Please enter your name: ')
print('''
    Welcome {} to the Tic-Tac-Toe Game!
    you are going to choose if 
    you want to play against a 
    computer or play with your 
    friend so the Rules are:
    ==========================
    #The game is played on a grid that's 3 squares by 3 squares.
    #You are X (The first player), your friend (or the computer in this case) is O. ...
    #The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.
    #When all 9 squares are full, the game is over.
    ==========================
    Good Luck!
        '''.format(name))


print('Please choose which mode you want to play')
print('''
        1.One Player Game
        2.Two Player Game     
        ''')
j = input('Please choose [1-2]: ')
if j == '1':
    print('====================')
    one_player_mode()  
elif j == '2':
    print('====================')
    two_player_mode()
else:
    print('OK u did\'nt type 1 or 2 so Goodbye!')
