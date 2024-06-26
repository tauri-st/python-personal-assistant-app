#imports PersonalAssistant.py and JSON files
import json
from PersonalAssistant import PersonalAssistant

#ADD CODE: open JSON file and pass data to PersonalAssistant class
with open("todo.json", "r") as todos, open("birthdays.json", "r") as birthdays, open("contacts.json", "r") as contacts:
    todo_list = json.load(todos)
    birthday_list = json.load(birthdays)
    contact_list = json.load(contacts)
    
    assistant = PersonalAssistant(todo_list, birthday_list, contact_list)

done = False

while not done:
    user_command = input(
        """
How can I help you?

    **** To-dos *****
    1: Add a to-do
    2: Remove a to-do
    3: Get to-do list
    **** Birthdays *****
    4: Get a birthday
    5: Add a birthday
    6: Remove a birthday
    **** Contacts *****
    7: View a contact
    8: Add a contact
    9: Remove a contact

    Select a number or type 'Exit' to quit: 
    
    """
    )
    # Add Todo
    if user_command == "1":
        user_input = input("\nItem to add to to-do list: ")
        assistant.add_todo(user_input)
    # Remove Todo
    elif user_command == "2":
        print(f"Your current todos: {assistant.get_todos()}")
        user_input = input("Item to remove from to-do list: ")
        print(f"\n {assistant.remove_todo(user_input)}")
    # Get Todos
    elif user_command == "3":
        print("\nYour to-do list")
        print(f"\n {assistant.get_todos()}")
    # Get Birthday
    elif user_command == "4":
        print("Your birthday contacts: \n")
        for name in assistant.get_birthdays():
            print(name)
        user_input = input("Whose birthday would you like to look up?")
        print(f"{assistant.get_birthday(user_input)}")
    # Add Birthday
    elif user_command == "5":
        print("Add a birthday: \n")
        name = input("Name of the person: ")
        birthday = input("Their birthday (ex: 08/18/2000): ")
        print(f"\n {assistant.add_birthday(name, birthday)}")
    # Remove Birthday
    elif user_command == "6":
        print("Your birthday contacts: \n")
        for name in assistant.get_birthdays():
            print(name)
        user_input = input("Who's birthday would you like to remove?")
        print(f"\n {assistant.remove_birthday(user_input)}")
    # Get a Single Contact
    elif user_command == "7":
        print("View a Contact: \n")
        print("Your contacts: \n")
        for name in assistant.get_contacts():
            print(name)
        user_input = input("Which contact would you like to pull up?")
        print(f"{assistant.get_contact(user_input)}")
    #Add a Contact
    elif user_command == "8":
        print("Add a contact: \n")
        print("Your contacts: \n")
        for name in assistant.get_contacts():
            print(name)
        name = input("Name of the person: ")
        job = input("Their job position: ")
        print(f"\n {assistant.add_contact(name, job)}")
    #Remove a Contact
    elif user_command == "9":
        print("Remove a contact: \n")
        print("Your contacts: \n")
        for name in assistant.get_contacts():
            print(name)
        user_input = input("Which contact would you like to remove?")
        print(f"\n {assistant.remove_contact(user_input)}")
    
    elif user_command == "exit" or user_command == "Exit" or user_command == "EXIT":
        done = True
        print("\nGoodbye, see you soon!")
    else:
        print("\nNot a valid command.")

# ADD CODE: write data to JSON file
with open("todo.json", "w") as write_todos, open("birthdays.json", "w") as write_birthdays, open("contacts.json", "w") as write_contacts:
    json.dump(assistant.get_todos(), write_todos)
    json.dump(assistant.get_birthdays(), write_birthdays)
    json.dump(assistant.get_contacts(), write_contacts)