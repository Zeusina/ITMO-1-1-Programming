a = 1000
b = a
c = int("1000")

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b) # Прогноз: True(численно равны)
print("a is b:", a is b) # Прогноз: True(один и тот же объект)
print("a == c:", a == c) # Прогноз: True(численно равны)
print("a is c:", a is c) # Прогноз: False(разные объекты)

c = None
print("Проверка с на None:", c is None)