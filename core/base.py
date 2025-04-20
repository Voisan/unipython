from datetime import datetime
from typing import Dict, List

from core.logger import logger
from .exceptions import InvalidDateError,check_permissions
from abc import ABC, abstractmethod
from .metaclass import CourseMeta
import json

class Course(ABC, metaclass=CourseMeta):
    """
        Абстрактный базовый класс, представляющий учебный курс на образовательной платформе.

        Атрибуты:
            title (str): Название курса.
            start_date (str): Дата начала курса в формате "YYYY-MM-DD".
            end_date (str): Дата окончания курса в формате "YYYY-MM-DD".
            instructor (str): Имя преподавателя.
            students (Dict[str, float]): Словарь студентов с их баллами.
            topics (List[str]): Список тем курса.

        Исключения:
            InvalidDateError: Если дата окончания раньше даты начала.

        Методы:
            set_current_user(name: str, role: str): Устанавливает текущего пользователя.
            update_score(student_name: str, score: float): Обновляет балл студента (только для instructor).
            log_action(message: str): Логирует действие курса.
            to_dict(): Сериализует объект курса в словарь.
            from_dict(data: dict): Восстанавливает объект курса из словаря.
            save_to_file(filename: str): Сохраняет курс в JSON-файл.
            load_from_file(filename: str): Загружает курс из JSON-файла.
            duration(): Возвращает продолжительность курса в днях.
            __eq__, __lt__, __gt__: Методы сравнения курсов по числу студентов.
        """
    def __init__(self, title, start_date, end_date, instructor, students: list, topics: list):
        self._title = title
        self._start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self._end_date = datetime.strptime(end_date, "%Y-%m-%d")
        self._instructor = instructor
        self._students: Dict[str, int] = {name: 0 for name in students}  # Заменил список на словарь
        self._topics = topics
        if self._end_date < self._start_date:
            raise InvalidDateError("Дата окончания курса раньше даты начала")

    def set_current_user(self, name: str, role: str):
        self.current_user = {"name": name, "role": role}

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def start_date(self) -> str:
        return self._start_date.strftime("%Y-%m-%d")

    @property
    def end_date(self) -> str:
        return self._end_date.strftime("%Y-%m-%d")

    @property
    def instructor(self) -> str:
        return self._instructor

    @property
    def students(self) -> Dict[str, float]:
        return self._students

    @property
    def topics(self) -> List[str]:
        return self._topics

    @abstractmethod
    def calculate_completion_rate(self) -> float:
        pass

    def __str__(self):
        return f"Курс: {self._title}, Преподаватель: {self._instructor}"

    def __eq__(self, other):
        return len(self._students) == len(other._students)

    def __lt__(self, other):
        return len(self._students) < len(other._students)

    def __gt__(self, other):
        return len(self._students) > len(other._students)

    def duration(self):
        return (self._end_date - self._start_date).days

    def to_dict(self):
        return {
            "course_type": self.__class__.__name__.replace("Course", "").lower(),
            "title": self.title,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "instructor": self.instructor,
            "students": self._students,
            "topics": self._topics
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

    def save_to_file(self, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=4)

    @classmethod
    def load_from_file(cls, filename: str):
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        return cls.from_dict(data)

    @check_permissions("instructor")
    def update_score(self, student_name: str, score: float):
        if student_name not in self._students:
            raise ValueError(f"Студент '{student_name}' не найден в списке.")
        self._students[student_name] = score

    def log_action(self, message):
        logger.info(f"{self.title}: {message}")