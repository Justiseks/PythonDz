import dz52module
radius = 4.2
print("Площадь круга с радиусом", radius, ":", dz52module.circarea(radius))

scores = [4, 2, 5, 3, 4]
print("Средний балл:", dz52module.averscore(scores))

money = 8742
stock_price = 42.42
print("Количество ценных бумаг Сбера, которые можно купить за", money, "рублей:", dz52module.sber(money, stock_price))
