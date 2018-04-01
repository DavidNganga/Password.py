#!/usr/bin/env python3.6
from contact import UserData

def create_contact(name,password):
    '''
    Function to create a new contact
    '''
    new_contact = UserData(name,password)
    return new_contact

def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()

def find_contact(name):
    '''
    Function that finds a contact by name and returns the contact
    '''
    return UserData.find_by_name(name)

def check_existing_contacts(name):
    '''
    Function that check if a contact exists with that name and return a Boolean
    '''
    return UserData.contact_exist(name)   

def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return UserData.display_contacts()  


       
def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

                    short_code = input().lower()

                    if short_code == 'cc':
                            print("New Contact")
                            print("-"*10)

                            print ("name ....")
                            name = input()

                            print ("password")
                            password = input()


                            save_contacts(create_contact(name,password)) # create and save new contact.
                            print ('\n')
                            print(f"New Contact {name} {password} created")
                            print ('\n')

                    elif short_code == 'dc':

                            if display_contacts():
                                    print("Here is a list of all your contacts")
                                    print('\n')

                                    for contact in display_contacts():
                                            print(f"{contact.name} {contact.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any contacts saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the name you want to search for")

                            search_name = input()
                            if check_existing_contacts(search_name):
                                    search_contact = find_contact(search_name)
                                    print(f"{search_contact.name} {search_contact.password}")
                                    print('-' * 20)

                            else:
                                    print("That contact does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':

    main()                            