def final_accusation():
    print("====================================================================================================================================================================")
    print("\nYou make an accusation based on the evidence gathered.")

    guilty_suspect = "driver"

    def catch_killer(): 
        user_choice = input("\nWho do you accuse of murder? ")
        return user_choice.lower()

    choice = ""

    while choice != guilty_suspect.lower(): 
        choice = catch_killer().lower()
        if choice == "driver":
            print("Congratulations, you solved the crime!")
            print("\nThank you for playing 'A study in Red'! ")
            print("======================================================================== THE END ============================================================================")
        else: 
            print(f"Sorry, the {choice} is not the killer. Keep investigating!")


