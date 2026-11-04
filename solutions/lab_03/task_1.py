from collections import defaultdict


def check_inputs(student_result, work_type, missed_classes):
    if not 0 <= student_result <= 100:
        print("Результат студента должен быть числом от 0 до 100")
        return False
    elif not 0 <= missed_classes <= 5:
        print("Количество пропущенных занятий должно быть не больше 5")
        return False
    return True


def calculate_grade(student_result, missed_classes):
    grade = 0
    if student_result < 60:
        grade = 0
    elif 60 <= student_result <= 74:
        grade = 1
    elif 75 <= student_result <= 89:
        grade = 2
    else:
        grade = 3

    if missed_classes > 3 and grade > 0:
        grade -= 1

    match grade:
        case 0:
            return "недостаточный"
        case 1:
            return "удовлетворительный"
        case 2:
            return "хороший"
        case 3:
            return "отличный"


def convert_work_type(work_type):
    match work_type:
        case "exam":
            return "экзаменационная работа"
        case "project":
            return "проектная работа"
        case "practice":
            return "практическая работа"
        case _:
            return "неизвестный тип - " + work_type


student_result = int(input("Введите результат студента: "))
work_type = input("Введите тип работы: ")
missed_classes = int(input("Введите количество пропусков: "))
if check_inputs(student_result, work_type, missed_classes):
    grade = calculate_grade(student_result, missed_classes)
    work_type_verbose = convert_work_type(work_type)
    print(work_type_verbose, "-", grade)


test_data = [
    (0, "exam", 0),
    (59, "practice", 3),
    (60, "project", 4),
    (74, "exam", 5),
    (75, "practice", 2),
    (89, "project", 4),
    (90, "exam", 3),
    (100, "project", 5),
    (50, "practice", 4),
    (101, "exam", 2),
    (85, "project", 6),
    (92, "unknown", 1),
]

stats = defaultdict(int)

for i in test_data:
    student_result, work_type, missed_classes = i

    if check_inputs(student_result, work_type, missed_classes):
        grade = calculate_grade(student_result, missed_classes)
        stats[grade] += 1
        work_type_verbose = convert_work_type(work_type)
        print(work_type_verbose, "-", grade)

print("\n===Статистика===")
for grade_name, cnt in stats.items():
    print(f"{grade_name} - {cnt}")
