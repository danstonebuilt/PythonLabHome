# -*- coding: iso-8859-1 -*-
__author__ = 'Daniel'

def bubble_sort(numbers):


    for x in range(0, len(numbers) - 1):
        for y in range(x+1, len(numbers)):
            if numbers[x] > numbers[y]:
                aux = numbers[x]
                numbers[x] = numbers[y]
                numbers[y] = aux
    return numbers

def quick_sort(numbers, esquerda,  direita):


    i = esquerda
    j = direita
    x = numbers[(esquerda + direita) / 2]

    while i <= j :

        while numbers[i] < x and i < direita:
            i += 1

        while numbers[j] > x and j > esquerda:
            j -= 1

        if i <= j:
            y = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = y
            i += 1
            j -= 1

    if j > esquerda:
        quick_sort(numbers, esquerda, j)

    if i < direita:
        quick_sort(numbers,  i, direita)

    return numbers


