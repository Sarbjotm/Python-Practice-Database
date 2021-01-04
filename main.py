import sqlite3

def add(name,money):
    pass

def update_money(name,updatedAge):
    pass

def remove(name):
    pass

def create():
    pass

create()
print("Welcome to the database simulator")
while(True):
    user = input("What would you like to do: add an entry (add), update money (update) or remove an entry (remove):  ")
    user = user.lower()
    if user == "add":
        name = input("What is the name of the user? ")
        dollars = input(f"How much money does {name} have? ")
        add(user,dollars)
    elif user == "update":
        name = input("Whose money amount would you like to change: ?")
        name = name.lower()
        dollars = input(f"How much money does {name} have? ")
        update_money(name, dollars)
    elif user == "remove":
        name = input("What is the name of the user that you want to remove? ")
        name = name.lower()
        remove(name)

    

