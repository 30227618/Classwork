#Week 3, Task 1
#Mohammed Ahmed
#09/10/2026

def get_password():                                 #Defines function to get password from user
    password = str(input("Enter your password: "))  #Asks user for password
    return password                                 

def analyse_password(password):         #Defines function to analyse password
    if len(password) < 8:
        print("Unsuitable password")    #Prints unsuitable password if password is less than 8 characters
        return None                     #Returns None if password is unsuitable

    is_digit = False                    #Defines variable to check if password contains a digit
    is_upper = False                    #Defines variable to check if password contains an uppercase letter
    is_lower = False                    #Defines variable to check if password contains a lowercase letter

    for character in password:          #Loops through each character in the password
        if character.isdigit():
            is_digit = True             #Sets is_digit to True if character is a digit
        elif character.isupper():
            is_upper = True             #Sets is_upper to True if character is an uppercase letter
        elif character.islower():
            is_lower = True             #Sets is_lower to True if character is a lowercase letter

    if is_digit == True and is_lower == True and is_upper == True:  #Checks if password meets all criteria
        print("Suitable password")                                  #Prints suitable password if all criteria are met
    else:
        print("Unsuitable password")                                #Prints unsuitable password if any criteria are not met

def main():                     #Defines main function
    password = get_password()   #Calls the get_password function
    analyse_password(password)  #Calls the analyse_password function

if __name__ == "__main__":  #Checks if the script is being run directly
    main()