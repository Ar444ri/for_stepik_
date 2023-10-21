money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
money_capital = money_capital+salary-spend  # в первый месяц
count = 0  # устанавливаем счетчик
while money_capital >= 0:
    spend *= (1 + increase)
    money_capital += salary - spend
    count += 1

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", count)
