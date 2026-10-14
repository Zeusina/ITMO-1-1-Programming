"""
Программа, принимающая данные об исследователе и эксперименте и расcчитывающая общее время запусков, а также квадрат модуля коэффициента
"""

researcher_name = input("Имя исследователя: ")
experiment_name = input("Название эксперимента: ")
launch_count = int(input("Количество выполненных запусков: "))
launch_duration = float(input("Длительность одного запуска,с: "))
re_coef = float(input("Действительная часть комплексного коэфициента: "))
im_coef = float(input("Мнимая часть комплексного коэфициента: "))

total_duration_sec = launch_count * launch_duration
total_duration_min = total_duration_sec / 60
coef = complex(re_coef,im_coef)
coef_mod_square = coef.imag**2 + coef.real**2
has_runs = bool(launch_count)

print("\n"+"="*20)
print(f"ЭКСПЕРИМЕНТ: {experiment_name}")
print(f"Исследователь: {researcher_name}")
print(f"Запуски: {launch_count}")
print(f"Общее время: {total_duration_sec:.2f} с ({total_duration_min:.2f} мин)")
print(f"Коэффициент: {coef}")
print(f"Квадрат модуля: {coef_mod_square}")
print(f"Есть выполненные запуски: {has_runs}")
print("="*20 + "\n")

print("@"*20)
print("ОТЛАДКА ТИПОВ ДАННЫХ")
print("Тип значения researcher_name: ", type(researcher_name))
print("Тип значения experiment_name: ", type(experiment_name))
print("Тип значения launch_count: ", type(launch_count))
print("Тип значения launch_duration: ", type(launch_duration))
print("Тип значения re_coef: ", type(re_coef))
print("Тип значения im_coef: ", type(im_coef))
print("@"*20)
