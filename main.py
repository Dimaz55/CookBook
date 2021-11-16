from pprint import pprint


def my_pprint(book):
    for key in book:
        print(key + ':')
        for entry in book[key]:
            print(entry)
        print()
    return None


def get_shop_list_by_dishes(book, dishes, person_count):
    """Принимает на вход список блюд из cook_book и количество персон для
    кого мы будем готовить. На выходе мы должны получить словарь с названием
    ингредиентов и его количества для блюда"""
    shop_list = {}
    for key in dishes:
        for dic in book[key]:
            ingredient, qty, unit = dic.values()
            # Если ингр. уже есть в списке - суммируем кол-во
            if ingredient in shop_list:
                qty += qty
            shop_list[ingredient] = {'measure': unit,
                                     'quantity': qty * person_count}
    return shop_list


def parse_cookbook_from_file(file_path):
    cook_book = {}
    with open(file_path, encoding='utf-8') as file:
        for line in file:
            name = line.strip()
            qty = file.readline()
            cook_book[name] = []
            for i in range(int(qty)):
                ingredient, quantity, unit = file.readline().split(' | ')
                cook_book[name].append({
                    'ingredient': ingredient,
                    'quantity': int(quantity),
                    'measure': unit.strip()
                })
            file.readline()
    return cook_book


def main():
    cook_book = parse_cookbook_from_file("recipes.txt")
    my_pprint(cook_book)
    print()
    shop_list = get_shop_list_by_dishes(cook_book, ['Фахитос', 'Омлет'], 2)
    pprint(shop_list)


if __name__ == '__main__':

    main()
