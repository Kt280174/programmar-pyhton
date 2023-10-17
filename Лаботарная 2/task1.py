money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
money_capital += salary
while money_capital >= spend:
    count += 1
    money_capital -= spend
    spend *= (1 + increase)
    money_capital += salary


print("Количество месяцев, которое можно протянуть без долгов:", count)
