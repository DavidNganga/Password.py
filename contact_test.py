import unittest
from contact import UserData


class TestUserData(unittest.TestCase):
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_contact = UserData("ObiWan","kenobi") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_contact.name,"ObiWan")
        self.assertEqual(self.new_contact.password,"kenobi")
    def test_save_contact(self):
        '''
        test_save_contact test case to test if the contact object is saved into
         the contact list
        '''
        self.new_contact.save_contact() # saving the new contact
        self.assertEqual(len(UserData.contact_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            UserData.contact_list = []

    def test_save_multiple_contact(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_contact.save_contact()
            test_contact = UserData("Test","user")# new contact
            test_contact.save_contact()
            self.assertEqual(len(UserData.contact_list),2)
    def test_find_contact_by_name(self):
        '''
        test to check if we can find a contact by  name and display information
        '''

        self.new_contact.save_contact()
        test_contact = UserData("Test","user") # new contact
        test_contact.save_contact()

        found_contact = UserData.find_by_name("Test")

        self.assertEqual(found_contact.password,test_contact.password)        
    def test_contact_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_contact.save_contact()
        test_contact = UserData("Test","user") # new contact
        test_contact.save_contact()

        contact_exists = UserData.contact_exist("Test")

        self.assertTrue(contact_exists) 
    def test_display_all_contacts(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(UserData.display_contacts(),UserData.contact_list) 

        
              

if __name__ == '__main__':
    unittest.main()

