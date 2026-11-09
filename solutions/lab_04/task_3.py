from collections import deque

raw_lines = ["10.0", "", "12.5", "100.0", "11.5", "13.0", "9.5"]


def read_measurements(lines):
    """Преобразует непустые строки в вещественные числа."""
    for line in lines:
        if line:
            yield float(line)


def filter_range(values, minimum: float, maximum: float):
    """Пропускает только значения из закрытого диапазона."""
    for value in values:
        if minimum < value < maximum:
            yield value


def moving_average(values, window_size: int):
    """Выдает скользящее среднее для заданного размера окна."""
    if window_size <= 0:
        raise ValueError("Некорректный размер окна")

    window = deque(maxlen=window_size)

    for value in values:
        window.append(value)
        if len(window) < window_size:
            continue
        yield sum(window) / window_size


pipeline = moving_average(
    filter_range(read_measurements(raw_lines), 10.0, 20.0),
    2,
)

print("Первое значение конвейера:", next(pipeline))
print("Второе значение конвейера:", next(pipeline))
print("Оставшиеся значения:", list(pipeline))
print("Повторный обход исчерпанного конвейера:", list(pipeline))

new_pipeline = moving_average(
    filter_range(read_measurements(raw_lines), 10.0, 20.0),
    2,
)
print("Новый конвейер:", list(new_pipeline))

print("\n\n===Дополнительные генерао=торы===\n")

squares = [i**2 for i in range(2, 20, 2)]
print("Список квадратов четных чисел от 1 до 20:", squares)

lens = (len(s) for s in raw_lines if s)
print("Длины непустых строк:", list(lens))

squares2 = {i: i**2 for i in range(1, 10)}
print("Словарь чисел и их квадратов:", squares2)

sums = sum(i**2 for i in range(1_000_000))
print("Сумма квадратов чисел от 1 до 999999:", sums)


print("\n\n===Практическое расширение===")


def take(n: int, it):
    if n < 0:
        raise ValueError("n должен быть неотрицательным")
    c = 0
    iterable = iter(it)
    while c != n:
        try:
            yield next(iterable)
        except StopIteration:
            break
        c += 1


def drop(n: int, it):
    if n < 0:
        raise ValueError("n должен быть неотрицательным")
    iterable = iter(it)
    for _ in range(n):
        try:
            next(iterable)
        except StopIteration:
            return

    yield from iterable


def batch(it, size: int):
    if size <= 0:
        raise ValueError("размер должен быть положительным")
    iterable = iter(it)
    while True:
        b = []
        try:
            for _ in range(size):
                b.append(next(iterable))
        except StopIteration:
            if b:
                yield b
            return
        yield b


new_pipeline_2 = take(
    3,
    moving_average(
        filter_range(
            drop(1, read_measurements(raw_lines)),
            10.0,
            20.0,
        ),
        2,
    ),
)
print("\nПакеты обработанных измерений:", list(batch(new_pipeline_2, 1)))


import gc
import tracemalloc

gc.collect()
tracemalloc.start()
values = (number for number in range(100_000))
processed = (number * 2 for number in values)
filtered = (number for number in processed if number % 3 == 0)
lazy_total = 0
for number in filtered:
    lazy_total += number
_, lazy_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

gc.collect()
tracemalloc.start()
values = list(range(100_000))
processed = [number * 2 for number in values]
filtered = [number for number in processed if number % 3 == 0]
list_total = sum(filtered)
_, list_peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print("Пиковая память ленивого конвейера:", lazy_peak, "байт")
print("Пиковая память конвейера со списками:", list_peak, "байт")
