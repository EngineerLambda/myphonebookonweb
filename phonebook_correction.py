from phonebook_list import PHONEBOOK
# CRUD - Create, Read, Update, Delete 

# create a custom print function to format phonebook
def print_phonebook():
    print("=====CONTACTS LIST=====\n")
    for contact in PHONEBOOK:
        print(f"{contact['name']:^10}: {contact['phone_number']:^10}")

# a funtion to create a new entry into the phonebook
def create(name, phone_number):
    new_contact = {"name": name, "phone_number": phone_number}
    PHONEBOOK.append(new_contact)

    print(f"Contact saved, {name}: {phone_number}")

# search for a contact
def search(search_text: str):
    print("=====SEARCH RESULTS=====\n")
    for contact in PHONEBOOK:
        if contact["name"].lower().startswith(search_text.lower()):
            print(f"{contact['name']:^10}: {contact['phone_number']:^10}")
            
# update a contact
def update(name, phone_number, edit_name=False):
    if edit_name:
        for contact in PHONEBOOK:
            if contact["phone_number"] == phone_number:
                contact["name"] = name
                print(f"Contact updated, {name}: {phone_number}")
    else:
        for contact in PHONEBOOK:
            if contact["name"] == name:
                contact["phone_number"] = phone_number
                print(f"Contact updated, {name}: {phone_number}")

# delete a contact 
def delete(name):
    for contact in PHONEBOOK:
        if contact["name"] == name:
            PHONEBOOK.remove(contact)
            print(f"Contact Deleted: {name}: {contact['phone_number']}")

create("Abdulsomad", "08102546098")
search("abdul")
update("Abdulsomad", "123456789")
update("Abdulsomad Ilorin", "123456789", edit_name=True)
delete("Abdulsomad Ilorin")

print_phonebook()