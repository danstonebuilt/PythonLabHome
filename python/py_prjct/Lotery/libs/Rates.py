# -*- coding: iso-8859-1 -*-
__author__ = 'Daniel'
import math


def annual_interest(val, rate, months):
    rate = rate / 100
    value = val * pow((1 + rate), months)
    return value