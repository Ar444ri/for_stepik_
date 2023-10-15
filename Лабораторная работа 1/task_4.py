users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
attendance = {"Общее количество": 0,
              "Уникальные посещения": 0}
attendance["Общее количество"] = len(users)
attendance["Уникальные посещения"] = len(set(users))
print(attendance)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
