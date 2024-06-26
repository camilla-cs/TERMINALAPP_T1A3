import csv
from colored import Fore, Back, Style

def notebook (): 
    def notebook_menu():
        print(f"{Fore.red}====================================================================================================================================================={Style.reset}")
        print("You open the notebook. What would you like to do? ")
        print("1. Add note. ")
        print("2. Remove note. ")
        print("3. Edit note. ")
        print("4. View notes. ")
        print("5. Go back to the main menu. ")
        user_choice = input("\nEnter a number:  ")
        return user_choice

    def add_note (file_name):
        note = input ("Enter your note: ")
        with open(file_name,"a", newline="") as n: 
            writer = csv.writer(n)
            writer.writerow ([note])

    def remove_note (file_name): 
        note_to_remove = input ("Enter the note you want to remove: ")
        with open (file_name,"r") as f: 
            reader = csv.reader(f) 
            notes = list(reader)
        good_notes = [note for note in notes if note [0] != note_to_remove]
        with open (file_name, "w", newline="") as f: 
            writer = csv.writer(f)
            writer.writerows(good_notes)
        

    def edit_note (file_name): 
        note_to_edit= input ("Enter the note you want to edit: ")
        new_note = input("Enter the new note: ")

        try: 
            with open (file_name, "r") as f: 
                reader = csv.reader (f)
                notes = list(reader)
            
            note_index = None
            for i, note in enumerate (notes): 
                if note[0] == note_to_edit:
                    note_index = i
                    break
            if note_index is not None: 
                notes [note_index][0] = new_note

                with open (file_name,"w", newline="") as f:
                    writer = csv.writer (f)
                    writer.writerows (notes)
                print ("Note changed successfully.")
            else:
                print ("Note not found. ")
        except FileNotFoundError:
            print("The notebook file does not exist. ")




    def view_notebook (file_name):
        try: 
            with open(file_name, "r") as f: 
                reader = csv.reader (f) 
                for row in reader:
                    print(row[0])
        except FileNotFoundError: 
            print("The notebook file does not exist. ")

    file_name = "notebook.csv"

    choice =""

    while choice != "5": 
        choice = notebook_menu()

        if choice == "1":
            add_note (file_name)
        elif choice == "2": 
            remove_note(file_name)
        elif choice =="3": 
            edit_note(file_name)
        elif choice == "4": 
            view_notebook (file_name) 
        elif choice == "5": 
            print("You quit the investigation.")
        else: 
            print("Please put a number from above. ")
