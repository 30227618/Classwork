#Week 2, Task 6
#Mohammed Ahmed
#02/10/2026

def check_password(password):                                               #
    user_input = str(input("Please enter the password: "))                  #
    while user_input != password:                                           #
        user_input = str(input("Incorrect password. Please try again: "))   #
    print("Access Granted!")                                                #

def main():                     #
    password = "Hello_World009" #
    check_password(password)    #

if __name__ == "__main__":  #Checks if the script is being run directly
    main()                  #Calls the main function