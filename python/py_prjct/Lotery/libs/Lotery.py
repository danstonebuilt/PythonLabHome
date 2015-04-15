# -*- coding: iso-8859-1 -*-
__author__ = 'Daniel'

from random import *
from OrdenationDN import *


def get_megasena_numbers():


    numbers = []
    totalMumbers = range(1, 61)

    for it in range(0, 7):
        shuffle(totalMumbers)
        numbers.append(totalMumbers[0])
        totalMumbers.remove(totalMumbers[0])

    numbers.sort()

    return numbers

def get_lotofacil_numbers():


    numbers = []
    totalMumbers = range(1, 26)

    for it in range(0, 15):
        shuffle(totalMumbers)
        numbers.append(totalMumbers[0])
        totalMumbers.remove(totalMumbers[0])

    numbers.sort()

    return numbers

def get_timemania_numbers():

    numbers = []
    totalMumbers = range(1, 81)

    for it in range(0, 10):
        shuffle(totalMumbers)
        numbers.append(totalMumbers[0])
        totalMumbers.remove(totalMumbers[0])

    numbers.sort()

    return numbers
