import sys
import tracemalloc

data = []
data.append({"name": "Тест 1 - материализация range"})
tracemalloc.start()

numbers = list(range(100_000))

data[0]["mem_cur"], data[0]["mem_peak"] = tracemalloc.get_traced_memory()
data[0]["ext_obj_size"] = sys.getsizeof(numbers)
data[0]["elem_count"] = len(numbers)
tracemalloc.stop()

del numbers
data.append({"name": "Тест 2 - хранение range"})
tracemalloc.start()

numbers = range(100_000)

data[1]["mem_cur"], data[1]["mem_peak"] = tracemalloc.get_traced_memory()
data[1]["ext_obj_size"] = sys.getsizeof(numbers)
data[1]["elem_count"] = len(numbers)
tracemalloc.stop()

for i in data:
    print("=" * 30)
    print("Название эксперимента:", i["name"])
    print("Число элементов:", i["elem_count"])
    print("Размер внешнего объекта:", i["ext_obj_size"])
    print(f"Текущий объем выделенной памяти: {i['mem_cur'] / 1024:.5f}КБ")
    print(f"Пиковый объем выделенной памяти: {i['mem_peak'] / 1024:.5f}КБ")

print("=" * 30)
print(
    f"Отношение пикового объема двух сценариев: {data[0]['mem_peak'] / data[1]['mem_peak']:.3f}"
)
