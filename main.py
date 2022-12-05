
def add_ingredient(current_ingredients, ingredient_name, quantity, measure):
    current_ingredients.append({'ingredient_name': ingredient_name,
                                'quantity': int(quantity),
                                'measure': measure})

def get_cook_book(filename: str) -> dict:

    cook_book = {}

    with open(filename, 'r') as file:
        for line in file:
            current_ingredients = []
            current_name = line.strip()
            ingredients_count = int(file.readline().strip())
            for counter in range(ingredients_count):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                add_ingredient(current_ingredients,
                               ingredient_name,
                               quantity,
                               measure)

            cook_book.setdefault(current_name, current_ingredients)
            file.readline()

    return cook_book


def add_portions(shop_list, ingredient, person_count):
    ingredient_name = ingredient['ingredient_name']
    if shop_list.get(ingredient_name) is None:

        new_need_to_buy = {
            'quantity': ingredient['quantity'] * person_count,
            'measure': ingredient['measure']
        }

        shop_list.setdefault(ingredient_name, new_need_to_buy)
    else:
        shop_list[ingredient_name]['quantity'] += ingredient['quantity'] * person_count


def get_shop_list_by_dishes(cook_book: dict, dishes: list, person_count: int) -> dict:

    shop_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            add_portions(shop_list, ingredient, person_count)

    return shop_list


cook_book = get_cook_book('recipes.txt')
print(cook_book)

shop_list = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)
print(shop_list)
