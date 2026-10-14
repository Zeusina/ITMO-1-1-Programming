# Эксперимент А
print("===Эксперимент А===\n")
a = 10
b = a

print("a, b:", a, b)
print("id(a), (b):", id(a), id(b))

a += 1

print("a, b:", a, b)
print("id(a), (b):", id(a), id(b))

# Эксперимент B
print("\n\n===Эксперимент B===\n")
first = [10, 20]
second = first

print("Оба имени указывают на один объект")
print("first, second:", first, second)
print("id(first), id(second):", id(first), id(second))

second.append(30)

print(
    "После изменения объекта через одно имя поменялось и значение получаемое через второе"
)
print("first, second:", first, second)
print("id(first), id(second):", id(first), id(second))

second = [10, 20, 30]
print("После переопределения second")
print("first == second:", first == second)
print("first is second:", first is second)

second.append(40)
print("После модификации second")
print(first, second)
print("first == second:", first == second)
print("first is second:", first is second)


# Практическая задача
print("\n\n===Практическая задача===\n")
import copy

config1 = {
    "name": "Название 1",
    "participants": ["Участник 1", "Участник 2", "Участник 3"],
    "parameters": [["param-1-1", "param-1-2"], ["param-2-1", "param-2-2"]],
}

config2 = config1

print("config1:", config1)
print("config2:", config2)
print("config1 is config2:", config1 is config2)
print("Обе конфигурации одинаковы, так как имена указывают на один объект\n")

config1["parameters"][0] = ["param-3-1", "param-3-2"]

assert config1 is config2
assert config1 == config2
print("config1:", config1)
print("config2:", config2)
print("config1 is config2:", config1 is config2)
print("Обе конфигурации изменились, так как оба имени указывают на один объект\n")

config2 = copy.deepcopy(config1)

config1["parameters"][0].append("param-4-1")

assert "param-4-1" not in config2["parameters"][0]

print("config1:", config1)
print("config2:", config2)
print("config1 is config2:", config1 is config2)
print(
    "Изменилась только конфигурация 1, так как мы скопировали ее через deepcopy и теперь конфигурация 2 независима"
)
