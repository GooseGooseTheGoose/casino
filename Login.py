print("Welcome to the computer!")
with open("Username1.txt",mode="r") as f:
    username1 = f.read()
with open("Password1.txt",mode="r") as f:
    password1 = f.read()
with open("Name1.txt",mode="r") as f:
    name1 = f.read()
with open("Username2.txt",mode="r") as f:
    username2 = f.read()
with open("Password2.txt",mode="r") as f:
    password2 = f.read()
with open("Name2.txt",mode="r") as f:
    name2 = f.read()
loggedIn = False
while loggedIn == False:
    passwordMaker=input("Type 1 to make a new login or 2 if you already have a login.\n")
    passwordMaker=int(passwordMaker)
    if passwordMaker == 1:
        if username1 != "":
            name2=input("What is your name?\n")
            with open("Name2.txt",mode="w") as f:
                f.write(name2)
            print("Hello ",name2,"!")
            username2=input("Please enter your new username:  ")
            with open("Username2.txt",mode="w") as f:
                f.write(username2)
            password2=input("Please enter your new password:  ")
            with open("Password2.txt",mode="w") as f:
                f.write(password2)
        if username1 == "":
            name1=input("What is your name?\n")
            with open("Name1.txt",mode="w") as f:
                f.write(name1)
            print("Hello ",name1,"!")
            username1=input("Please enter your new username:  ")
            with open("Username1.txt",mode="w") as f:
                f.write(username1)
            password1=input("Please enter your new password:  ")
            with open("Password1.txt",mode="w") as f:
                f.write(password1)
    if passwordMaker == 2:
        while True:
            usernameChecker1=input("Please enter your username:  ")
            passwordChecker1=input("Please enter your password:  ")
            if usernameChecker1 == username1:
                if passwordChecker1 == password1:
                    print("Welcome",name1,".")
                    loggedIn = True
                    break
                else:
                    print("Password is incorrect.")
                    print("You have 3 attempts left for ",username1,".")
                    passwordChecker1=input("Please enter your password:  ")
                    if passwordChecker1 == password1:
                        print("Welcome",name1,".")
                        loggedIn = True
                        break
                    else:
                        print("Password is incorrect.")
                        print("You have 2 attempts left for ",username1,".")
                        passwordChecker1=input("Please enter your password:  ")
                        if passwordChecker1 == password1:
                            print("Welcome",name1,".")
                            loggedIn = True
                            break
                        else:
                            print("Password is incorrect.")
                            print("You have 1 attempts left for ",username1,".")
                            passwordChecker1=input("Please enter your password:  ")
                            if passwordChecker1 == password1:
                                print("Welcome",name1,".")
                                loggedIn = True
                                break
                            else:
                                print("Password is incorrect.")
                                print("You have 0 attempts left for ",username1,".")
                                print("You have been locked out of",username1,".")
                                with open("Username1.txt",mode="w") as f:
                                    f.write("")
                                with open("Password1.txt",mode="w") as f:
                                    f.write("")
                                with open("Name1.txt",mode="w") as f:
                                    f.write("")
                                break
            if usernameChecker1 == username2:
                if passwordChecker1 == password2:
                    with open("Name2.txt",mode="r") as f:
                        name2 = f.read()
                    print("Welcome",name1,".")
                    loggedIn = True
                    break
                else:
                    print("Password is incorrect.")
                    print("You have 3 attempts left for ",username2,".")
                    passwordChecker1=input("Please enter your password:  ")
                    if passwordChecker1 == password1:
                        print("Welcome",name2,".")
                        loggedIn = True
                        break
                    else:
                        print("Password is incorrect.")
                        print("You have 2 attempts left for ",username2,".")
                        passwordChecker1=input("Please enter your password:  ")
                        if passwordChecker1 == password1:
                            print("Welcome",name2,".")
                            loggedIn = True
                            break
                        else:
                            print("Password is incorrect.")
                            print("You have 1 attempts left for ",username2,".")
                            passwordChecker1=input("Please enter your password:  ")
                            if passwordChecker1 == password2:
                                print("Welcome",name2,".")
                                loggedIn = True
                                break
                            else:
                                print("Password is incorrect.")
                                print("You have 0 attempts left for ",username2,".")
                                print("You have been locked out of",username2,".")
                                with open("Username2.txt",mode="w") as f:
                                    f.write("")
                                with open("Password2.txt",mode="w") as f:
                                    f.write("")
                                with open("Name2.txt",mode="w") as f:
                                    f.write("")
                                break
            if usernameChecker1 != username2:
                if usernameChecker1 != username2:
                    print("Username is invalid or nonexistant")
                
            
        




#chese is great
