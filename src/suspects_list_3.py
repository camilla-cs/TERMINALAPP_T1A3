from colored import Fore, Back, Style

def suspects (): 
    print(f"{Fore.red}===================================================================================================================================================================={Style.reset}")
    print ("\nYou start interviewing the suspects: ")
    print("1. Wife")
    print("2. Son")
    print("3. Chef")
    print("4. Driver")
    print("5. Cleaning lady")
    print("6. Go back to the main menu. ")
    user_choice = input("Who would you like to interview? ")
    return user_choice
    


def motives (): 
    choice = ""
    while choice != "6":
        choice = suspects ()

        if choice == "1": 
            print("\nYou are questioning the Wife, making time to ask them about the relationship with the victim and what they were doing when the murder happened...")
            print("The suspect's alibi is: Pilates lesson. ")
            print("After talking with the suspect you arrive at the conclusion that their possible motive could be: Caught the husband cheating")

        elif choice =="2": 
            print("\nYou are questioning the Son, making time to ask them about the relationship with the victim and what they were doing when the murder happened...")
            print("The suspect's alibi is: Out drinking with friends. ")
            print("After talking with the suspect you arrive at the conclusion that their possible motive could be: Inheritance")
        
        elif choice =="3" : 
            print("\nYou are questioning the Chef, making time to ask them about the relationship with the victim and what they were doing when the murder happened...")
            print("The suspect's alibi is: Making dinner in the kitchen. ")
            print("After talking with the suspect you arrive at the conclusion that their possible motive could be: Dispute over salary")

        elif choice =="4": 
            print("\nYou are questioning the Driver, making time to ask them about the relationship with the victim and what they were doing when the murder happened...")
            print("The suspect's alibi is: Smoking outside. ")
            print("After talking with the suspect you arrive at the conclusion that their possible motive could be: Quick to anger. ")

        elif choice == "5": 
            print("\nYou are questioning the Cleaning lady, making time to ask them about the relationship with the victim and what they were doing when the murder happened...")
            print("The suspect's alibi is: Cleaning the patio. ")
            print("After talking with the suspect you arrive at the conclusion that their possible motive could be: Unknown. ")
        
        elif choice == "6":
            print("")

        else: 
            "Please, put a number from above. "
