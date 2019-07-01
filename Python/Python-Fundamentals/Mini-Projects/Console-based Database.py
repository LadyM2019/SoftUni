# A simple implementation of a basic people database
import pickle

"""
Note: Instead of using flying functions, a class 'Database' could be created instead which turns all the
database functions into methods and encapsulates the information.
"""
database = []  # global variable to be used to store the database


class Person:
    def __init__(self, name, phone_number, town):
        self.name = name
        self.phone_number = phone_number
        self.town = town


def pick_option(option):
    # Credits: https://jaxenter.com/implement-switch-case-statement-python-138315.html?
    menu = {
        '1': search_by_name,
        '2': search_by_town,
        '3': search_by_tel_number,
        '4': display_database,
        '5': add_person,
        '6': delete_person,
        '7': update_person_info,
        'M': display_menu
    }
    try:
        func = menu[option]
        func()
    except KeyError:
        print('Invalid command. Please enter a value between 1 and 7.')
    # func = menu.get(option, lambda: 'Invalid command. Please enter a value between 1 and 7.')


def display_menu():
    """This function informs the user about the available operations and forces the user to pick one."""
    print("====================================================================================================")
    print("Press 1 to search people by name.")
    print("Press 2 to search people by town.")
    print("Press 3 to search people by tel.number.")
    print("Press 4 to display all the people in the database.")
    print("Press 5 to add a new person.")
    print("Press 6 to delete a person.")
    print("Press 7 to update person's information.")
    print("Choose your move: ", end='')
    choice = input().upper()
    while choice.upper() not in map(str, [1, 2, 3, 4, 5, 6, 7]):
        print('Invalid command. Please enter a value between 1 and 7.')
        choice = input().upper()
    print("====================================================================================================")
    pick_option(choice)


def search_by_name():
    print('You have chosen to search by name.')
    name = input("Name of the person: ")
    filtered_names_list = list(filter(lambda p: p.name == name, database))
    if filtered_names_list:
        print(f"Number of records found: {len(filtered_names_list)}\n")
        for person in filtered_names_list:
            print(f"Name: {person.name}")
            print(f"Phone number: {person.phone_number}")
            print(f"Town: {person.town}\n")
    else:
        print("No records found for this name.")


def search_by_town():
    pass


def search_by_tel_number():
    pass


def display_database():
    print(f"Number of records in the database: {len(database)}\n")
    for person in database:
        print(f"Name: {person.name}")
        print(f"Phone number: {person.phone_number}")
        print(f"Town: {person.town}\n")


def add_person():
    print('You have chosen to add a new person to the database.')

    name = input("Name of the person: ")

    tel_numbers_list = [p.phone_number for p in database]
    while True:
        try:
            tel_number = int(input("Person's phone number: "))
            # if the number is not unique continue looping, else break the while loop
            if tel_number in tel_numbers_list:
                print("Incorrect phone number. Try again.")
                continue
            break
        except ValueError:
            print("Incorrect phone number. Try again.")

    town = input("Person's town: ")

    new_person = Person(name, tel_number, town)
    database.append(new_person)
    print("Person added successfully.\n\n")


def delete_person():
    pass


def update_person_info():
    pass


def main():
    global database
    try:
        with open('save.pickle', 'rb') as load_file:
            database = pickle.load(load_file)
    except FileNotFoundError:
        pass

    while True:
        print("Press 'M' to see the available operations.")
        choice = input().upper()
        pick_option(choice)
        with open("save.pickle", "wb") as save_file:
            pickle.dump(database, save_file)


if __name__ == '__main__':
    main()
