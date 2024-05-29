class PersonalAssistant:

  def __init__(self, todos, birthdays, contacts):
    self.todos = todos
    self.birthdays = birthdays
    self.contacts = contacts

#To-do methods
  def add_todo(self, new_item):
    self.todos.append(new_item)

  def remove_todo(self, todo_item):
    if todo_item in self.todos:
        # Get the todo_item index in list
        index = self.todos.index(todo_item)
        # pop the index for todo_item in todos list
        self.todos.pop(index)
        print(f"{todo_item} was removed")
    else:
        print("Todo is not in list!")

  def get_todos(self):
      return self.todos

#Birthday methods
  def get_birthdays(self):
      return self.birthdays

  def get_birthday(self, name):
    if name in self.birthdays:
      print(f"{name}'s birthday is on {self.birthdays[name]}.")
    else:
      print("Can't find a birthday for this person!")

  def add_birthday(self, name, date):
      if name in self.birthdays:
        print(f"{name} already has a birthday!")
      else:
        self.birthdays[name] = date
        print(f"Successfully added new birthday for {name}!")

  def remove_birthday(self, name):
      if name in self.birthdays:
        self.birthdays.pop(name)
        print(f"{name}'s birthday removed!")
      else:
        print("Birthday not found!")

#Contact methods
  def get_contacts(self):
    return self.contacts
  
  def get_contact(self, name):
    if name in self.contacts:
      return self.contacts[name]
    else:
      return "No contact with that name!"

  def add_contact(self, name, job):
    if name in self.contacts:
      print(f"{name} already in your contacts!")
    else:
      self.contacts[name] = job
      print(f"Successfully added new contact for {name}!")

  def remove_contact(self, name):
    if name in self.contacts:
      self.contacts.pop(name)
      print(f"{name} removed from contacts!")
    else:
      print("Contact not found!")