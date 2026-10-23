#Week 2, Task 5
#Mohammed Ahmed
#02/10/2026

def get_no():                                       #Defines the function to get a number from the user
    number = int(input("Please enter a number: "))  #Asks the user for a number
    return number                                   #Returns the number

def display_table(number):                      #Defines the function to calculate and display the multiplication table
    for n in range(1,11):                       #Runs a loop 10 times
        print(f"{number} x {n} = {number*n}")   #Displays the number and what it is multiplied with and the product

def main():                 #Defines the main function
    number = get_no()       #Calls the get_no function
    display_table(number)   #Calls the display_table function

if __name__ == "__main__":  #Checks if the script is being run directly
    main()                  #Calls the main function