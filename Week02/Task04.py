#Week 2, Task 4
#Mohammed Ahmed
#02/10/2026

def get_no():                                                       #Defines the function to get a number from user
    number = int(input("Please enter a number from 1 - 100: "))     #Asks user to enter a number between 1 - 100
    if number < 1 or number > 100:                                  #Checks if number is between 1 - 100
        print("Error. You did not enter an appropriate number.")    #Displays error message if number is not between 1 - 100
        return None                                                 #Returns 'None' if number is not between 1 - 100
    else:                                                           
        return number                                               #Returns the number if it is between 1 - 100

def check_even_or_odd(number):                      #Defines the function to check if the number is even or odd
    remainder = number % 2                          #Divides the number by 2
    if remainder == 0:                              
        print("You have entered an even number.")   #If the remainder is 0, sends a message for even number
    elif remainder == 1:                            
        print("You have entered an odd number.")    #IF the remainder is 1, sends a message for odd number

def main():                     #Defines the main function
    number = get_no()           #Calls the get_no function
    if number is None:          #Checks to see if the number returned is 'None'
        return                  #Ends the function if number is 'None'
    
    check_even_or_odd(number)   #Calls the check_even_or_odd function

if __name__ == "__main__":  #Checks if the script is being run directly
    main()                  #Calls the main function