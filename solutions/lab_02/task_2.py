import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)

original.append(["Databases", 5])
print("\n===После добавления элемента в оригинал===")
print("original", original)
print("alias", alias)
print("shallow", shallow)
print("deep", deep)
original[0][1] = 3

print("\n===После замены элемента во вложенном списке оригинала===")
print("original", original)
print("alias", alias)
print("shallow", shallow)
print("deep", deep)


print("\n=== Идентификаторы внешних списков ===")
print("Исходный список:       ", id(original))
print("Присваивание (alias):  ", id(alias))
print("Поверхностная копия:   ", id(shallow))
print("Глубокая копия:       ", id(deep))

print("\n=== Идентификаторы первых вложенных списков ===")
print("Исходный список:       ", id(original[0]))
print("Присваивание (alias):  ", id(alias[0]))
print("Поверхностная копия:   ", id(shallow[0]))
print("Глубокая копия:       ", id(deep[0]))

print("\n=== Идентификаторы объектов с первой оценкой ===")
print("Исходный список:       ", id(original[0][1]))
print("Присваивание (alias):  ", id(alias[0][1]))
print("Поверхностная копия:   ", id(shallow[0][1]))
print("Глубокая копия:       ", id(deep[0][1]))

wrong_matrix = [[0] * 3] * 3
wrong_matrix[0][0] = 1
print(*wrong_matrix, sep="\n")

correct_matrix = [[0] * 3 for _ in range(3)]
correct_matrix[0][0] = 1

print(*correct_matrix, sep="\n")
