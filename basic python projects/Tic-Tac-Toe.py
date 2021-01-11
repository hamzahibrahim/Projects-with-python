import random

board = ["  " for i in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()    
    
    


def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("Your turn player {}".format(number))
    while True:
        choice = input("Enter your move (1-9): ")
        try:
            choice = int(choice)
            if choice < 10 and choice > 0:
                if board[choice - 1] == "  ":
                    board[choice - 1] = icon
                    break
                else:
                    print("\nThat space is taken!")
            else:
                print('Please type a number between [1-9]!')        
        except:
            print('Did you type a number?')

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
       (board[3] == icon and board[4] == icon and board[5] == icon) or \
       (board[6] == icon and board[7] == icon and board[8] == icon) or \
       (board[0] == icon and board[3] == icon and board[6] == icon) or \
       (board[1] == icon and board[4] == icon and board[7] == icon) or \
       (board[2] == icon and board[5] == icon and board[8] == icon) or \
       (board[0] == icon and board[4] == icon and board[8] == icon) or \
       (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False


def is_draw():
    if "  " not in board:
        return True
    else:
        return False

def two_player_mode():
    global board
    board = ["  " for i in range(9)]
    while True:
        print_board()
        player_move("X")
        print_board()
        if is_victory("X"):
            print("X Wins! Congratulations!")
            break
        elif is_draw():
            print("Its a draw!")
            break
        player_move("O")
        if is_victory("O"):
            print_board()
            print("O Wins! Congratulations!")
            break
        elif is_draw():
            print("Its a draw!")
            break

def computer_move():
    icon = 'O'
    go = True
    while go == True:
        computer_choice = random.randint(0, 8)
        if board[computer_choice] == "  ":
            board[computer_choice] = icon
            go = False

def one_player_mode():
    global board
    board = ["  " for i in range(9)]
    while True:
        print_board()
        player_move('X')
        print_board()
        if is_victory("X"):
            print("You Win! Congratulations!")
            break
        elif is_draw():
            print("Its a draw!")
            break
        computer_move()
        if is_victory("O"):
            print_board()
            print("You lost!")
            break
        elif is_draw():
            print("Its a draw!")
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
rerun = 'y'      
while rerun == 'y':
    if rerun.lower() == 'y':
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' '] 
        print('--------------------')
        print('Please choose which mode you want to play')
        print('''
                1.One Player Game
                2.Two Player Game     
                ''')
        j = input('[1/2]: ')
        if j == '1':
            one_player_mode()
        elif j == '2':
            two_player_mode()
        else:
            print('That means nothing bye!')
            break    
    else:
        break
    rerun = input("Do you want to play y for yes anything else will end: ")
