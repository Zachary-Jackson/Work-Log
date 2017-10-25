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
        csv.add()


unittest.main()
