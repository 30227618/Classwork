#Week 3, Task 4
#Mohammed Ahmed
#09/10/2026

import random                   #Imports the random module for generating random numbers
from datetime import datetime   #Imports the datetime module for working with dates and times
import socket                   #Imports the socket module for network-related operations

def login():                                                        #Defines the login function
    correct_password = "admin"                                      #Sets the correct password
    password_attempt = ""                                           #Initializes the password attempt variable

    username = input("Please enter the username: ")                 #Asks the user for their username
    password_attempt = input("Please enter the correct password: ") #Asks the user to enter the password
    while password_attempt != correct_password:                     #Checks if the entered password is incorrect
        #If the password is incorrect, it generates and prints a random event ID, the username, an unsuccessful login message, the IP address, timestamp, and asks the user to enter the username and password again.
        get_event_id()  
        print("Username:", username, "\nLogin: Unsuccessful")
        ip_address()
        timestamp()
        username = input("\nPlease enter the username: ")
        password_attempt = input("Please enter the correct password: ")
    else:
        #If the password is correct, it generates and prints a random event ID, the username, a successful login message, the IP address, and timestamp.
        get_event_id()
        print("Username:", username, "\nLogin: Successful")
        ip_address()
        timestamp()


def get_event_id():                         #Defines the get_event_id function
    event_id = random.randint(1000, 9999)   #Generates a random event ID between 1000 and 9999
    print("\nEvent ID:", event_id)          #Prints the generated event ID

def timestamp():                                                #Defines the timestamp function
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    #Gets the current date and time
    print("Timestamp:", timestamp)                              #Prints the current date and time

def ip_address():   #Defines the ip_address function to get the local IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    print("IP Address:", ip_address)
    s.close()

def main(): #Defines main function
    login()

if __name__ == "__main__":  #Checks if the script is being run directly
    main()