# Эксперимент 1

import gc

first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("GC status", gc.isenabled())
print("Gen threesholds", gc.get_threshold())
print("Gen statistics", gc.get_stats())

id_first = id(first)

id_second = id(second)

print(id_first, id_second)

del first
del second

gc_collect = gc.collect()  # Сохраненное значение 2
print(gc_collect)


# Дополнительный эксперимент

print("\n\n===Дополнительный эксперимент===\n")

gc.disable()

first = []
second = []
third = []

first.append(second)
first.append(third)
second.append(first)
second.append(third)
third.append(first)
third.append(second)

del first
del second
del third

print("Собрано объектов:", gc.collect())

gc.enable()

# Практическая задача
print("\n\n===Практическая задача===\n")

print("Собрано объектов:", gc.collect())

a = {"name": "a", "links": []}
b = {"name": "b", "links": []}
c = {"name": "c", "links": []}
d = {"name": "d", "links": []}

a["links"].append(b)
b["links"].append(c)
c["links"].append(a)

print("Связи")
for i in (a, b, c, d):
    print(f"{i['name']} -> {', '.join([j['name'] for j in i['links']]) or 'нет'}")

del a
del b
del c

print("Собрано объектов:", gc.collect())

print("Имя независимого узла:", d["name"])
