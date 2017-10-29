import datetime
import os
import time

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
                print("\n    That is not a valid date." +
                      "  Please enter a valid one.\n")
            user_date = input("\n    Please enter the date in " +
                              "  MM/DD/YYYY format.\n" +
                              "  Enter 'q' to return to the main menu.  ")
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
                    print("\n  That is not a valid number for minutes.\n" +
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

    def show_all(self):
        """ This gets all of the work log entries from CSVIntermediary and
        sends it to self.show()."""
        csv = CSVIntermediary()
        self.found_results = csv.return_all()
        self.show()

    def search(self):
        """ This gathers the users input and determins how to process the
        data using CSVIntermediary and sends it to self.show()."""
        # Shows the user a menu of items to choice from.
        continue_loop = True
        while continue_loop:
            self.clear()
            menu_options = ['a', 'a)', 'b', 'b)', 'c', 'c)', 'd',
                            'd)', 'e', 'e)', 'all', 'q', 'quit',
                            'date', 'time',
                            'exact', 'regular', 'regular expression']
            menu_selector = input("\n    Enter how you would like to search " +
                                  "the work log database.\n\n" +
                                  '  a) Search by date.\n' +
                                  '  b) Search by time spent\n' +
                                  '  c) Search by an exact search\n' +
                                  '  d) Search by a python ' +
                                  'regular expression\n' +
                                  '  e) Shows all work logs.\n' +
                                  "    Enter 'q' to return to the main menu.  "
                                  ).lower()
            if menu_selector in menu_options:
                break

        csv = CSVIntermediary()
        # Finds by date
        if menu_selector == 'a' or menu_selector == 'a)' \
           or menu_selector == 'date':
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
        if menu_selector == 'b' or menu_selector == 'b)' \
           or menu_selector == 'time':
            valid_variable = True
            self.clear()
            while True:
                if valid_variable is False:
                    self.clear()
                    print("  That is not a valid number for minutes.\n" +
                          "  Please enter a number like '15'.  \n")
                try:
                    minutes = int(input("  Please enter the minutes " +
                                        "spent on the task.  "))
                except ValueError:
                    valid_variable = False
                else:
                    break
            self.found_results = csv.search(minutes=minutes)

        # Find by an exact search
        if menu_selector == 'c' or menu_selector == 'c)' \
           or menu_selector == 'exact':
            self.clear()
            key_phrase = input("  Enter the 'exact' phrase you want to " +
                               'search for.\n' +
                               '  This searches titles and notes.  ')
            self.found_results = csv.search(key_phrase=key_phrase)

        # Find by a regular expression pattern.
        if menu_selector == 'd' or menu_selector == 'd' \
           or menu_selector == 'regular' \
           or menu_selector == 'regular expression':
            regex = input('\nEnter the python regular expression ' +
                          'string you want to search with.  ')
            self.found_results = csv.search(regex=regex)

        # This returns all work log items and sends them to show.
        if menu_selector == 'e' or menu_selector == 'e)' \
                or menu_selector == 'all':
            self.show_all()

        # This goes to the show method to show the user there results.
        if menu_selector != 'q' and menu_selector != 'quit' \
                and menu_selector != 'e' and menu_selector != 'e)' \
                and menu_selector != 'all':
            self.show()

    def edit(self):
        pass

    def show_template(self, entry_num, max_entries, entry_date,
                      title, minutes, notes, menu_options=None):
        """ This is template that is created for and used in show(). """
        self.clear()
        template = """
      Entry number_{} of {}
  Date: {}
  Title: {}
  Minutes: {}

  Notes: {}
  ----------------------------------------------------------------------------
  """.format(entry_num + 1, max_entries, entry_date, title, minutes, notes)
        print(template)
        print("  Enter 'q' to exit to the main menu\n" +
              "  Enter 'search' to do another search.\n" +
              "  Enter 'd' to delete this work log.")
        if menu_options == 'left':
            print("  You can move left. Enter 'l' or 'left'")
        elif menu_options == 'right':
            print("  You can move right. Enter 'r' or 'right'")
        elif menu_options == 'both':
            print("  You can move left or right.\n" +
                  "  Enter 'r', 'right', 'l', or 'left'")

    def show(self, index_counter=0):
        """ Using the information in self.found_results this shows the
        user the results of a previous search. It also allows the user
        to to continue searching, edit, delete, or exit out of the
        show menu."""
        found_results = self.found_results
        length = len(found_results)
        run_loop = True

        # This is incase the user deletes the only entry in the search
        # results.
        if index_counter == -1:
            if length > 0:
                index_counter = 0
            else:
                run_loop = False

        # This prevents the loop from running if not results are returned.
        elif length == 0:
            run_loop = False
            timer_counter = range(4, 0, -1)
            for second in timer_counter:
                self.clear()
                print("""
    There were no results found for your search.
  Taking you back to the search menu. In {} seconds.""".format(second))
                time.sleep(1)
            run_loop = False
            self.search()

        # This gathers all the information from a ceratain work log in
        # found results and gathers the information to show to the
        # user in an organized fashion.
        while run_loop:

            entry_date = found_results[index_counter]['date']
            title = found_results[index_counter]['title']
            minutes = found_results[index_counter]['minutes']
            notes = found_results[index_counter]['notes']

            # This creates the menu_options variable for the show_template
            # left means the user can move left.
            # Right, both and none mean the same as there name.
            menu_options = None
            if index_counter == 0:
                if index_counter < length - 1:
                    menu_options = 'right'
            if index_counter == length - 1:
                if index_counter != 0:
                    menu_options = 'left'
            if index_counter > 0 and index_counter < length - 1:
                menu_options = 'both'

            self.show_template(index_counter, length, entry_date, title,
                               minutes, notes, menu_options)
            menu_selector = input("  ").lower()

            # This controls if the user can actually go left and right.
            # If not, then the user is told and can choice what to do next.
            if menu_selector == 'r' or menu_selector == 'right':
                if index_counter >= length - 1:
                    timer_counter = range(3, 0, -1)
                    for seconds in timer_counter:
                        self.clear()
                        print("\n    You can not go right.\n" +
                              "  Returning to your search in {} seconds."
                              .format(seconds))
                        time.sleep(1)
                else:
                    index_counter += 1
            elif menu_selector == 'l' or menu_selector == 'left':
                if index_counter <= 0:
                    timer_counter = range(3, 0, -1)
                    for seconds in timer_counter:
                        self.clear()
                        print("\n    You can not go left.\n" +
                              "  Returning to your search in {} seconds."
                              .format(seconds))
                        time.sleep(1)
                else:
                    index_counter -= 1
            elif menu_selector == 'q' or menu_selector == 'quit':
                break
            elif menu_selector == 's' or menu_selector == 'search':
                run_loop = False
                self.search()
            elif menu_selector == 'e' or menu_selector == 'edit':
                pass
                # add later..

            elif menu_selector == 'd' or menu_selector == 'delete':
                delete = input('\n  Are you sure you want to delete this ' +
                               "entry? N/y'").lower()
                if delete == 'y':
                    csv = CSVIntermediary()
                    csv.delete(entry_date, title, minutes, notes)
                    del self.found_results[index_counter]
                    index_counter -= 1
                    self.show(index_counter=index_counter)
                    break
