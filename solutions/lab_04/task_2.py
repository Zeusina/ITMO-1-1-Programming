import math


class StepRangeIter:
    start = 0
    stop = 0
    step = 1
    current = 0

    def __init__(self, start: int, stop: int, step=1):
        if step == 0:
            raise ValueError("Шаг должен быть не равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start - step

    def __iter__(self):
        return self

    def __next__(self) -> int:
        self.current += self.step
        if (self.step > 0 and self.current >= self.stop) or (
            self.step < 0 and self.current <= self.stop
        ):
            raise StopIteration
        return self.current

    def __len__(self) -> int:
        if self.step > 0 and self.start < self.stop:
            return math.ceil(abs(self.stop - self.start) / abs(self.step))
        elif self.step < 0 and self.start > self.stop:
            return math.ceil(abs(self.start - self.stop) / abs(self.step))
        else:
            return 0

    def __contains__(self, item):
        if self.step > 0 and self.start < self.stop:
            return (self.start <= item < self.stop) and abs(item - self.start) % abs(
                self.step
            ) == 0
        elif self.step < 0 and self.start > self.stop:
            return (self.stop < item <= self.start) and abs(item - self.start) % abs(
                self.step
            ) == 0
        else:
            return False

    def __repr__(self):
        if self.step == 1:
            return "StepRange(" + ",".join(map(str, (self.start, self.stop))) + ")"
        return (
            "StepRange(" + ",".join(map(str, (self.start, self.stop, self.step))) + ")"
        )


class StepRange:
    start = 0
    stop = 0
    step = 1

    def __init__(self, start: int, stop: int, step=1):
        if step == 0:
            raise ValueError("Шаг должен быть не равен 0")
        self.start = start
        self.stop = stop
        self.step = step

    def __iter__(self) -> StepRangeIter:
        return StepRangeIter(self.start, self.stop, self.step)

    def __len__(self) -> int:
        if self.step > 0 and self.start < self.stop:
            return math.ceil(abs(self.stop - self.start) / abs(self.step))
        elif self.step < 0 and self.start > self.stop:
            return math.ceil(abs(self.start - self.stop) / abs(self.step))
        else:
            return 0

    def __contains__(self, item):
        if self.step > 0 and self.start < self.stop:
            return (self.start <= item < self.stop) and abs(item - self.start) % abs(
                self.step
            ) == 0
        elif self.step < 0 and self.start > self.stop:
            return (self.stop < item <= self.start) and abs(item - self.start) % abs(
                self.step
            ) == 0
        else:
            return False

    def __repr__(self):
        if self.step == 1:
            return "StepRange(" + ",".join(map(str, (self.start, self.stop))) + ")"
        return (
            "StepRange(" + ",".join(map(str, (self.start, self.stop, self.step))) + ")"
        )
    


print("\n\n===Проверка класса StepRange===\n")
print("StepRange(0, 5, 1):", list(StepRange(0, 5, 1)))
print("StepRange(5, 0, -1):", list(StepRange(5, 0, -1)))
print("StepRange(0, 0, 1):", list(StepRange(0, 0, 1)))
print("StepRange(0, 5, -1):", list(StepRange(0, 5, -1)))


print("\n\n===Проверки через assert(равенство list(range()))===\n")

assert list(StepRange(0, 5, 1)) == list(range(0, 5, 1))
assert list(StepRange(5, 0, -1)) == list(range(5, 0, -1))
assert list(StepRange(0, 0, 1)) == list(range(0, 0, 1))
assert list(StepRange(0, 5, -1)) == list(range(0, 5, -1))

print("Проверки пройдены")

step_range = StepRange(0, 5, 2)
first_iterator = iter(step_range)
second_iterator = iter(step_range)
print("\nНезависимые итераторы одного StepRange:")
print("Первый итератор:", next(first_iterator))
print("Второй итератор:", next(second_iterator))
print("Первый итератор:", next(first_iterator))
print("Второй итератор:", next(second_iterator))

try:
    StepRange(0, 5, 0)
except ValueError as error:
    print("Ошибка: ", error)
