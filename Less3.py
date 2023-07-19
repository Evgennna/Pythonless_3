# 1. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import choices

count = int(input())
list_nums = choices(range(1, count * 2), k=count)

print(list_nums)

res_list = set()
for i in list_nums:
    if list_nums.count(i) > 1:
        res_list.add(i)

print(res_list)


# 2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

text = "She sells sea shells on the sea shore," \
       " The shells that she sells are sea shells," \
       " I'm sure. So if she, sells sea shells, on the" \
       " sea shore I'm sure, that the shells, are sea shore, shells"

text_list = text.lower().split()

text_dict = {}

for i in text_list:
    cl = i.strip(".,!:;")
    if cl not in text_dict:
        text_dict[cl] = 1
    else:
        text_dict[cl] += 1

print(text_dict)

result = dict(sorted(text_dict.items(), key=lambda x: x[1], reverse=True))
print(result)

# 3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

def find_possible_combinations(items, max_weight):
    combinations = []

    def find_combinations(item_index, current_combination, current_weight):
        #Вариант с точной массой
        if current_weight == max_weight:
            combinations.append(current_combination)
            return

        if current_weight > max_weight or item_index == len(items):
            return

        item, weight = items[item_index]
        if current_weight + weight <= max_weight:
            find_combinations(item_index + 1, current_combination + [item], current_weight + weight)

        find_combinations(item_index + 1, current_combination, current_weight)

    find_combinations(0, [], 0)
    return combinations

backpack_capacity = 8
items = {
    'Топор': 1.5,
    'Пиво': 3,
    'Горелка': 2,
    'Удочка': 2,
    'Фонарик': 0.5,
    'Котелок' : 1,
    'Нож' : 1,
    'Спички' : 0.5

}

items_list = [(item, weight) for item, weight in items.items()]

combinations = find_possible_combinations(items_list, backpack_capacity)
#print(combinations)
if len(combinations):
    for i,combination in enumerate(combinations, start=1):
        print(f'Вариант {i}')
        print(f'Вещи: {", ".join(item for item in combination)}')
        print(f'Общая масса: {sum(items[item] for item in combination)}')
        print('---')
else:
    print(" Отсутствуют подходящие комбинации")