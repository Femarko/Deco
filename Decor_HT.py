import os
import datetime
from logger_param import logger

current_dir = os.getcwd()
file_name = 'callings.log'
target_path = os.path.join(current_dir, file_name)

class Cook_book:
    def __init__(self, sourse):
        self.sourse = sourse

    @logger(target_path)
    def create_dict(self):
        with open(self.sourse, 'rt', encoding='utf-8') as file:
            cook_book_dict = {}

            for line in file:
                dish_name = line.strip()
                ingredients_count = int(file.readline().strip())

                ingredients = []

                for iteration in range(ingredients_count):
                    ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                    ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})

                file.readline()

                cook_book_dict[dish_name] = ingredients

        return cook_book_dict

    @logger(target_path)
    def get_shop_list_by_dishes(self, dishes, person_count):

        shoplist_dict = {}

        for dish in dishes:

            for ingredient in self.create_dict()[dish]:
                shoplist_dict[ingredient['ingredient_name']] = {
                    'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count
                }

        return shoplist_dict


some_cook_book = Cook_book('recipes.txt')
print(some_cook_book.create_dict())
print(some_cook_book.get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))