from abc import ABC, abstractmethod
from collections.abc import Callable
from datetime import date, datetime

from task_4 import Student, Submission


class CourseEvent(ABC):
    """Общий интерфейс события учебного курса."""

    @property
    @abstractmethod
    def student_id(self):
        pass

    @property
    @abstractmethod
    def creation_date(self) -> datetime:
        pass

    @abstractmethod
    def describe(self) -> str:
        """Возвращает текстовое описание события."""


class SubmissionEvent(CourseEvent):
    """Событие сдачи лабораторной работы."""

    def __init__(
        self,
        submission: Submission,
    ):
        """Создает событие по объекту сдачи."""
        super().__init__()
        self.__creation_date: datetime = datetime.now()
        self.submission = submission

    @property
    def creation_date(self):
        return self.__creation_date

    def describe(self):
        """Формирует текстовое описание сдачи."""
        return f"Тип: событие попытки. Id студента {self.student_id}. Создан: {self.__creation_date}. Попытка: {self.submission}"

    @property
    def student_id(self):
        return self.submission.student_id


class AttendanceEvent(CourseEvent):
    """Событие посещения занятия студентом."""

    def __init__(self, student_id: str, attendance_date: date):
        """Создает событие с датой посещения."""
        self.attendance_date = attendance_date
        self.__student_id = student_id
        self.__creation_date: datetime = datetime.now()

    @property
    def student_id(self):
        return self.__student_id

    @property
    def creation_date(self):
        return self.__creation_date

    def describe(self):
        """Формирует текстовое описание посещения."""
        return f"Тип: событие посещения. Id студента {self.student_id}. Создан: {self.__creation_date}. Дата посещения: {self.attendance_date}"


class CommentEvent(CourseEvent):
    """Событие с текстовой обратной связью студенту."""

    def __init__(self, student_id: str, comment: str):
        """Создает событие обратной связи."""
        super().__init__()
        self.comment = comment
        self.__student_id = student_id
        self.__creation_date: datetime = datetime.now()

    @property
    def student_id(self):
        return self.__student_id

    @property
    def creation_date(self):
        return self.__creation_date

    def describe(self):
        """Формирует текстовое описание обратной связи."""
        return f"Тип: событие обратной связи. Id студента {self.student_id}. Создан: {self.__creation_date}. Комментарий: {self.comment}"


class DeadlineEvent(CourseEvent):  # Практическое расширение
    """Событие с информацией о сроке сдачи работы."""

    def __init__(self, student_id: str, deadline: datetime):
        """Создает событие со сроком сдачи для указанного студента."""
        self.__student_id = student_id
        self.deadline = deadline
        self.__creation_date = datetime.now()

    @property
    def student_id(self):
        return self.__student_id

    @property
    def creation_date(self):
        return self.__creation_date

    def describe(self) -> str:
        """Возвращает описание срока сдачи."""
        return f"Тип: срок сдачи. Id студента {self.student_id}. Срок: {self.deadline}"


class ScoreView:
    """Ленивое повторно итерируемое представление оценок сдач."""

    def __init__(self, events: list[CourseEvent]):
        """Сохраняет источник событий для последующего обхода."""
        self.__events = events

    def __iter__(self):
        """Выдает оценки сдач без создания промежуточного списка."""
        for event in self.__events:
            if isinstance(event, SubmissionEvent):
                event: SubmissionEvent
                yield event.submission.score


class CourseJournal:
    """Журнал событий курса в порядке их добавления."""

    def __init__(self):
        """Создает пустой журнал."""
        self.__timeline: list[CourseEvent] = []

    def __len__(self):
        return len(self.__timeline)

    def __iter__(self):
        return iter(self.__timeline)

    def __getitem__(self, key):
        """Возвращает событие или срез событий."""
        return self.__timeline[key]

    def events_for_student(self, student_id: str):
        """Лениво выдает события указанного студента."""
        yield from (i for i in self.__timeline if i.student_id == student_id)

    def events_by_type(self, event_type: type):
        """Лениво выдает события заданного типа."""
        yield from (i for i in self.__timeline if type(i) is event_type)

    def add_event(self, event: CourseEvent):
        """Добавляет событие в конец журнала."""
        self.__timeline.append(event)

    @property
    def events(self):
        """Возвращает копию списка событий."""
        return self.__timeline.copy()

    def summary(self):
        """Возвращает количество событий по типам и студентам."""
        events_by_type = {}
        events_by_student = {}

        for event in self.__timeline:
            event_type = type(event).__name__
            events_by_type[event_type] = events_by_type.get(event_type, 0) + 1
            events_by_student[event.student_id] = (
                events_by_student.get(event.student_id, 0) + 1
            )

        return {
            "total_events": len(self.__timeline),
            "events_by_type": events_by_type,
            "events_by_student": events_by_student,
        }

    def __str__(self):
        return f"Журнал курса: {len(self)} событий"

    def __repr__(self):
        return f"CourseJournal(events={len(self)})"


class FilteredJournalView:
    """Ленивое представление журнала, отфильтрованное предикатом."""

    def __init__(
        self,
        journal: CourseJournal,
        predicate: Callable[[CourseEvent], bool],
    ):
        """Сохраняет журнал и функцию проверки событий."""
        self.__journal = journal
        self.__predicate = predicate

    def __iter__(self):
        """Выдает подходящие события, не создавая промежуточный список."""
        yield from (event for event in self.__journal if self.__predicate(event))

def render_timeline(events: list[CourseEvent]) -> str:
    """Формирует временную шкалу, вызывая describe() у каждого события."""
    out = []
    for event in sorted(events, key=lambda x: x.creation_date):
        event: CourseEvent
        out.append(f"{event.creation_date}: {event.describe()}")
    return "\n".join(out)


students = [
    Student("s1", "Анна"),
    Student("s2", "Борис"),
    Student("s3", "Вера"),
]
print("Студенты:", students)

journal = CourseJournal()
journal.add_event(SubmissionEvent(Submission("s1", "lab1", 1, 80.0, "Первая попытка")))
journal.add_event(AttendanceEvent("s2", date(2026, 10, 1)))
journal.add_event(CommentEvent("s3", "Хорошая работа"))
journal.add_event(
    SubmissionEvent(Submission("s1", "lab1", 2, 95.0, "Повторная попытка"))
)
journal.add_event(AttendanceEvent("s1", date(2026, 10, 8)))
journal.add_event(CommentEvent("s2", "Повтори тему итераторов"))
journal.add_event(SubmissionEvent(Submission("s2", "lab2", 1, 88.0)))
journal.add_event(AttendanceEvent("s3", date(2026, 10, 15)))
journal.add_event(CommentEvent("s1", "Задание принято"))
journal.add_event(SubmissionEvent(Submission("s3", "lab1", 1, 72.0)))

print("\nЖурнал:", journal)
print("Представление журнала:", repr(journal))
print("Количество событий:", len(journal))

print("\nСобытия студента s1:")
for event in journal.events_for_student("s1"):
    print(event.describe())

print("\nСобытия типа AttendanceEvent:")
for event in journal.events_by_type(AttendanceEvent):
    print(event.describe())

print("\nСрез журнала [2:5]:")
for event in journal[2:5]:
    print(event.describe())

print("\nВременная шкала:")
print(render_timeline(journal))

scores = ScoreView(journal.events)
score_values = list(scores)
print("\nБаллы из ScoreView:", score_values)
print(
    "Статистика баллов:",
    {
        "количество": len(score_values),
        "среднее": sum(score_values) / len(score_values),
        "минимум": min(score_values),
        "максимум": max(score_values),
    },
)


print("\n\n===Практическое расширение===")

deadline_event = DeadlineEvent("s1", datetime(2026, 12, 1, 23, 59))
journal.add_event(deadline_event)


def is_student_s1_event(event: CourseEvent) -> bool:
    """Проверяет, относится ли событие к студенту s1."""
    return event.student_id == "s1"


named_view = FilteredJournalView(journal, is_student_s1_event)
lambda_view = FilteredJournalView(journal, lambda event: isinstance(event, DeadlineEvent))

print("Фильтрация именованной функцией:", [event.describe() for event in named_view])
print("Фильтрация через lambda:", [event.describe() for event in lambda_view])
print("Повторный обход того же представления:", [event.describe() for event in named_view])
