import sqlite3

def add(name,money):
    c.execute(f"INSERT INTO persons VALUES ('{name}','{money}')")

def update_money(name,updatedAge):
    pass

def lookup(name):
    c.execute(f"SELECT * FROM persons WHERE firstname='{name}'")
    print(c.fetchone())

def remove(name):
    pass

def create():
    c.execute("""
    CREATE TABLE IF NOT EXISTS persons(
        firstname text,
        money real
    ) 
    """)


conn = sqlite3.connect('students.db')
c = conn.cursor()
create()
conn.commit()
print("Welcome to the database simulator")
while(True):
    user = input("What would you like to do: add an entry (add), update money (update), lookup info (lookup) or remove an entry (remove) \n Press anything else to exit:  ")
    user = user.lower()
    if user == "add":
        name = input("What is the name of the user? ")
        dollars = input(f"How much money does {name} have? ")
        add(name,dollars)
    elif user == "update":
        name = input("Whose money amount would you like to change: ?")
        name = name.lower()
        dollars = input(f"How much money does {name} have? ")
        update_money(name, dollars)
    elif user == "remove":
        name = input("What is the name of the user that you want to remove? ")
        name = name.lower()
        remove(name)
    elif user == "lookup":
        name = input("What is the name of the user that you want to lookup? ")
        lookup(name)
    else:
        break

    
conn.commit()
conn.close()