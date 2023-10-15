numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
None_index = numbers.index(None)
Numbers_Without_Null = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
Numbers_Without_Null.pop(None_index)
numbers[None_index] = sum(Numbers_Without_Null) / len(numbers)
# TODO заменить значение пропущенного элемента средним арифметическим
print("Измененный список:",numbers)
