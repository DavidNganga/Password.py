import pyperclip

class UserData:
    contact_list = []
    def __init__(self,name,password):
        self.name = name
        self.password = password
        
        '''

        __init__ method that helps us define properties for our objects.

         Args:
            name: New contacname.
            last_name : New contact last name.
            number: New contact phone number.
            email : New contact email address.
        '''
    
    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        UserData.contact_list.append(self) 
    @classmethod

    def find_by_name(cls,name):
        '''
        Method that takes in a name and returns a contact that matches that name.

        Args:
            name: name to search for
        Returns :
            Contact of person that matches the number.
        '''

        for contact in cls.contact_list:
            if contact.name == name:
                return contact    

    @classmethod
    def contact_exist(cls,name):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            name: Name to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.name == name:
                    return True

        return False 
    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list 
    
 