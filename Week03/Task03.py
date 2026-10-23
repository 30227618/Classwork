#Week 3, Task 3
#Mohammed Ahmed
#09/10/2026

#Sets the security event message as a global variable
event_message = "Security Alert: Failed login attempt detected from IP address 192.168.1.25. The user account admin was targeted at 22:45. The server blocked the login attempt after an incorrect password was entered."
print(event_message)    #Prints event_message

def detect_failed():                        #Defines the detect_failed function
    if "failed" in event_message.lower():   #Changes all the letters in event_message to lowercase
        return True                         #Returns true if the word "failed" is in event_message
    else:
        return False                        #Returns false if not found

def detect_login():                         #Defines the detect_login function
    if "login" in event_message.lower():    #Changes all the letters in event_message to lowercase
        return True                         #Returns true if the word "login" is in event_message
    else:
        return False                        #Returns false if not found

def locate_ip():                                            #Defines the locate_ip function
    for word in event_message.split():                      #Loops for every word in event_message
        word = word.strip(".")                              #Removes the fullstop from every word
        dots = 0                                            #Sets number of dots to 0 to find the IP Address
        for char in word:                                   #Loops for every character in every word
            if char == ".":
                dots += 1                                   #Adds one to dots if a dot is found in a word
        if dots == 3 and word.replace(".", "").isdigit():   #If there are three dots in a character, and after removing the dots, all the characters are numbers, then it is an IP address
            return word

def main():                                                         #Defines main function
    if detect_failed() == True:
        print("\nWarning: A failed security event was detected.")   #Prints a warning message if the detect_failed function returns true
    if detect_login() == True:
        print("Login activity detected.")                           #Prints "login activity detected" if the detect_login function returns true
    ip_address = locate_ip()
    print("IP Address:", ip_address)                                #Prints the IP address

if __name__ == "__main__":  #Checks if the script is being run directly
    main()