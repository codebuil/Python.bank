import os

def save_to_file(contacts, file_name):
    with open(file_name, 'w') as file:
        for contact in contacts:
            file.write(','.join(contact) + '\n')

def load_from_file(file_name):
    contacts = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                contact = line.strip().split(',')
                contacts.append(contact)
    return contacts

def add_contact(contacts, contact_info):
    contacts.append(contact_info)

def display_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("ID\tName\tAddress\tEmail")
        for contact in contacts:
            print(f"{contact[0]}\t{contact[1]}\t{contact[2]}\t{contact[3]}")

def delete_contact(contacts, contact_id):
    for contact in contacts:
        if contact[0] == contact_id:
            contacts.remove(contact)
            return

def main():
    file_name = "address_book.txt"

    contacts = load_from_file(file_name)

    while True:
        print("ADDRESS BOOK MENU:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            contact_id = input("Enter ID: ")
            name = input("Enter Name: ")
            address = input("Enter Address: ")
            email = input("Enter Email: ")
            new_contact = [contact_id, name, address, email]
            add_contact(contacts, new_contact)
            save_to_file(contacts, file_name)
            print("Contact added.")
        elif choice == '2':
            display_contacts(contacts)
        elif choice == '3':
            contact_id = input("Enter ID of contact to delete: ")
            delete_contact(contacts, contact_id)
            save_to_file(contacts, file_name)
            print("Contact deleted.")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if 0 == 0:
    print("\x1bc\x1b[43;30m")
    main()

