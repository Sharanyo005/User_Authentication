from time import sleep as s
def signUp(username, password):
    a = open('database.txt', 'a')
    a.close()
    with open('database.txt', 'r') as f:
        txt = f.readlines()   
    if f"{username},{password}\n" in txt:
        print("Processing...")    
        s(1)
        print("You have already Signed Up...try to Log in")
    if f"{username},{password}\n" not in txt:
        print("Processing...")
        s(1)
        with open("database.txt", 'a') as f:
            f.write(f'{username},{password}\n')
        print("You have Successfully Signed Up!")
def logIn(username, password):
    with open('database.txt', 'r') as f:
        txt = f.readlines()
    if f"{username},{password}\n" in txt:
        print("Correct!") 
        id = txt.index(f"{username},{password}\n")
        print(f'Your id is:{id}')
        print("Processing...")
        s(1)
        print("You have Successfully Logged In!")
    elif f"{username},{password}\n" not in txt:
        print("Processing...")
        s(1)
        print("Incorrect Username or Password...(May be you haven't signed up yet)")
while True:
    choice = input('''
If You are new here, Sign Up type 'S' to Sign Up, Or If You Have Already Signed Up, type 'L' to Log in...!

Sign up / Log in [S/L]: ''')
    if choice.upper() == 'S':
        print('''
                SIGN UP      
        ''')
        uname = input("Username: ")
        s(1)
        pswd = input("Password: ")
        signUp(uname, pswd)
        break
    elif choice.upper() == 'L': 
        print('''
                LOG IN      
        ''')
        uname = input("Username: ")    
        s(1)
        pswd = input("Password: ")
        s(1)
        logIn(uname,pswd)
        break 
