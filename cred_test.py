import unittest
from cred import CredData


class TestCredData(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = CredData("twitter","kenobi") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.social_media,"twitter")
        self.assertEqual(self.new_contact.password,"kenobi")


if __name__ == '__main__':
    unittest.main()        