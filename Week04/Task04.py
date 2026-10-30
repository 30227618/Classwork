#Week 4, Task 4
#Mohammed Ahmed

def validate_ip(ip):    #Defines the validate_ip function
    ip = ip.strip() #Removes spaces from the beginning and end of the user input
    if "." not in ip:
        return False    #Returns false if there is no . in the user input
    elif ip.count(".") != 3:
        return False    #Counts the number of dots in the input. If it is not equal to 3, then it is not an ip address and returns false

    parts = ip.split(".")   #Splits the ip address based on the number of .
    if len(parts) != 4:
        return False    #If the number of parts after splitting is not 4, then it is not an ip address and returns false

    for part in parts:  #Loops for every part of the ip address
        if not part.isdigit():  
            return False    #Returns false if the part is not digits
        number = int(part)  #Converts the part to an integer
        if number < 0 or number > 255:
            return False    #If the converted integer is not between 1 and 255, returns false

    return True #Returns true if all the above conditions are met

def main(): #Defines the main function
    ip_address = input("Please enter the IP Address: ") #Asks the user for an ip address
    if validate_ip(ip_address):
        print("Valid IP Address")   #Calls the validate_ip function, and prints valid if the ip address is valid
    else:
        print("Invalid IP Address") #Prints invalid if the ip address is invalid

if __name__ == "__main__":  #Checks if the script is being run directly
    main()