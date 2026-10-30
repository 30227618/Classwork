#Week 4, Task 2
#Mohammed Ahmed

def authenticate(username, password):   #Defines the authenticate function and returns True or False depending on if credentials match
    correct_username = "admin"  #Sets the correct username
    correct_password = "admin123"   #Sets the correct password

    if username == correct_username and password == correct_password:
        return True #Returns true if the user entered username and password match with the correct values
    else:
        return False    #Returns false if they don't match

def main(): #Defines the main function
    while True: #Loops forever
        username = input("\nPlease enter the username: ")   #Asks the user for username
        password = input("Please enter the password: ") #Asks the user for password

        if authenticate(username, password):
            print("Login successful.")  #Calls the authenticate function, and if it returns true, then sends success to display
            break   #Breaks out of the while loop if authenticate returns True
        else:
            print("Login unsuccessful. Please try again.")  #If authenticate function returns False, then prints error message and repeats the whole program

if __name__ == "__main__":  #Checks if the script is being run directly
    main()