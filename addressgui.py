
import tkinter as tk
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

def add_contact():
    contact_id = id_entry.get()
    name = name_entry.get()
    address = address_entry.get()
    email = email_entry.get()

    new_contact = [contact_id, name, address, email]
    contacts.append(new_contact)
    save_to_file(contacts, "address_book.txt")
    status_label.config(text="Contact added.")
    refresh_display()

def display_contacts():
    contact_display.delete(1.0, tk.END)
    if not contacts:
        contact_display.insert(tk.END, "No contacts found.")
    else:
        contact_display.insert(tk.END, "ID\tName\tAddress\tEmail\n")
        for contact in contacts:
            contact_display.insert(tk.END, f"{contact[0]}\t{contact[1]}\t{contact[2]}\t{contact[3]}\n")

def delete_contact():
    contact_id = delete_id_entry.get()
    for contact in contacts:
        if contact[0] == contact_id:
            contacts.remove(contact)
            save_to_file(contacts, "address_book.txt")
            status_label.config(text="Contact deleted.")
            refresh_display()
            return
    status_label.config(text="Contact ID not found.")

def refresh_display():
    display_contacts()

contacts = load_from_file("address_book.txt")

root = tk.Tk()
root.title("Address Book")
root.configure(bg="brown", width=800, height=600)  # Define a cor de 


id_label = tk.Label(root, text="ID:")
id_label.grid(row=0, column=0)
id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1)

name_label = tk.Label(root, text="Name:")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=2, column=0)
address_entry = tk.Entry(root)
address_entry.grid(row=2, column=1)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=3, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, columnspan=2)

display_button = tk.Button(root, text="Display Contacts", command=display_contacts)
display_button.grid(row=5, columnspan=2)

contact_display = tk.Text(root, height=10, width=40)
contact_display.grid(row=6, columnspan=2)

delete_id_label = tk.Label(root, text="Enter ID to delete:")
delete_id_label.grid(row=7, column=0)
delete_id_entry = tk.Entry(root)
delete_id_entry.grid(row=7, column=1)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=8, columnspan=2)

status_label = tk.Label(root, text="")
status_label.grid(row=9, columnspan=2)

root.mainloop()
