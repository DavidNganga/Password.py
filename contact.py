class UserData:
    contact_list = []
    '''

     __init__ method that helps us define properties for our objects.

        Args:
            name: New contacname.
            last_name : New contact last name.
            number: New contact phone number.
            email : New contact email address.
    '''
        
    def __init__(self,name,password):

        self.name = name
        self.password = password
 