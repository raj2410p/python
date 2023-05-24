import sqlite3
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create a table if it doesn't exist     
cursor.execute('''CREATE TABLE IF NOT EXISTS userdata
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   first_name TEXT,
                   last_name TEXT,
                   age INTEGER,
                   iq INTEGER)''')

first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
age = int(input("Enter your age: "))
iq = int(input("Enter your iq: "))  
if iq >130:
    print(first_name,last_name,"is genius")
elif iq > 100:
    print(first_name,last_name,"is average")
else:
    print(first_name,last_name,"is dumb")

# Insert user data into the database
cursor.execute("INSERT INTO userdata (first_name,last_name, age, iq) VALUES (?, ?, ?,?)", (first_name,last_name, age, iq))
conn.commit()

# Close the database connection
conn.close()
