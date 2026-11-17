def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка."""
    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    clear_name: list[str] = [i.capitalize() for i in name.split()]
    return " ".join(clear_name)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    report = f"Студент {student}\n"
    c = 1
    for result in results:
        report += f"{prefix} {c} - {result}\n"
        c += 1
    if len(results) != 0:
        report += f"Средний балл: {sum(results) / len(results):.{precision}f}"
    return report


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    res = set()
    for tag in tags:
        stag = tag.strip()
        if stag:
            if lowercase:
                res.add(stag.lower())
            else:
                res.add(stag)
    return tuple(res)


assert arithmetic_mean([1, 2, 3]) == 2
assert arithmetic_mean([10]) == 10
assert arithmetic_mean([2.5, 3.5]) == 3.0

assert normalize_name("  аННа   пЕтРоВа ") == "Анна Петрова"
assert normalize_name("boris") == "Boris"
assert normalize_name("  ") == ""

assert isinstance(build_report("Анна", [5, 4, 5]), str)
assert "Анна" in build_report("Анна", [5, 4, 5])
assert "Результат 1 - 5" in build_report("Анна", [5, 4, 5])
assert "Средний балл" in build_report("Анна", [5, 4, 5])

assert isinstance(collect_tags("python"), tuple)
assert collect_tags("Python", "python", " Python ") == ("python",)
assert set(collect_tags("A", "B", lowercase=False)) == {"A", "B"}
assert collect_tags("", "  ", "ok") == ("ok",)

print("\n===Вызовы функций===\n")
# Вызовы с позиционными и именованными аргументами
print("Среднее (позиционные):", arithmetic_mean([4, 5, 3]))
print("Среднее (именованный):", arithmetic_mean(values=[4, 5, 3]))

print("Имя:", normalize_name("  аННа   пЕтРоВа "))

print(build_report("Анна", [5, 4, 5]))
print(build_report("Анна", [5, 4, 5], precision=1, prefix="Оценка"))

print("Теги (нижний регистр):", collect_tags("Python", "PYTHON", " OOP "))
print(
    "Теги (без изменений):", collect_tags("Python", "PYTHON", " OOP ", lowercase=False)
)


print("\n===Распаковка списка и словаря===\n")
# Распаковка списка через * и словаря через **
report_args = ["Борис", [4, 5, 3]]
report_options = {"precision": 1, "prefix": "Балл"}
print(build_report(*report_args))
print(build_report(*report_args, **report_options))

tags = ["Python", "python", " OOP "]
print("Теги:", collect_tags(*tags))


course = "Курс 1"


print("\n===Исследование LEGB===\n")


def ext_func():
    course = "Курс 2"
    print("После изменения во внешней функции")

    def int_func():
        nonlocal course
        print("До изменения:", course)
        course = "Курс 3"
        print("После изменения локально:", course)

    int_func()
    print("После локальной функции:", course)


ext_func()
print("После глобальной функции:", course)


print("\n===Ошибка изменяемого значения по умолчанию===\n")


def add_result(value, results=None):
    if results is None:
        results = []
    results.append(value)
    return results


print(add_result(3))  # Выводится [3] до исправления
print(add_result(4))  # Выводится [3,4] до исправления


print("\n===Практическое расширение===\n")


def apply_to_results(operation, values):
    return [operation(value) for value in values]


def double(a):
    return a * 2


print("Применение функции double:", apply_to_results(double, [1, 2, 3]))
print("Применение lambda x * 3:", apply_to_results(lambda x: x * 3, [1, 2, 3]))


def make_threshold_checker(threshold):
    def check(value):
        return value >= threshold

    return check


print("\nПроверка пороговых значений (замыкания)")
check3 = make_threshold_checker(3)
check4 = make_threshold_checker(4)

print("Порог 3, значение 3:", check3(3))
print("Порог 3, значение 4:", check3(4))
print("Порог 4, значение 3:", check4(3))
print("Порог 4, значение 4:", check4(4))
print("Порог 3, значение 3:", check3(3))
print("Порог 3, значение 4:", check3(4))
