from input_parser import parse_input
from data_handler import add_contact, change_contact, show_phone, show_all
from file_handler import create_dict_from_file

def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, create_dict_from_file()))
        elif command == "change":
            print(change_contact(args, create_dict_from_file()))
        elif command == "phone":
            print(show_phone(args, create_dict_from_file()))
        elif command == "all":
            for output_string in show_all(create_dict_from_file()):
                print(output_string)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()