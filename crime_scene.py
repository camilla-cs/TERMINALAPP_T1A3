from suspects_list import suspects

def evidence (): 
    print("\n You enter the crime scene...You notice the victim is on the ground with a stab wound.")
    print("There are several items across the floor: ")

    print("Bloody knife")
    print("Footprints leading from the crime scene to the son's room")
    print("Wife's necklace is found near the body")
    print("Tobacco")
    print("Cleaning supplies")
    evidence_choice = input ("\n Would you like to go back to the menu? Choose between yes or no: ")
    return evidence_choice
