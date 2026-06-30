"""
A sample dictionary of contacts to be used as the baseline for the phonebook system
- contains 10 sample contacts
"""

PHONEBOOK = [
    {"name": "Kemi", "phone_number": "08011223344"},
    {"name": "Yomi", "phone_number": "08022334455"},
    {"name": "Tunde", "phone_number": "08033445566"},
    {"name": "Bola", "phone_number": "08044556677"},
    {"name": "Chike", "phone_number": "08055667788"},
    {"name": "Amara", "phone_number": "08066778899"},
    {"name": "David", "phone_number": "08077889900"},
    {"name": "Grace", "phone_number": "08088990011"},
    {"name": "Femi", "phone_number": "08099001122"},
    {"name": "Ngozi", "phone_number": "08000112233"},
]

# Testing update with ID
phone_dict ={
    1: {"name": "Kemi", "phone_number": "08011223344"}
    }

def update(id, name, phone_number):
    contact = phone_dict.get(id)
    if contact:
        contact["name"] = name
        contact["phone_number"] = phone_number
        print(f"Contact updated, {name}: {phone_number}")
    else:
        print("Contact not found")
if __name__ == "__main__":
    update(1, "kemi Alhaja", "09011223344")
    print(phone_dict)