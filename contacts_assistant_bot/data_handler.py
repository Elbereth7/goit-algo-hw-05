from file_handler import write_to_file
from functools import wraps

# Decorator to add a logic for Exceptions which can appear in data handling functions
def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try: 
            return func(*args, **kwargs)
        except ValueError:
            return "Please provide a name and phone to be added / updated."
        except IndexError:
            return "Please provide a name to be checked in a phone book."
        except KeyError:
            return f"Contact {args[0]} does not exist"
    return inner


def add_contact_validation(name, phone):
    while True:
        user_input = input('Enter yes/no: ').strip().lower()
        if user_input == 'yes':
            return name, phone
        elif user_input == 'no':
            new_name = input(f'Please enter a new name for the contact with a phone number {phone}: ').replace(' ', '_')
            return new_name, phone
        else:
            print("Invalid answer.")

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        print(f'Contact {name} already exists with a phone number {contacts[name]}. Should I rewrite it?')
        name, phone = add_contact_validation(name, phone)           
    contacts[name] = phone
    write_to_file(contacts)
    return "Contact added."

def change_contact_validation(name, phone, contacts):
    while True:
        user_input = input('Enter yes/no: ').strip().lower()
        if user_input == 'yes':
            contacts[name] = phone
            write_to_file(contacts)
            return "Contact added."
        elif user_input == 'no':
            return "Contact skipped."
        else:
            print("Invalid answer.")

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        print(f'Contact {name} does not exist in a phone book. Should I add it?')
        return change_contact_validation(name, phone, contacts)
    else:
        contacts[name] = phone
        write_to_file(contacts)
        return "Contact updated."    

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

@input_error 
def show_all(contacts):
    if not contacts:
        yield "Contact list is empty"
    for name in contacts:
        yield f'Contact name: {name}, phone number: {contacts[name]}'
