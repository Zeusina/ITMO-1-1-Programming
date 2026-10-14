# Эксперимент 1

import sys

data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))


# Эксперимент 2
import weakref


class Record:
    pass


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())

# Практическое задание

registry = weakref.WeakValueDictionary()

o_1 = Record()
o_2 = Record()

registry["o-1"] = o_1
registry["o-2"] = o_2
registry["o-3"] = Record()

print(*registry.keys())  # Только o-1 и o-2

del o_2

print(*registry.keys())  # Только o-1
