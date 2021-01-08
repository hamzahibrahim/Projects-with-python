print('-----------------------')
val = input('first number: ')
print('-----------------------')
val1 = input('second number: ')
val = int(val)
val1 = int(val1)
print('-----------------------')
type = input('choose one (+,/,*,-): ')
if (type == '+'):
    print('answer is: ',val + val1)
elif (type == '-'):
    print('answer is: ',val - val1)
elif (type == '/'):
    print('answer is: ',val / val1)
elif (type == '*'):
    print('answer is: ',val * val1)
else:
    print('rerun the program')
print('-----------------------')
