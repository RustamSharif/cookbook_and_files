def load_cookbook(file_path):
    cook_book = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:
                break
            ingredients_count = int(file.readline().strip())
            ingredients_list = []
            for _ in range(ingredients_count):
                ingredient_line = file.readline().strip()
                if ingredient_line:
                    ingredient = ingredient_line.split(' | ')
                    if len(ingredient) == 3:  # Защита от некорректного количества элементов
                        ingredients_list.append({
                            'ingredient_name': ingredient[0],
                            'quantity': int(ingredient[1]),
                            'measure': ingredient[2]
                        })
                    else:
                        raise ValueError(f"Некорректный формат ингредиентов: {ingredient_line}")
                else:
                    raise ValueError("Неожиданная пустая строка в списке ингредиентов")
            cook_book[dish_name] = ingredients_list
            file.readline()  # Пропускаем пустую строку
    return cook_book

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[name]['quantity'] += quantity
    return shop_list

cook_book_file_path = r"C:\Users\Abu Aisha\OneDrive\Рабочий стол\Git&GitHub Netology\HW_5\recipes.txt"
try:
    cook_book = load_cookbook(cook_book_file_path)
    shopping_list = get_shop_list_by_dishes(cook_book, ['Запеченный картофель', 'Омлет'], 2)
    print(shopping_list)
except FileNotFoundError:
    print(f"Файл '{cook_book_file_path}' не найден.")
except ValueError as e:
    print(e)
