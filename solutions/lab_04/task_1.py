from task_2 import StepRange

values = [10, 20, 30]
iterator = iter(values)

print(iterator is values)
print(iter(iterator) is iterator)
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))


def consume(iterable) -> list:
    """Собирает элементы iterable, вручную используя iter() и next()."""
    it = iter(iterable)
    res = []
    while True:
        try:
            res.append(next(it))
        except StopIteration:
            return res


print("\n\n===Проверка функции consume===\n")

values_list = [10, 20, 30]
values_tuple = (10, 20, 30)
values_string = "Python"
values_range = range(1, 6)

print("Список:", consume(values_list))
print("Кортеж:", consume(values_tuple))
print("Строка:", consume(values_string))
print("Объект range:", consume(values_range))

partially_used_iterator = iter(values_list)
print("Первый элемент итератора:", next(partially_used_iterator))
print("Остаток частично использованного итератора:", consume(partially_used_iterator))

print("\nПовторный обход списка:", consume(values_list))
iterator = iter(values_list)
print("Первый обход итератора:", consume(iterator))
print("Повторный обход итератора:", consume(iterator))


print("\n\n===Практическое расширение===\n")


def my_enumerate(iterable, start=0):
    it = iter(iterable)
    res = []
    i = start
    for elem in it:
        res.append((i, elem))
        i += 1
    return res


def my_zip(first, second):
    it1 = iter(first)
    it2 = iter(second)
    res = []
    while True:
        try:
            el1 = next(it1)
            el2 = next(it2)
            res.append((el1, el2))
        except StopIteration:
            return res


print("my_enumerate(), список:", my_enumerate(["a", "b", "c"]))
print("my_enumerate(), строка:", my_enumerate("кот", start=1))
print("my_enumerate(), генератор:", my_enumerate(x * 2 for x in range(3)))

print("my_zip(), списки:", my_zip([1, 2, 3], ["a", "b"]))
print("my_zip(), строки:", my_zip("кот", "домик"))
print(
    "my_zip(), генераторы:",
    my_zip((x for x in range(3)), (x * 10 for x in range(2))),
)

