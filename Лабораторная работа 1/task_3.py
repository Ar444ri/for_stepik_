list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
list_number = len(list_players)
people_in_team = int(list_number/2)
firs_team = list_players[0 : people_in_team]
second_team =list_players[people_in_team:]

print(firs_team)
print(second_team)