
def suspects (): 
    print ("\n You start interviewing the suspects: ")
    print("1. Wife")
    print("2. Son")
    print("3. Chef")
    print("4. Driver")
    print("5. Cleaning lady")
    print("6. Quit the game")
    user_choice = (input("Who would you like to interview? "))
    return user_choice

choice =""
    
while choice != "6": 
    
    if choice =="1":
        pass

    elif choice =="2":
        evaluation()
    
    elif choice == "3": 
        evaluation ()

    elif choice == "4": 
        evaluation()
    
    elif choice == "5":
        evaluation()
    
    else:
        print("You quit the game.")




class suspect : 
    def __init__(self,name, alibi, motive):
            self.name= name
            self.alibi = alibi 
            self.motive = motive

    def evaluation (self):
            print(f"You are questioning the {self.name}, making time to ask them about the relationship with the victim and what were they doing when the murder happened...")
            print(f"\nThe suspect's alibi is: {self.alibi}")
            print(f"After talking with the suspect you arrive at the conclusion that their possible motive could be: {self.motive}")

suspect1 = suspect ("wife","Pilates lessons","Caught the husband cheating")
suspect1.evaluation()

suspect2 = suspect ("son","Out drinking with friends","Inheritance")
suspect2.evaluation()

suspect3 = suspect ("chef","cooking in the kitchen","dispute over salary")
suspect3.evaluation()

suspect4 = suspect ("driver", "was waiting outside in the car","quick to anger")
suspect4.evaluation()

suspect5 = suspect ("cleaning lady","was cleaning the patio","unknown")
suspect5.evaluation ()







   

