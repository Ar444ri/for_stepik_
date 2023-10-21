list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Поменяйте местами значения согласно условию

last_index = len(list_numbers) - list_numbers[::-1].index(max(list_numbers)) - 1
end_numb = list_numbers[19]

list_numbers[19] = list_numbers[last_index]
list_numbers[last_index] = end_numb
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
