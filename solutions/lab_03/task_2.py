import time


def linear_search(a, a_len, query):
    for i in range(a_len):
        if a[i] == query:
            return i
    return -1


measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]


min_value = float("inf")
max_value = float("-inf")
sm = 0  # Сумма элементов
count_even = 0  # Количество четных
count = 0

for i in measurements:
    sm += i
    if i < min_value:
        min_value = i
    if i > max_value:
        max_value = i
    if i % 2 == 0:
        count_even += 1
    count += 1

avg = sm / count
count_gr_avg = 0  # Количество больших среднего арифметического
for i in measurements:
    if i > avg:
        count_gr_avg += 1

print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Сумма элементов:", sm)
print("Количество четных элементов:", count_even)
print("Количество элементов больших среднего арифметического:", count_gr_avg)


searchable = int(input("Введите число для поиска: "))

print("Индекс числа: ", linear_search(measurements, count, searchable))


def is_simple(a):  # Время алгоритма О(sqrt(n))
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True


# Бинарный поиск. Возвращает (индекс, число проверенных элементов).
def bin_search(a, start, stop, search):
    if start > stop:
        return -1, 0
    mid = (start + stop) // 2
    if a[mid] > search:
        index, comparisons = bin_search(a, start, mid - 1, search)
    elif a[mid] < search:
        index, comparisons = bin_search(a, mid + 1, stop, search)
    else:
        return mid, 1
    return index, comparisons + 1


# Сортировка выбором
def select_sort(data, d_len):
    c = 0
    for i in range(d_len - 1):
        cur_min_index = i
        for j in range(i + 1, d_len):
            c += 1
            if data[j] < data[cur_min_index]:
                cur_min_index = j

        data[i], data[cur_min_index] = data[cur_min_index], data[i]

    return data, c


def linear_search(a, query): # Переопределяем поиск для подсчета сравнений
    c = 0
    for i in range(len(a)):
        c += 1
        if a[i] == query:
            return i, c
    return -1, c


# Замеры на одинаковых наборах данных
for size in [10, 100, 1000]:
    data = list(range(size, 0, -1))

    start = time.perf_counter()
    data, sort_count = select_sort(data, size)
    sort_time = time.perf_counter() - start

    target = 0  # Худший случай, когда элемента нет в списке

    start = time.perf_counter()
    linear_count = linear_search(data, target)[1]
    linear_time = time.perf_counter() - start

    start = time.perf_counter()
    binary_count = bin_search(data, 0, size - 1, target)[1]
    binary_time = time.perf_counter() - start

    print("\nРазмер массива:", size)
    print("Сравнения сортировки выбором:", sort_count)
    print("Сравнения линейного поиска:", linear_count)
    print("Сравнения бинарного поиска:", binary_count)
    print("Время сортировки выбором:", round(sort_time * 1000, 4), "мс")
    print("Время линейного поиска:", round(linear_time * 1000, 4), "мс")
    print("Время бинарного поиска:", round(binary_time * 1000, 4), "мс")
