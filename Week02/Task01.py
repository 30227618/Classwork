#Week 2, Task 1
#Mohammed Ahmed
#02/10/2026

def input_values():                                         #Defines the function to ask the user for both values
    value1 = int(input("Please enter the first value: "))   #Gets first value from user
    value2 = int(input("Please enter the second value: "))  #Get second value from user
    return value1, value2                                   #Returns both values

def add_values(value1, value2): #Defines the function to add both values
    return value1 + value2      #Adds the values and returns the sum

def multiply_values(value1, value2):    #Defines the function to multiply both values
    return value1 * value2              #Multiplies the values and returns the sum

def take_away_second(value1, value2):   #Defines the function to take away the second value from the first
    return value2 - value1              #Returns the difference

def take_away_first(value1, value2):    #Defines the function to take away the first value from the second
    return value1 - value2              #Returns the difference

def remainder_of_first(value1, value2): #Defines the function to divide both values
    return value1 % value2              #Divides both values and returns the remainder

def power_to_second(value1, value2):    #Defines the function to raise the first value to the power of the second
    return value1 ** value2             #Returns the result

def main():                         #Main function to call the functions and print the values
    value1, value2 = input_values() #Calls the input_values function to get both values from the user

    sum_of_values = add_values(value1, value2)  #Calls the function to add both values
    print(sum_of_values)                        #Prints the sum

    product_of_values = multiply_values(value1, value2) #calls the function to multiply both values
    print(product_of_values)                            #Prints the product

    difference_of_second = take_away_second(value1, value2) #Calls the function to subtract the second from the first
    print(difference_of_second)                             #Prints the difference

    difference_of_first = take_away_first(value1, value2)   #Calls the function to subtract the first from the second
    print(difference_of_first)                              #Prints the difference

    modulus_of_first = remainder_of_first(value1, value2)   #Calls the function to get the remainder when dividing the values
    print(modulus_of_first)                                 #Prints the remainder

    value1_power_value2 = power_to_second(value1, value2)   #Calls the function to raise the first to the power of the second
    print(value1_power_value2)                              #Prints the raised number

if __name__ == "__main__":
    main()