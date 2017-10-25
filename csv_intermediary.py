import csv
import os


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
            CSV_contents = []
            reader = csv.DictReader(csvfile)
            for row in reader:
                CSV_contents.append(row)
        return CSV_contents

    def add(self, date='12/24/2017', title='Test', minutes=5, notes=None):
        """ This adds the data that is given to it into the CSV file. """
        with open(self.file_location, 'a') as csvfile:
            fieldnames = ['date', 'title', 'minutes', 'notes']
            logwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
            logwriter.writerow({
                               'date': '{}'.format(date),
                               'title': '{}'.format(title),
                               'minutes': '{}'.format(minutes),
                               'notes': '{}'.format(notes)
                               })

    def search(self, date=None, title=None, minutes=None, notes=None,
               regex=None, *args, **kwargs):
        """ This takes any of the variables above and searches the CSV
        file using the paramiters given above."""

    def edit(self, date=None, title=None, minutes=None, notes=None):
        """ This edits a particular line in the CSV file. """
        pass
