rerun = "y"
while rerun == 'y':
    print('=======================')
    email = input("Please enter your Email Address: ").strip()
    print('=======================')
    try:
        the_tag = email.index('@')
        username = email[:the_tag]
        domain = email[the_tag+1:]
        the_dot = email.index('.')
        domain_name = email[the_tag+1:the_dot]

        print('-----------------------')
        print("Email address: ", email)
        print("Username: ", username)
        print("Domain name (without . and the after it): ", domain_name)
        print("Domain name (with . and the after it): ", domain)
        print('-----------------------')
    except:
        print('Did u enclude the @!!!!!')    
    rerun = input('Enter y to rerun or anthing else to end: ')
