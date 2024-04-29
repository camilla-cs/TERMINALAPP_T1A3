from suspects_list_3 import suspects
from colored import Fore, Back , Style

def evidence (): 
    print(f"{Fore.red}===================================================================================================================================================================={Style.reset}")
    print("\nYou enter the crime scene...You notice the victim is on the ground with a stab wound.\n")
    print("There are several items across the floor: ")

    print("+ Bloody knife")
    print("+ Footprints leading from the crime scene to the son's room")
    print("+ Necklace ")
    print("+ Tobacco")
    print("+ Cleaning supplies")
    choice = input ("\n Press enter to go back to the menu. ")
    return choice


