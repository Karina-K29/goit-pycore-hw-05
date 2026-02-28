"""Handlers and utilities for the assistant bot"""


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Enter the argument for the command"
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
    return inner


def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.strip().lower(), args


@input_error
def hello_handler(args: list[str], contacts: dict) -> str:
    return "How can I help you?"


@input_error
def add_contact(args: list[str], contacts: dict) -> str:
    name = args[0]                  # IndexError якщо немає імені
    phone = args[1]                 # IndexError якщо немає телефону
    name = name.strip()
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args: list[str], contacts: dict) -> str:
    name = args[0]                  # IndexError якщо немає імені
    phone = args[1]                 # IndexError якщо немає телефону
    name = name.strip()
    contacts[name]                  # KeyError якщо контакту нема
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_contact(args: list[str], contacts: dict) -> str:
    name = args[0].strip()          # IndexError якщо імені нема
    return contacts[name]           # KeyError якщо контакту нема


      
""" Декоратор тут не потрібен технічно бо функція не викликає помилок.
Але в умові завдання написано: кожна функція для обробки команд
має декоратор input_error тому залишила його тут"""
@input_error   
def show_all_contacts(args: list[str], contacts: dict) -> str:
    if not contacts:
        return "Contact book is empty."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())