import unittest

from csv_intermediary import CSVIntermediary
from entry_changer import EntryChanger


class CSVIntermediaryTestCase(unittest.TestCase):
    """ Tests the CSVIntermediary class. """

    def test_return_all(self):
        """ Does return_all work? This checks to see if return_all crashes."""
        csv = CSVIntermediary()
        csv.return_all()

    def test_add(self):
        """ Does add work? This checks to see if add crashes.
        This does not test to see if the correct values are added to the
        CSV file. """
        csv = CSVIntermediary()
        # This is to check by user_date
        csv.add(user_date='04/21/1974', title='Testing with the ' +
                'test_add', minutes=8, notes="None to report")

    def test_search_by_date(self):
        """ This checks mostly to see if the searching crashes the program"""
        csv = CSVIntermediary()
        csv.search(user_date='04/21/1974')

    def test_search_by_minutes(self):
        """ This checks mostly to see if the searching crashes the program"""
        csv = CSVIntermediary()
        csv.search(minutes=15)

    def test_search_by_key_phrase(self):
        """ This checks mostly to see if the searching crashes the program"""
        csv = CSVIntermediary()
        csv.search(key_phrase='Mayflower')

    def test_search_by_regex(self):
        """ This checks mostly to see if the searching crashes the program"""
        csv = CSVIntermediary()
        csv.search(regex='\d')


class EntryChangerTest(unittest.TestCase):
    """ Tests the EntryChanger class. """

    def test_show(self):
        """ This checks to see if the show menu is operating as intended.
        This is commented out unless actively testing. """
        show_test = EntryChanger()
        show_items = [{'notes': 'This day in history a space ship may ' +
                      'have launched.',
                       'date': '01/04/1995', 'minutes': '10',
                       'title': 'Space Launch'},
                      {'notes': 'Some salt was undoubtedly mined this day.',
                       'date': '01/04/1995',
                       'minutes': '49', 'title': 'Salt mines'}]
        show_test.found_results = show_items
        show_test.show()


unittest.main()
