import os

from entry_changer import EntryChanger


def clear():
    """ This function clears the screen for easier reading and use."""
    os.system('cls' if os.name == 'nt' else 'clear')


def welcome():
    """ This funciton welcomes the user to the program. """
    clear()
    menu_selector = input("""
    Welcome to the work log application!

  Here you may add or delete tasks for your work log.
  Enter anything to continue or enter 'q' to quit. """).lower()
    if menu_selector != 'q':
        main()
    else:
        print("\nUntil next time, bon voyage!")


def main():
    """ This is the primary menu for work_log.py and gathers information
    to call on the correct class. The user is also allowed to quit and
    end the script."""

    main_loop = True
    while main_loop:
        # This clears the screen on every new instance of the loop
        clear()
        menu_item = EntryChanger()
        # This is the primary menu prompting the user what they want to do.
        menu_selector = input('                                 Main Menu\n' +
                              '-----------------------------------------' +
                              '---------------------------------------\n'
                              "    Please enter the option you would " +
                              'like to select.\n\n' +
                              '  a) Add an entery to the program.\n' +
                              '  b) Search exsisting entries.\n' +
                              '  c) Show all work log entries.\n' +
                              '  d) Exit the program.  ').lower()
        if menu_selector == 'a)' or menu_selector == 'a' \
                or menu_selector == 'add':
            menu_item.add()
        if menu_selector == 'b)' or menu_selector == 'b' \
                or menu_selector == 'search':
            menu_item.search()
        if menu_selector == 'c' or menu_selector == 'c)' \
                or menu_selector == 'all':
            menu_item.show_all()

        if menu_selector == 'd' or menu_selector == 'd)' \
                or menu_selector == 'q' or menu_selector == 'quit':
            print("\nThank you for using the work log application!")
            main_loop = False


if __name__ == '__main__':
    # This makes sure that the script does not run if imported
    welcome()
