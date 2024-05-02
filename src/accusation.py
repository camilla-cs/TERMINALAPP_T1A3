from colored import Fore, Back, Style

def final_accusation():
    print(f"{Fore.red}===================================================================================================================================================================={Style.reset}")
    print("\nYou make an accusation based on the evidence gathered.")

    guilty_suspect = "driver"

    def catch_killer(): 
        user_choice = input("\nWho do you accuse of murder? Write the name of the suspect: ")
        return user_choice

    choice = ""

    while choice != guilty_suspect.lower(): 
        choice = catch_killer().lower()
        if choice == "driver":
            print("Congratulations, you solved the crime!")
            print("\nThank you for playing 'A study in Red'! ")
            print(f"{Fore.red}===================================================================================================================================================={Style.reset}")
            print("Would you like to play again?")
        else: 
            print(f"Sorry, the {choice} is not the killer. Keep investigating!")

