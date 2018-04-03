class CredData:

    cred_list = []
    def __init__(self,social_media,password):
        self.social_media = social_media
        
        self.password = password
        
        '''

        __init__ method that helps us define properties for our objects.

         Args:
            social_media: New contactsocial_media.
            password : New contact password.
          
        '''
    def save_cred(self):

        '''
        save_contact method saves contact objects into contact_list
        '''
        print("cred run")
        CredData.cred_list.append(self)    

    classmethod
    def display_cred(cls):
        '''
        method that returns the contact list
        '''
        return cls.cred_list      
  