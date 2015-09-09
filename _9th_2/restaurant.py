#!/usr/bin/python

'''simple example for class'''

class Human(object):
    def __init__(self, name):
        self.name = name

    def say(words):
        print words
        return words

class Customer(Human):
    def order(item):
        return item

class Chef(Human):
    menu = ['yu_xiang_qie_zi', 'stir_fried_beef']
    ingredients = {'eggplant': menu[0], 'beef': menu[1]}
    order_list = []
    ingredients_list = []

    def take_order(ordered_item):
        if ordered_item in menu:
            return ordered_item
        else:
            return

    def choose_ingredient(ordered_list):
        if is_instance(ordered_list, list):
            for order in ordered_list:
                ingredients_list = 

    def cook(ingredient):
        return ingredients[ingredient]
