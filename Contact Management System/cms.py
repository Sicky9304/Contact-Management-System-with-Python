import json
import os

def add_person():
    name= input("Name: ")
    age= input("Age: ")
    phone= int(input("Phone: "))
    email= input("Email: ")
    
    person= {'name':name, 'age':age, 'phone':phone, 'email':email}
    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i+1,"-",person["name"], "|",person["age"], "|", person["phone"], "|", person["email"])

def delete_people(people):
    display_people(people)
    while True:
        number = int(input("Enter a number to delete: "))
        try:
            if number <= 0 or number > len(people):
                print("Invalid Number! Out of range")
                continue
            else:
                break
        except:
            print("Invalid Input Number!")
    people.pop(number-1)
    print("Person Deleted...")

def search_contact(people):
    search_name = input("Enter name to Search in contact List: ").lower()
    results = []
    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
    if results:
        print("Search Results:")
        display_people(results)
    else:
        print("No contacts found with that name.")


print(".....Welcome to Contact Management System.....")


# Read Contact From .Json File when program start...
try:
    with open("contacts.json", "r") as f:
        people = json.load(f)["contacts"]
except (FileNotFoundError, json.JSONDecodeError):
    # Create empty contacts list if file doesn't exist or is invalid
    people = []
    with open("contacts.json", "w") as f:
        json.dump({"contacts": people}, f)


print("1. Add People")
print("2. Display People")
print("3. Delete People")
print("4. Search Contact")
print("5. Exit")
print()
while True:
    print("Contact List Size: ", len(people))

    try:
        command = int(input("\nEnter the choice: "))
    except ValueError:
        print("Invalid Input! Please enter a number.")
        continue
    
    match (command):
        case (1):
            person = add_person()
            people.append(person)
            print("Person Added Successfully!")
        
        case (2):
            if not people:
                print("Contact List is Empty! Nothing to display.")
                continue
            display_people(people)
        
        case (3):
            if not people:
                print("Contact List is Empty! Nothing to delete.")
                continue
            delete_people(people)
        
        case (4):
            if not people:
                print("Contact List is Empty! Nothing to Search.")
                continue
            search_contact(people)
            
        
        case (5):
            print("Exiting....")
            break
                 
        case (_):
            print("Invalid  Choice!") 

#After all operations, save the updated contacts back to the JSON file

    with open("contacts.json",'w')as f:
        json.dump({"contacts":people},f)
    