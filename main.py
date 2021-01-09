import sqlite3

def add(name,money):
    c.execute(f"""INSERT INTO persons 
                  VALUES ('{name}','{money}')
            """)

def update_money(name,updatedMoney):
    c.execute(f"""UPDATE persons 
                  SET money = {updatedMoney} 
                  WHERE firstname='{name}'
            """)

def lookup(name):
    c.execute(f"""SELECT money 
                  FROM persons 
                  WHERE firstname='{name}'
            """)
    print(f"{name} has {c.fetchone()[0]} dollars")

def lookupall():
    c.execute(f"""SELECT * 
                  FROM persons
            """)
    print(c.fetchall())

def remove(name):
    c.execute(f"""DELETE from persons 
                  WHERE firstname='{name}'
            """)

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
    user = input("What would you like to do: \n\t add an entry (add) \
                \n\t update money (update) \
                \n\t lookup how much money a specific user has (lookup) \
                \n\t lookup everyone (lookupall) \
                \n\t remove an entry (remove) \
                \n\t Press anything else to exit \
                \n What would you like to do:  ")
    print("\n")
    user = user.lower()
    if user == "add":
        name = input("What is the name of the user? ")
        dollars = input(f"How much money does {name} have? ")
        add(name,dollars)
    elif user == "update":
        name = input("Whose money amount would you like to change: ?")
        dollars = input(f"How much money does {name} have? ")
        update_money(name,dollars)
    elif user == "remove":
        name = input("What is the name of the user that you want to remove? ")
        remove(name)
    elif user == "lookup":
        name = input("What is the name of the user that you want to lookup? ")
        lookup(name)
    elif user == "lookupall":
        lookupall()
    else:
        break
    conn.commit()


conn.commit()
conn.close()