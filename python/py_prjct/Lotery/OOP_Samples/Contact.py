# -*- coding: iso-8859-1 -*-
__author__ = 'Daniel'

class Contact(object):


    numberOfContacts = 0

    def __init__(self):
        Contact.numberOfContacts += 1

    def get_name(self):
        return self.__name;

    def set_name(self, new_name):
        self.__name = new_name

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_telephone(self):
        return self.__telephone

    def set_telephone(self, new_phone_number):
        self.__telephone = new_phone_number

