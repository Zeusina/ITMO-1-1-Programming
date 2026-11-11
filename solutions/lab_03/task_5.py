from collections import defaultdict


def mean(values: list[float | int]) -> float:
    if not values:
        return 0.0
    sm = 0
    for val in values:
        sm += val
    return sm / len(values)


def minimum(values: list[float | int]):
    if not values:
        return 0
    min_val = float("inf")
    for val in values:
        if val < min_val:
            min_val = val
    return min_val


def maximum(values: list[float | int]):
    if not values:
        return 0
    max_val = float("-inf")
    for val in values:
        if val > max_val:
            max_val = val
    return max_val


def classify(score: float) -> str:
    if score < 60:
        return "недостаточный"
    elif 60 <= score <= 74:
        return "удовлетворительный"
    elif 75 <= score <= 89:
        return "хороший"
    else:
        return "отличный"


def student_summary(name, results):
    minv = minimum(results)
    maxv = maximum(results)
    avg = mean(results)
    category = classify(avg)
    return {"min": minv, "max": maxv, "avg": avg, "cat": category}


def find_top_students(students):
    if not students:
        return []
    avgs = {student: mean(scores) for student, scores in students.items()}
    max_avg = maximum(list(avgs.values()))
    return [student for student, avg in avgs.items() if avg == max_avg]


def rank_students(students):
    avgs = {student: mean(scores) for student, scores in students.items()}
    ranked = []
    while avgs:
        maxv = maximum(list(avgs.values()))
        maxs = [student for student in avgs if avgs[student] == maxv]
        ranked.extend(maxs)
        for student in maxs:
            del avgs[student]
    return ranked


def group_summary(students):
    values = []
    for scores in students.values():
        values.extend(scores)
    avgs = {student: mean(scores) for student, scores in students.items()}
    avg = mean(values)
    leaders = find_top_students(students)
    group_count = defaultdict(int)
    for student in avgs:
        group_count[classify(avgs[student])] += 1

    return {
        "leaders": leaders,
        "group_count": group_count,
        "avg": avg,
        "ranking": rank_students(students),
    }


def format_report(student_data, group_data):
    report = "=== ОТЧЕТ ===\n===Статистика по студентам===\n"
    for student in student_data:
        report += (
            f"Студент: {student}\n"
            f"Минимальный балл: {student_data[student]['min']}\n"
            f"Максимальный балл: {student_data[student]['max']}\n"
            f"Средний балл: {student_data[student]['avg']:.2f}\n"
            f"Категория: {student_data[student]['cat']}\n"
            f"{'-' * 10}\n"
        )
    report += "===Статистика по группе===\n"
    report += (
        "Лидеры: "
        + (", ".join(group_data["leaders"]) if group_data["leaders"] else "нет")
        + "\n"
    )
    report += "Статистика по категориям:\n"
    for category in group_data["group_count"]:
        report += f"{category}: {group_data['group_count'][category]}\n"
    report += "-" * 10 + "\n"
    report += f"Средний балл: {group_data['avg']:.2f}\n"
    report += "Рейтинг:\n"
    ranking = group_data.get("ranking", group_data.get("top", []))
    if ranking:
        for c, student in enumerate(ranking, start=1):
            report += f"{c}. {student}\n"
    else:
        report += "список пуст\n"

    return report


# === Базовый запуск ===
students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

student_data = {
    student: student_summary(student, students[student]) for student in students
}
group_data = group_summary(students)

print(format_report(student_data, group_data))


# === 6 сценариев проверки ===
test_cases = {
    "1. Обычный набор данных": {
        "Анна": [78, 91, 84, 88],
        "Борис": [60, 72, 68],
        "Дарья": [95, 93, 97, 90],
    },
    "2. Один студент": {
        "Елена": [80, 85, 90],
    },
    "3. Несколько лидеров": {
        "Алексей": [90, 90],
        "Мария": [90, 90],
        "Петр": [70, 75],
    },
    "4. Пустая группа": {},
    "5. Студент без результатов": {
        "Ольга": [80, 90],
        "Иван": [],
    },
    "6. Граничные значения категорий": {
        "Низ_Недост": [59],
        "Граница_Удовл": [60],
        "Верх_Удовл": [74],
        "Граница_Хор": [75],
        "Верх_Хор": [89],
        "Граница_Отл": [90],
    },
}

print("\n" + "=" * 20 + " ТЕСТОВЫЕ СЦЕНАРИИ " + "=" * 20 + "\n")

for name, group in test_cases.items():
    print(f"\n--- Сценарий: {name} ---")
    s_data = {s: student_summary(s, group[s]) for s in group}
    g_data = group_summary(group)
    print(format_report(s_data, g_data))
