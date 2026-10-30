#Week 4, Task 3
#Mohammed Ahmed

def calculate_failed_percentage():   #Defines the calculate_failed_percentage function
    no_failed_attempts = int(input("Please enter the number of failed attempts: ")) #Asks user for number of failed attempts
    no_total_attempts = int(input("Please enter the total number of attempts: "))   ##Asks user for number of total attempts

    failed_percentage = (no_failed_attempts/no_total_attempts) * 100    #Finds the percentage of failed attempts
    return failed_percentage    #Returns the percentage of failed attempts

def main(): #Defines the main function
    try:    #Tries to execute the code block and handles exceptions
        failed_percentage = calculate_failed_percentage()   #Calls the calculate_failed_percentage function and stores the result
    except ValueError:  #Handles the case where the user enters a non-numeric value
        print("Please enter numbers only.") #Prints an error message if the user enters a non-numeric value
        return  #Exits the function if an exception occurs
    except ZeroDivisionError:   #Handles the case where the user enters zero for total attempts
        print("Total login attempts cannot be zero.")   #Prints an error message if the user enters zero for total attempts
        return  #Exits the function if an exception occurs

    if failed_percentage >= 50:
        print("HIGH RISK")  #If the failed_percentage is higher than 50%, prints High Risk
    elif failed_percentage >= 25 and failed_percentage < 50:
        print("MEDIUM RISK")    #Prints Medium Risk if the failed_percentage is between 25% and 50%
    else:
        print("LOW RISK")   #Prints low risk if failed_percentage is less than 25%

if __name__ == "__main__":  #Checks if the script is being run directly
    main()