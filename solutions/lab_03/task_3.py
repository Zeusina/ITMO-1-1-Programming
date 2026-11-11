from collections import defaultdict

submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]

students = {i[0] for i in submissions}
print("Студенты:", students)

submitted_labs = {i[1] for i in submissions}
print("Сданные лабораторные:", submitted_labs)

tries = defaultdict(list)
best = defaultdict(int)
count = defaultdict(int)
for submission in submissions:
    tries[submission[0]].append(submission[1:])
    best[submission[:2]] = max(best[submission[:2]], submission[2])
    count[submission[:2]] += 1
print("Попытки по студентам:", dict(tries))
print("Результаты по студенту и лабораторной", dict(best))
print("Количество попыток:", dict(count))

lab_01_students = {s for s, lab, _ in submissions if lab == "lab_01"}
lab_02_students = {s for s, lab, _ in submissions if lab == "lab_02"}

print("Студенты, сдававшие обе лабораторные:", lab_01_students & lab_02_students)

submissions.append(("daria", "lab_02", 5))

students.add(submissions[-1][0])
submitted_labs.add(submissions[-1][1])
tries[submissions[-1][0]].append(submissions[-1][1:])
best[submissions[-1][:2]] = max((submissions[-1][2]), best[submissions[-1][:2]])
count[submissions[-1][:2]] += 1

print("\n\n===После добавления нового элемента в сдачи===\n")

print("Студенты:", students)
print("Сданные лабораторные:", submitted_labs)
print("Попытки по студентам:", dict(tries))
print("Результаты по студенту и лабораторной:", dict(best))
print("Количество попыток:", dict(count))


print("\nВведите команду или нажмите ENTER чтобы завершить.")
inp = input("> ")
while inp != "":
    cmd = inp.split()
    match cmd:
        case ["student", student]:
            if student in students:
                print(f"Попытки студента {student}: {tries[student]}")
            else:
                print("Студент не найден")
        case ["completed", lab]:
            if lab not in submitted_labs:
                print("Такую лабораторную не сдавали")
            else:
                print(
                    f"Студенты сдавшие лабораторную {lab}: {set(submission[0] for submission in submissions if submission[1] == lab)}"
                )
        case ["best", student, lab]:
            key = (student, lab)
            if key in best:
                print(
                    f"Лучший результат студента {student} для лабораторной {lab}: {best[(student, lab)]}"
                )
            else:
                print("Результат не найден")
        case ["attempts", student, lab]:
            key = (student, lab)
            if key in count:
                print(
                    f"Количество попыток {student} для лабораторной {lab}: {count[(student, lab)]}"
                )
            else:
                print("Результат не найден")
        case _:
            print("Неизвестная или неполная команда")
    inp = input("> ")
