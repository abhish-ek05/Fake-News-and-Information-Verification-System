# registration of new user 

def register():
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    
    # username and password validation

    if username and password :
        file = open("datausers.txt", "a")
        file.write(username + "," + password + "\n")
        file.close()

        print("Registration Successful")
        
    else:
        print("Username and Password cannot be empty")

## login function ---> when correct credentials are found then login

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    file = open("datausers.txt", "r")

    for line in file:
        user, pwd = line.strip().split(",")

        if user == username and pwd == password:
            file.close()
            print("Login Successful")
            return True

    file.close()
    print("Invalid Credentials")
    return False