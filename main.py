#System packages
import os.path 


#External packages


#Imports of our own functions 
# from notebook_functions import add_note, remove_note 
from crime_scene import evidence 
from suspects_list_2 import suspects 
# from suspects_list import suspects
# from accusation import catch_killer

print("=================================================================== A STUDY IN RED ==============================================================================")
print("\nWelcome to 'A Study in Red' mistery game." )

username = input("\nPlease choose your username: ") #input username 

print("You are detective" + " "+ username + " ,who has been assigned to investigate the murder of mr. Otto, a rich old man who was killed in his mansion." )
print("Your task is to gather evidence, question the suspects and catch the killer!")
print("Let's begin the investigation! \n")
print("")

print("\nWhat would you like to do?")

def options_menu (): 
    
    print("1. Investigate the crime scene. ")
    print("2. Question a suspect. ")
    print("3. Use the Notebook. ")
    print("4. Make an accusation! ")
    print("5. Quit the investigation. ")

    user_choice = input("Enter your selection: ")
    return user_choice 

choice=""

while choice != "5": 
    choice = options_menu()

    if choice == "1": 
        evidence()

    elif choice == "2":
        suspects ()
        
    elif choice == "3": 
        pass

    elif choice == "4": 
        pass
    
    elif choice =="5": 
        print("You quit the investigation. ")

    else: 
        print("Please enter a number shown above. ")


file_name = "notebook.csv"

if (not os.path.isfile (file_name)):
    print("Creating the notebook...")
    notebook_file = open(file_name, "w")
    notebook_file.close()


print("Thank you for playing 'A study in Red'! ")
print("===============================================================================================================================================================")

