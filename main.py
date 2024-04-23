#System packages
import os.path 


#External packages



#Imports of our own functions 

print("Welcome to 'A Study in Red' mistery game." )
print("Please choose your username: ") #input username 
print("You are detective who has been assigned to investigate the murder of mr. Otto, a rich old man, happened in his mansion." )
print("Your task is to gather evidence, question the suspects and catch the killer!")
print("Let's begin the investigation! \n")

print("What would you like to do?")

def options_menu (): 
    
    print("1. Investigate the crime scene. ")
    print("2. Question a suspect. ")
    print("3. review the evidence. ")
    print("4. Make an accusation! ")
    print("5. Quit the investigation. ")

    user_choice = input("Enter your selection: ")
    return user_choice 

choice=""

while choice != "5": 
    choice = options_menu()

    if choice == "1": 
        crime_scene ()

    elif choice == "2":
        question_suspect()

    elif choice == "3": 
        review_evidence()

    elif choice == "4": 
        accusation ()
    
    elif choice =="5": 
        print("You quite the investigation. ")

    else: 
        print("Please enter a number shown above. ")

print("Thank you for playing 'A study in Red'! ")


