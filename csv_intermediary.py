import csv
import os
import re


class CSVIntermediary():
    """ This class is an intermediary that adds, deletes, or changes
    the data from a CSV file that is given to it. This class also outputs
    data from that same CSV file. """

    def __init__(self, file_location='worklog_csv.csv'):
        # This helps to prevent errors based on file locations
        # presuming the file locations have not been messed with.
        file_location = os.path.dirname(os.path.abspath(__file__))
        self.file_location = os.path.join(file_location,
                                          'worklog_csv.csv')
        try:
            with open(self.file_location) as csvfile:
                pass
        except FileNotFoundError:
            with open(self.file_location, 'w') as csvfile:
                fieldnames = ['date', 'title', 'minutes', 'notes']
                logwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                logwriter.writeheader()

    def return_all(self):
        with open(self.file_location) as csvfile:
            csv_contents = []
            reader = csv.DictReader(csvfile)
            for row in reader:
                csv_contents.append(row)
        self.csv_contents = csv_contents
        return self.csv_contents

    def add(self, user_date='12/24/2017', title='Test', minutes=5, notes=None):
        """ This adds the data that is given to it into the CSV file. """
        with open(self.file_location, 'a') as csvfile:
            fieldnames = ['date', 'title', 'minutes', 'notes']
            logwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            logwriter.writerow({
                               'date': '{}'.format(user_date),
                               'title': '{}'.format(title),
                               'minutes': '{}'.format(minutes),
                               'notes': '{}'.format(notes)
                               })

    def search(self, user_date=None, minutes=None, key_phrase=None,
               regex=None, *args, **kwargs):
        """ This takes any of the variables above and searches the CSV
        file using the paramiters given above."""
        self.return_all()
        csv_contents = self.csv_contents
        returned_contents = []
        if user_date:
            for item in csv_contents:
                for value in item.values():
                    if user_date in value:
                        returned_contents.append(item)
                        break
        elif minutes:
            # searching by the minutes section in the dictionary prevents
            # minutes from catching dates.
            for item in csv_contents:
                if str(minutes) == item['minutes']:
                    returned_contents.append(item)

        elif key_phrase:
            for item in csv_contents:
                for value in item.values():
                    if key_phrase in value:
                        returned_contents.append(item)
                        break

        elif regex:
            # This gets the csv file converted into a string.
            with open(self.file_location) as file:
                csv_string = file.read().splitlines()

            # found_results is the index number associated with where a
            # found result is in self.csv_contents
            found_results = []
            line_counter = 0
            # New line characters are counted as a line so the sub_counter
            # reverts line_counter one line every other run
            sub_counter = 0
            for line in csv_string:
                if sub_counter == 2:
                    sub_counter = 0
                    line_counter -= 1
                if re.findall(r'{}'.format(regex), line):
                    found_results.append(line_counter)
                line_counter += 1
                sub_counter += 1

            # This gets the found dictionaries form
            for number in found_results:
                # This is number -1 because the string form of the csv file
                # has the top line of 'date,title,minutes,notes'
                # where as the csv_contents does not.
                returned_contents.append(csv_contents[number-1])

        self.found = returned_contents
        return self.found

    def edit(self, user_date=None, title=None, minutes=None, notes=None):
        """ This edits a particular line in the CSV file. """
        pass
