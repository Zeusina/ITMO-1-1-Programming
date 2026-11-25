from dataclasses import dataclass


@dataclass
class Submission:
    """Результат одной попытки сдачи лабораторной работы."""
    student_id: str
    laboratory_id: str
    attempt: int
    score: float
    comment: str = ""

    def __post_init__(self):
        """Проверяет идентификаторы, номер попытки и границы балла."""
        if not self.student_id or not self.laboratory_id:
            raise ValueError("Идентификаторы должны быть непустыми")
        if self.attempt <= 0:
            raise ValueError("Номер попытки должен быть положительным")
        if self.score > 100 or self.score < 0:
            raise ValueError(
                "Результат должен быть в пределах от 0 до 100(включительно)"
            )

    def __eq__(self, value: "Submission"):
        """Сравнивает сдачи по значениям всех полей."""
        return bool(
            self.student_id == value.student_id
            and self.laboratory_id == value.laboratory_id
            and self.attempt == value.attempt
            and self.score == value.score
            and self.comment == value.comment
        )


class Student:
    """Студент и его попытки сдачи лабораторных работ."""

    def __init__(self, student_id: str, name: str):
        """Создает студента с идентификатором и непустым именем."""
        if not name:
            raise ValueError("Имя студента не должно быть пустым")
        self.check_id(student_id)
            

        self.student_id = student_id
        self.name = name
        self.__submissions: list[Submission] = []

    def add_submission(self, submission: Submission):
        self.__submissions.append(submission)

    @property
    def submissions(self):
        """Возвращает кортеж попыток без доступа к внутреннему списку."""
        return tuple(self.__submissions)

    @property
    def sorted_submissions(self):
        """Возвращает копию попыток, отсортированную по номеру и баллу."""
        return sorted(self.__submissions, key=lambda x: (x.attempt, x.score))

    @property
    def average_score(self):
        """Вычисляет средний балл студента."""
        return sum(i.score for i in self.__submissions) / len(self)

    def best_score(self, laboratory_id: str):
        """Возвращает лучший балл по указанной лабораторной работе."""
        return max(
            i.score for i in self.__submissions if i.laboratory_id == laboratory_id
        )

    def __iter__(self):
        return iter(self.__submissions)

    def __len__(self):
        return len(self.__submissions)

    def __str__(self):
        return f"Студент {self.name} - {len(self)} попыток, средний балл: {self.average_score()}"

    def __repr__(self):
        return f"Student(id={self.student_id},name={self.name},submissions:{self.submissions})"

    @staticmethod
    def from_full_name(student_id: str, full_name: str):
        """Создает студента, используя полное имя."""
        return Student(student_id=student_id, name=full_name)

    @staticmethod
    def check_id(student_id: str):
        """Проверяет, что идентификатор является непустой строкой."""
        if not student_id:
            raise ValueError("id не может быть пустым")
        if type(student_id) is not str:
            raise TypeError("id должен быть строкой")


class Course:
    """Курс, хранящий студентов по идентификаторам."""

    def __init__(self):
        self.__students: dict[str, Student] = {}

    def __iter__(self):
        return iter(self.__students.values())

    def __len__(self):
        return len(self.__students.values())

    def __contains__(self, item: Student):
        """Проверяет регистрацию студента по его идентификатору."""
        return item.student_id in self.__students

    def add_student(self, student: Student):
        self.__students[student.student_id] = student

    def get_student(self, student_id: str):
        """Возвращает студента курса по идентификатору."""
        if student_id not in self.__students:
            raise ValueError("Студента нет на курсе")

        return self.__students[student_id]

    def submit(self, submission: Submission):
        """Добавляет сдачу студенту, зарегистрированному на курсе."""
        if submission.student_id not in self.__students:
            raise ValueError("Студента нет на курсе")

        self.__students[submission.student_id].add_submission(submission)

    def top_students(self, limit: int = 3):
        """Возвращает ограниченный список лучших студентов."""
        if limit <= 0:
            raise ValueError("Лимит должен быть положительным числом")

        return sorted(self.__students.values(), key=lambda x: x.average_score, reverse=True)[
            : min(len(self.__students), limit)
        ]
