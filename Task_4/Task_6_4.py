"""Console assistant bot """


from functions_handler import (
    parse_input,
    hello_handler,
    add_contact,
    change_contact,
    show_contact,
    show_all_contacts,
)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    handlers = {
        "hello": hello_handler,
        "add": add_contact,
        "change": change_contact,
        "phone": show_contact,
        "all": show_all_contacts,
    }

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break

        handler = handlers.get(command)
        print(handler(args, contacts) if handler else "Invalid command.")


if __name__ == "__main__":
    main()