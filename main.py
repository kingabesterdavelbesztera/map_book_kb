from models.data_source import users
from package.crud import read_friends, add_user, search_user, remove_user

if __name__ == "__main__":
    while True:
        print("Welcome to the menu choose an option: ")
        print("1. Read a list of friend")
        print("0. Exit")
        print("2. add new users")
        print("3. Search")
        print("4 remove")
        menu_option = input("Choose an option:")
        if menu_option == "0":
            break
        if menu_option == "1":
            read_friends(users)
        if menu_option == "2":
            add_user(users)
        if menu_option == "3":
            search_user(users)
        if menu_option == "4":
            remove_user(users)