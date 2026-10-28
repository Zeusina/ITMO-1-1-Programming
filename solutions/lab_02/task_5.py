import sys

# Часть 1
print("\n\n===Часть 1===\n")

print("Размер пустого списка:", sys.getsizeof([]))
print(
    "Размер списка из десяти целых чисел:",
    sys.getsizeof([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]),
)
print(
    "Размер кортежа из десяти целых чисел:",
    sys.getsizeof((1, 2, 3, 4, 5, 6, 7, 8, 9, 0)),
)
print("Размер строки из десяти символов", sys.getsizeof("1234567890"))
print("Размер целого числа:", sys.getsizeof(1))
print("Размер объекта None:", sys.getsizeof(None))


# Часть 2
print("\n\n===Часть 2===\n")


l = []
prev = sys.getsizeof(l)

for i in range(100):
    l.append(i)
    new = sys.getsizeof(l)
    if prev != new:
        print("Длина списка:", len(l))
        print("Размер списка:", new)
        prev = new


# Часть 3

# Вынесено в memory_report.py
