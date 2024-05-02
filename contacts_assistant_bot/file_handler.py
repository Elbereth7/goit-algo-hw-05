from pathlib import Path
from functools import wraps

file_path = Path('contacts_assistant_bot/contacts.txt')

# Decorator to add a logic for Exceptions which can appear while reading the file (file does not exist)
def file_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try: 
            return func(*args, **kwargs)
        except FileNotFoundError:
            contacts = {}
            return contacts
    return inner

def write_to_file(contacts, file_path=file_path):
    with open(file_path, 'w') as file:
        str_contacts = str(contacts).replace('{', '').replace('}', '')
        str_contacts = str_contacts.replace(', ', ',\n')
        file.write(str_contacts)

@file_error
def create_dict_from_file(file_path=file_path):
    contacts = {}
    with open(file_path, 'r') as file:
        string = file.read()
        if string:
            records_list = string.split(',')
            for record in records_list:
                name, phone = record.split(':')
                name = name.replace("'", "").strip()
                phone = phone.replace("'", "").strip()
                contacts[name] = phone
    return contacts

if __name__ == "__main__":
    print(create_dict_from_file(), type(create_dict_from_file()))