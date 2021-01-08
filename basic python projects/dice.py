import random
print("This is a dice stimulator")
rerun = "y"
while rerun == "y":
    number = random.randint(1,6)
    if number == 1:
        print("----------")
        print("|        |")
        print("|    O   |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O    O |")
        print("|    O   |")
        print("| O    O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    else:
        print("rerun the program")
    rerun = input("Enter y to rerun or any thing else to end: ")
