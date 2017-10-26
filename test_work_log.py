import unittest

from csv_intermediary import CSVIntermediary


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
        test = csv.add(user_date='04/21/1974', title='Testing with the ' +
                       'test_add', minutes=8, notes="None to report")
        #  add later self.assertEqual(test, )

    def test_search_by_date(self):
        """ This checks to see if test_add put in the correct values,
        and to see if the test_add method's work log file can be found."""
        csv = CSVIntermediary()
        csv.search(user_date='04/21/1974')


unittest.main()
