#Week 2, Task 7
#Mohammed Ahmed
#02/10/2026

def fibonacci():                                                #Defines the function to calculate and print the fibonacci sequence numbers
    first_no = 0                                                #Assigns 0 to first_no
    second_no = 1                                               #Assigns 1 to second_no

    for loop in range(1, 21):                                   #Loops 20 times
        print(first_no, end=", ")                               #Prints the first number on the same line with a comma

        first_no, second_no = second_no, first_no + second_no   #Carries out the right hand side first and then assigns the values. This prevents the old values from being overridden by the new values


def main():     #Defines the main function
    fibonacci() #Calls the fibonacci function

if __name__ == "__main__":  #Checks if the script is being run directly
    main()