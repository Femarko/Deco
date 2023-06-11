import os
import datetime

current_dir = os.getcwd()
target_dir = 'Deco'
target_path = os.path.join(current_dir, target_dir)

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            result_str = str(result) + '\n' + '\n'
            call_time = str(datetime.datetime.now()) + '\n'
            func_name = str(old_function) + '\n'
            func_args = str([args, kwargs]) + '\n'
            file_name = 'main.log'
            path_to_the_file = os.path.dirname(path)
            full_path = os.path.join(path_to_the_file, file_name)
            with open(full_path, 'a', encoding='utf-8') as log_file:
                log_file.write(call_time)
                log_file.write(func_name)
                log_file.write(func_args)
                log_file.write(result_str)
        return new_function
    return __logger

class Cook_book:
    def __init__(self, sourse):
        self.sourse = sourse

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