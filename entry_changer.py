import datetime
import os

from csv_intermediary import CSVIntermediary


class EntryChanger():
    """ This class handles the menu and logic work for work_log.py.
    The user imput is sent into the CSVIntermediary class to be
    processed into the CSV file. """

    def clear(self):
        """ This clears the screen for easier viewing. """
        os.system('cls' if os.name == 'nt' else 'clear')

    def add(self):
        """ This gathers information from the user and sends it to
        CSVIntermediary() to be stored into the csv file."""
        valid_variable = True
        continue_add = True
        # Collects the date
        while True:
            self.clear()
            if valid_variable is False:
                print("    That is not a valid date." +
                      "  Please enter a valid one.\n")
            user_date = input("    Please enter the date in " +
                              "  MM/DD/YYYY format.\n" +
                              "  Enter 'q' to 'quit'.  ")
            try:
                datetime.datetime.strptime(user_date, '%m/%d/%Y')
            except ValueError:
                if user_date == 'q' or user_date == 'quit':
                    continue_add = False
                    break
                else:
                    valid_variable = False
                    continue
            else:
                break

        # continue_add breaks out of the loop if the user chose to quit.
        if continue_add:
            # Collects the event title
            title = input("\n  Please enter a title for the work log.  ")

            # Collects the minutes spent on tasks
            valid_variable = True
            while True:
                if valid_variable is False:
                    self.clear()
                    print("  That is not a valid number for minutes.\n" +
                          "  Please enter a number like '15'.")
                try:
                    minutes = int(input("\n  Please enter the minutes spent " +
                                        "on the task.  "))
                except ValueError:
                    valid_variable = False
                else:
                    break

            # Gathers the information associated with the tasks
            notes = input("\n  Enter any notes you want about the task.\n" +
                          "  This section is optional.  ")
            # This sends all of the information to CSVIntermediary for
            # further processing
            csv = CSVIntermediary()
            csv.add(user_date, title, minutes, notes)

    def search(self):
        # Shows the user a menu of items to choice from.
        continue_loop = True
        while continue_loop:
            self.clear()
            menu_options = ['a', 'a)', 'b', 'b)', 'c', 'c)', 'd',
                            'd)', 'q', 'quit']
            menu_selector = input("    Enter how you would like to search " +
                                  "the work log database.\n" +
                                  '  a) Search by date.\n' +
                                  '  b) Search by time spent\n' +
                                  '  c) Search by an exact search\n' +
                                  '  d) Search by a python ' +
                                  'regular expression\n' +
                                  "    Enter 'q' to quit  "
                                  ).lower()
            if menu_selector in menu_options:
                break

        csv = CSVIntermediary()
        # Finds by date
        if menu_selector == 'a' or menu_selector == 'a)':
            valid_variable = True
            while True:
                self.clear()
                if valid_variable is False:
                    print('  That is not a valid date. Please enter a' +
                          'valid one.\n')
                user_date = input('  Please enter the date in ' +
                                  'MM/DD/YYYY format.  ')
                try:
                    datetime.datetime.strptime(user_date, '%m/%d/%Y')
                except ValueError:
                    valid_variable = False
                    continue
                else:
                    break
            self.found_results = csv.search(user_date=user_date)

        # Find by time spent
        if menu_selector == 'b' or menu_selector == 'b)':
            valid_variable = True
            self.clear()
            while True:
                if valid_variable is False:
                    self.clear()
                    print("  That is not a valid number for minutes.\n" +
                          "  Please enter a number like '15'.\n")
                try:
                    minutes = int(input("  Please enter the minutes " +
                                        "spent on the task.  "))
                except ValueError:
                    valid_variable = False
                else:
                    break
            self.found_results = csv.search(minutes=minutes)

        # Find by an exact search
        if menu_selector == 'c' or menu_selector == 'c)':
            self.clear()
            key_phrase = input("  Enter the 'exact' phrase you want to " +
                               'search for.\n' +
                               '  This searches titles and notes.')
            self.found_results = csv.search(key_phrase=key_phrase)

        # Find by a regular expression pattern.
        if menu_selector == 'd' or menu_selector == 'd':
            regex = input('Enter the python regular expression ' +
                          'string you want to search with.')
            self.found_results = csv.search(regex=regex)

        # This goes to the show method to show the user there results.
        self.show()

    def edit(self):
        pass

    def show(self):
        """ Using the information in self.found_results this shows the
        user the results of a previous search. It also allows the user
        to to continue searching, edit, delete, or exit out of the
        show menu."""
        found_results = self.found_results
        length = len(found_results)

        # This gathers all the information from a ceratain work log in
        # found results and gathers the information to show to the
        # user in an organized fashion.
        index_counter = 0
        while True:
            print(found_results[index_counter])
            menu_selector = input("Which way to you want to go?  ").lower()
            if menu_selector == 'r' or menu_selector == 'd':
                index_counter += 1
            elif menu_selector == 'l' or menu_selector == 'a':
                index_counter -= 1
