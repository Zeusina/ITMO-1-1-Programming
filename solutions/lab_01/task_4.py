student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

print("Первый символ имени:", student[0])
print("Последний символ имени:", student[3])

print("Имя:", student[:4])
print("Фамилия:", student[5:])

print("Нижний регистр:", student.lower())
print("Верхний регистр:", student.upper())

print("Инициалы:", student[0] + "." + student[5] + ".")

print("Название в обратном порядке:", course[::-1])

# Через %
print("%s - %s: %d/%d (%.1f%%)" % (student,course,completed,total,completed/total*100))

# Через format
print("{} - {}: {}/{} ({:.1f}%)".format(student,course,completed,total,completed/total*100))

# Через f-строку
print(f"{student} - {course}: {completed}/{total} ({completed/total*100:.1f}%)")

symbol = "Я"
print(symbol)
print("Позиция:", ord(symbol))
print("Восстановленный символ", chr(ord(symbol)))
print("Закодированный символ:", symbol.encode("utf-8"))
print("Длина закодированного символа", len(symbol.encode("utf-8")))

# symbol[0] = "А"