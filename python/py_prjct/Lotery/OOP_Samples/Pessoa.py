# -*- coding: iso-8859-1 -*-
__author__ = 'Daniel'


class Pessoa(object):


    perCount = 0

    def __init__(self):
        Pessoa.perCount += 1

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name







