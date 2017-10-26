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
        # Collects the date
        while True:
            self.clear()
            if valid_variable is False:
                print("That is not a valid date. Please enter a valid one.\n")
            user_date = input("Please enter the date in MM/DD/YYYY format.  ")
            try:
                datetime.datetime.strptime(user_date, '%m/%d/%Y')
            except ValueError:
                valid_variable = False
                continue
            else:
                break
        # Collects the event title
        self.clear()
        title = input("Please enter a title for the work log.  ")
        # Collects the minutes spent on tasks
        valid_variable = True
        while True:
            self.clear()
            if valid_variable is False:
                print("That is not a valid number for minutes.\n" +
                      "Please enter a number like '15'.\n")
            try:
                minutes = int(input("Please enter the minutes spent " +
                                    "on the task.  "))
            except ValueError:
                valid_variable = False
            else:
                break
        # Gathers the information associated with the tasks
        notes = input("Enter any notes you want about the task." +
                      "This section is optional.  ")
        # This sends all of the information to CSVIntermediary for
        # further processing
        csv = CSVIntermediary()
        csv.add(user_date, title, minutes, notes)

    def search(self):
        pass

    def edit(self):
        pass
