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

        self.assertEqual(self.new_cred.social_media,"twitter")
        self.assertEqual(self.new_cred.password,"kenobi")

    def test_save_cred(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_cred.save_contact() # saving the new contact
        self.assertEqual(len(CredData.cred_list),1)
    


if __name__ == '__main__':
    unittest.main()        