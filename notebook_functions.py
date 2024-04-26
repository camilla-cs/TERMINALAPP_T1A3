import csv


def add_note (file_name):
    print("Add note: ")
    with open(file_name,"a") as n: 
        writer = csv.writer(n)
        writer.writerow ()

def remove_note (file_name): 
    print("Remove note: ")


