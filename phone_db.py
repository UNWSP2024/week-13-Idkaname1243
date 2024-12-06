import sqlite3


def create_database():
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()
def add_entry(name, phone_number):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO Entries (name, phone_number)
    VALUES (?, ?)
    ''', (name, phone_number))
    conn.commit()
    conn.close()
def lookup_entry(name):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT phone_number FROM Entries WHERE name = ?
    ''', (name,))
    result = cursor.fetchone()
    if result:
        print(f"Phone number for {name}: {result[0]}")
    else:
        print(f"No entry found for {name}.")
    conn.close()
def update_entry(name, new_phone_number):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE Entries SET phone_number = ? WHERE name = ?
    ''', (new_phone_number, name))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Updated phone number for {name}.")
    else:
        print(f"No entry found for {name}.")
    conn.close()
def delete_entry(name):
    conn = sqlite3.connect('phonebook.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM Entries WHERE name = ?
    ''', (name,))
    conn.commit()
    if cursor.rowcount > 0:
        print(f"Deleted entry for {name}.")
    else:
        print(f"No entry found for {name}.")
    conn.close()
def menu():
    create_database()
    while True:
        print("\nPhonebook Menu:")
        print("1. Add entry")
        print("2. Lookup entry")
        print("3. Update entry")
        print("4. Delete entry")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            add_entry(name, phone_number)
            print(f"Added {name} with phone number {phone_number}.")
        elif choice == '2':
            name = input("Enter name to lookup: ")
            lookup_entry(name)
        elif choice == '3':
            name = input("Enter name to update: ")
            new_phone_number = input("Enter new phone number: ")
            update_entry(name, new_phone_number)
        elif choice == '4':
            name = input("Enter name to delete: ")
            delete_entry(name)
        elif choice == '5':
            print("Exiting phonebook.")
            break
        else:
            print("Invalid choice, please try again.")
if __name__ == '__main__':
    menu()
