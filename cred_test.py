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
        self.new_cred.save_cred() # saving the new cred
        self.assertEqual(len(CredData.cred_list),1)
    
    def test_display_all_cred(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(CredData.display_cred(),CredData.cred_list) 

        

if __name__ == '__main__':
    unittest.main()        