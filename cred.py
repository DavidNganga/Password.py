class CredData:

    contact_list = []
    def __init__(self,social_media,password):
        self.social_media = social_media
        
        self.password = password
        
        '''

        __init__ method that helps us define properties for our objects.

         Args:
            social_media: New contactsocial_media.
            password : New contact password.
          
        '''
    def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        CredData.contact_list.append(self)     
  