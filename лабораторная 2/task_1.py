import math
salary = 5000
spend = 6000
months = 10
increase = 0.03
money_capital = 0
for i in range(10):
    money_capital += ((spend * (1 + increase)**i) - salary)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", math.ceil(money_capital))