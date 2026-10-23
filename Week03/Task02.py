#Week 3, Task 2
#Mohammed Ahmed
#09/10/2026

def validate_password():    #Defines the validate_password function

    #Sets the values of all the variables to the NOT equal what is required in the password
    min_length = False
    one_upper = False
    one_lower = False
    special_chars = False
    is_space = False        #Set to false, which is required
    digits = 0

    while min_length == False or one_lower == False or one_upper == False or special_chars == False or is_space == True or digits < 2:  #Loops until password fulfills all these requirements

        #Resets the variables everytime the loop restarts
        min_length = False
        one_upper = False
        one_lower = False
        special_chars = False
        is_space = False
        digits = 0

        password = input("Please enter a suitable password: ")  #Gets password from user
        if len(password) >= 10:
            min_length = True                                   #If the number of characters is 10 or more, then sets min_length to true

        for character in password:                              #Loops for every character in the password
            if character.isdigit():
                digits += 1                                     #Adds one to digits everytime a digit is detected
            elif character.isupper():
                one_upper = True                                #Sets one_uppern to true as soon as an uppercase letter is detected
            elif character.islower():
                one_lower = True                                #Sets one_lower to true as soon as a lowercase letter is detected
            elif character == " ":
                is_space = True                                 #If a space is detected, is_space becomes true and the program asks for another password
            elif character == "!" or "@" or "#" or "$" or "%":
                special_chars = True                            #Sets special_chars to true if any one from !, @, #, $, % is detected

    print("You have entered a suitable password.")              #Prints this when a suitable password is detected

def main():             #Defines main function
    validate_password() #Calls the validate password function

if __name__ == "__main__":  #Checks if the script is being run directly
    main()