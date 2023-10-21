list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]
count_chet = 0
count_nechet = 0
# TODO завести отдельные счетчики для четных и нечетных чисел
for i, value in enumerate(list_):
    if value % 2 == 0:
        count_chet += 1
    else:
        count_nechet += 1
if count_chet > count_nechet:
    print("Четных чисел больше")
elif count_chet < count_nechet:
    print("Нечетных чисел больше")
else:
    print("Четных и нечетных одинаковое количество")
# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных
