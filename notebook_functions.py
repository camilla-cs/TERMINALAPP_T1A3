import csv
def notebook_menu():
    print("You open the notebook. What would you like to do? ")
    print("1. Add note. ")
    print("2. Remove note. ")
    print("3. Edit note. ")
    print("4. View notes. ")
    print("5. Quit the game. ")
    user_choice = input("\nPlease enter a number from above. ")
    return user_choice

def add_note (file_name):
    note = input ("Enter your note: ")
    with open(file_name,"a", newline="") as n: 
        writer = csv.writer(n)
        writer.writerow ([note])

def remove_note (file_name): 
    pass



def view_notebook (file_name):
    try: 
        with open(file_name, "r") as f: 
            reader = csv.reader (f) 
        for row in reader:
            if (row[1] == "True"): 
                print(f"{row[0]} is complete.")
            else:
                print(f"{row[0]} is not complete.")
    except FileNotFoundError: 
        print("The todo file does not exist. ")