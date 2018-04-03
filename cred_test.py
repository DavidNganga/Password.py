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

    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(CredData.contact_list),1)
    


if __name__ == '__main__':
    unittest.main()        