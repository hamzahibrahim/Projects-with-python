import time

print('''
      Hi and welcome to the (Speed typing test)
      You are going to write a word and the program
      will calculate how much did you need to type 
      that word (in seconds)
      ''')

rerun = 'y'
while rerun == 'y':
    the_word = input(
        'Enter the word you want to test on \n(AFTER FINISHING THIS WORD THE TIMER STARTS!): ')
    while len(the_word) <= 1:
        print("You need two letter to calculate the time!")
        the_word = input(
            'Enter the word you want to test on \n(AFTER FINISHING THIS WORD THE TIMER STARTS!): ')
    time_start = time.time()
    typed_word = input(
        "Repeat the word with your typing speed to calculate the time: \n          ---")
    time_ended = time.time()
    while the_word != typed_word:
        print('Are you sure you picked this word to test on')
        time_start = time.time()
        typed_word = input(
            "Repeat the word with your typing speed to calculate the time:\n         ---")
        time_ended = time.time()
    time_taken = time_ended - time_start
    time_taken = float(time_taken)
    if the_word == typed_word:
        print("You took ", round(time_taken, 2)," seconds to type the word ", typed_word)

    rerun = input('Enter y to rerun anything else to end: ')



