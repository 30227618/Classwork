#Week 2, Task 3
#Mohammed Ahmed
#02/10/2026

def get_eggs():                                                     #Defines the function to get the number of eggs from user
    no_of_eggs = int(input("Please enter the number of eggs: "))    #Asks the user to enter the number of eggs
    while not no_of_eggs > 0:                                       #Runs a loop asking for a suitable number incase the user enters 0 or a negative number
        int(input("Please enter a suitable number: "))              
    return no_of_eggs                                               #Returns the number of eggs

def calc_eggs(no_of_eggs):                      #Defines the function to calculate gross, dozen and single eggs
    remaining_eggs = no_of_eggs % 144           #Gets the remaining eggs after putting them into grosses
    gross_eggs = no_of_eggs // 144              #Gets the number of gross eggs
    dozen_eggs = remaining_eggs // 12           #Gets the number of dozen eggs
    single_eggs = remaining_eggs % 12           #Gets the number of single eggs
    return gross_eggs, dozen_eggs, single_eggs  #Returns all the egg types

def main():                                                     #Defines the main function
    no_of_eggs = get_eggs()                                     #Calls the function get_eggs
    gross_eggs, dozen_eggs, single_eggs = calc_eggs(no_of_eggs) #Calls the function calc_eggs
    print("Gross eggs:",gross_eggs)                             #Prints the number of gross eggs
    print("Dozen eggs:",dozen_eggs)                             #Prints the number of dozen eggs
    print("Single eggs:",single_eggs)                           #Prints the number of single eggs

if __name__ == "__main__":  #Checks if the script is being run directly
    main()                  #Calls the main function