
money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
count = 0

while money_capital + salary >= spend:
    money_capital -= (spend - salary)
    spend *= (1 + increase)
    count += 1

print("Количество месяцев, которые можно протянуть без долгов:", count)
