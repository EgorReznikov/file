cook_book = {}

with open ('file_name.txt', 'rt', encoding='utf8') as file:
    for l in file:
      dish_name = l.strip()
      ingridients = []
      ingridients_count = file.readline()
      for i in range(int(ingridients_count)):
        ing = file.readline()
        ing.split('|')
        ingredient_name, quantity, measure = ing.strip().split('|')
        ingridients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
      blank_line = file.readline()
      cook_book.update({dish_name: ingridients})

print(f'cook_book = {cook_book}\n')


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
      if dish in cook_book.keys():
        for ing in cook_book[dish]:
          sum_1 = int(ing['quantity']) * person_count
          shop_list.update({ing['ingredient_name']: {'measure': ing['measure'], 'quantity': sum_1}})
    return shop_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))



def number_of_lines(*files):
    lines = {}
    for file in files:
        with open(file, 'rt', encoding='utf-8') as f:
            result = f.readlines()
            res = (len(result))
            lines.update({file: res})
    lines_new = {}
    for i in sorted(lines, key=lines.get):
        lines_new[i] = lines[i]
    return lines_new


def writing_file(*files):
    text_dict = {}
    for i in number_of_lines('files/1.txt', 'files/2.txt', 'files/3.txt'):
        with open(i, encoding='utf-8') as file:
            f = file.read()
            text_dict.update({i: f})
    for key, value in text_dict.items():
        with open('files/new.txt', 'a', encoding='utf-8') as file_1:
            file_1.writelines([f"{key}\n{number_of_lines(*files)[key]}\n{value}\n"])

