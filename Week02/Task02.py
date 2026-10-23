#Week 2, Task 2
#Mohammed Ahmed
#02/10/2026

def get_time():                                                             #Defines the function that gets the time from the user
    hours = int(input("Please enter the time in hours: "))                  #Gets the hour in GMT as a whole number
    while hours < 0 or hours > 24:                                          #Runs a loop to ensure that the hour entered by the user is between 0 to 23
        hours = int(input("Please enter a number between 0 - 23: "))        #Error message asking user to enter again if the hour is not between 0 and 23

    minutes = int(input("Please enter the time in minutes: "))              #Gets the minutes in GMT as a whole number
    while minutes < 0 or minutes > 59:                                      #Runs a loop to ensure that the minutes entered by the user are between 0 to 59
            minutes = int(input("Please enter a number between 0 - 59: "))  #Error message asking user to enter again if the minutes are not between 0 and 59
    return hours, minutes                                                   #Returns the GMT hour and minutes entered by the user

def give_cet_time(hours):       #Defines the function that turns GMT into CET
    hours = (hours + 1) % 24    #Adds one hour to the GMT time. % 24 makes it such if the hour goes above 23, then it resets it from 0
    return hours                #Returns the CET hour

def give_pst_time(hours):       #Defines the function that turns GMT into PST
    hours = (hours - 8) % 24    #Subtracts eight hours from the GMT time. % 24 makes it such if the hour goes above 23, then it resets it from 0
    return hours                #Returns the PST hours

def main():                             #Defines the main function
    hours, minutes = get_time()         #Calls the get_time function to get the GMT time from the user
    print("GMT:",hours,":",minutes)     #Prints the GMT time
    cet_hours = give_cet_time(hours)    #Calls the function to make GMT into CET time
    print("CET:",cet_hours,":",minutes) #Prints the CET time
    pst_hours = give_pst_time(hours)    #Calls the function to make GMT into PST time
    print("PST:",pst_hours,":",minutes) #Prints the PST time

if __name__ == "__main__":  #Checks if the script is being run directly
    main()                  #Calls the main function