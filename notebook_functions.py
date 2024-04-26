import csv

def add_note (file_name):
    print("Add note: ")
    with open(file_name,"a") as n: 
        writer = csv.writer(n)
        writer.writerow ()

def remove_note (file_name): 
    print("Remove note: ")



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