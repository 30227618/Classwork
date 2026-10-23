#Week 2, Task 8
#Mohammed Ahmed
#02/10/2026

password = "Hello_World09"  #Sets the correct password for the entire program

def authenticate_user():                                                            #Defines the function to authenticate user login
    user_password = input("Please enter the password or type 'exit' to leave: ")    #Receives password from user or logs user out
    if user_password == "exit":                                                     
        return False                                                                #If the user enters 'exit', it returns False and the function ends
    else:
        while user_password != password:                                            #Runs a loop to get the correct password from the user
            user_password = input("Incorrect. Please enter the correct password: ") 
            if user_password == "exit":                                             
                return False                                                        #If the user enters 'exit', it returns False and the function ends
        return True                                                                 #Returns True when the user enters the correct password

def security_event_counter():                                           #Defines the security event counter function
    correct_guesses = 0                                                 #Sets the variable correct_guesses to 0
    wrong_guesses = 0                                                   #Sets the variable wrong_guesses to 0

    print("\nRunning Security Event Counter...")                        
    for loop in range(1, 11):                                           
        user_password = input(f"{loop}. Please enter the password: ")   #Runs a loop 10 times, asking the user for the password
        if user_password == password:                                   
            correct_guesses += 1                                        #If the correct password is entered, adds 1 to correct_guesses
        else:
            wrong_guesses += 1                                          #If the wrong password is entered, adds 1 to wrong_guesses

    print(f"You guessed the correct password {(correct_guesses/10) * 100}% of the time.")                               #Calculates and displays the percentage of how many times the correct password was entered
    print(f"You entered the correct password {correct_guesses} times, and the wrong password {wrong_guesses} times.")   #Displays the number of times the user entered the correct and wrong password

    if input("Press enter to proceed or type 'exit' to exit: ") == "exit":  #Asks the user if they want to proceed or exit
        return False                                                         #If the user enters 'exit', it returns False and the function ends

def brute_force_simulation():                                               #Defines the brute force simulation function
    no_of_attempts = 0                                                      #Initializes the number of attempts variable

    user_password = input("Please enter the password: ")                    #Gets the password from the user
    while no_of_attempts < 11 and user_password != password:                #Runs a loop to get the correct password from the user, with a maximum of 10 attempts
        user_password = input("Incorrect. Please try again: ")              
        no_of_attempts += 1                                                 #Adds 1 to the no_of_attempts variable each time the user enters the wrong password

    print(f"\nYou entered the wrong password {no_of_attempts} time(s).")    #Displays the number of times the user entered the wrong password

    proceed = input("Press enter to proceed or type 'exit' to exit: ")      #Asks the user if they want to proceed or exit
    if proceed == "exit":                                                   #If the user enters 'exit', it returns False and the function ends
        return False

def login_authentication():                                                         #Defines the login authentication function
    loop = 0

    username = input("Please enter your username: ")                                #Gets the username from the user
    user_password = input("Please enter your password: ")                           #Gets the password from the user

    while user_password != password and loop < 2:                                   #Runs a loop to get the correct password from the user, with a maximum of 2 attempts
        user_password = input("Incorrect password. Please try again: ") 
        loop += 1                                                                   #Adds 1 to the loop variable each time the user enters the wrong password

    if user_password == password:
        print("Access granted.")                                                    #Displays a message if the user enters the correct password
    else:
        print("Too many incorrect login attempts. Account frozen for 24 hours.")    #Displays a message if the user enters the wrong password 3 times

    proceed = input("Press enter to proceed or type 'exit' to exit: ")              #Asks the user if they want to proceed or exit
    if proceed == "exit":                                                           #If the user enters 'exit', it returns False and the function ends
        return False

def main():                                                         #Defines the main function that runs the program
    if authenticate_user() == False:                                #If the user enters 'exit' during the authentication process, it returns False and the program ends
        return

    while True:                                                                                                         #Runs a loop to display the menu options and get the user's choice
        print("\nPlease choose any of the following options by typing in the corresponding number.")    
        print("\n1. Security Event Counter", "\n2. Brute-Force Simulation", "\n3. Login Authentication", "\n4. Exit")   #Displays the menu options for the user to choose from
    
        user_choice = int(input("\nPlease choose an option: "))     #Gets the user's choice
        if user_choice == 1:
            if security_event_counter() == False:                   #Runs the security event counter function and checks if the user wants to exit
                print("\nThank you for using the security tool.")   #Exits the program if the user enters 'exit' during the security event counter process
                return
        elif user_choice == 2:  
            if brute_force_simulation() == False:                   #Runs the brute force simulation function and checks if the user wants to exit
                print("\nThank you for using the security tool.")   #Exits the program if the user enters 'exit' during the brute force simulation process
                return           
        elif user_choice == 3:
            if login_authentication() == False:                     #Runs the login authentication function and checks if the user wants to exit
                print("\nThank you for using the security tool.")   #Exits the program if the user enters 'exit' during the login authentication process
                return
        elif user_choice == 4 or False: 
            print("\nThank you for using the security tool.")       #Exits the program if the user enters 'exit' during the menu options process
            return

if __name__ == "__main__":  #Checks if the script is being run directly
    main()