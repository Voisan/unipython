from .base import Course
from .interfaces import Teachable, Assessable
from .mixins import LoggingMixin, NotificationMixin

class DesignCourse(LoggingMixin, NotificationMixin, Course, Teachable, Assessable):
    """
    Класс курса по дизайну.

    Наследуется от:
        - LoggingMixin: логирование действий
        - NotificationMixin: уведомления для студентов
        - Course: базовый курс
        - Teachable: интерфейс для проведения занятий
        - Assessable: интерфейс для оценки прогресса

    Атрибуты:
        title (str): название курса
        start_date (str): дата начала
        end_date (str): дата окончания
        instructor (str): имя преподавателя
        students (list): список студентов
        topics (list): список тем
        tools (list): используемые инструменты (например, Figma, Photoshop и др.)
    """

    def __init__(self, title, start_date, end_date, instructor, students, topics, tools):
        """
        Инициализация курса по дизайну.

        :param title: название курса
        :param start_date: дата начала
        :param end_date: дата окончания
        :param instructor: преподаватель курса
        :param students: список студентов
        :param topics: список тем
        :param tools: список инструментов
        """
        super().__init__(title, start_date, end_date, instructor, students, topics)
        self._tools = tools

    def calculate_completion_rate(self) -> float:
        """
        Вычисляет условную степень завершенности курса.

        :return: значение в процентах (по количеству тем)
        """
        return len(self.topics) * 15

    def teach(self):
        """
        Метод, реализующий проведение урока по дизайну.
        """
        print("Провожу уроки по дизайну.")

    def assess_progress(self):
        """
        Метод для оценки прогресса студентов по курсу дизайна.
        """
        print("Оцениваю креативность и оформление проектов по дизайну.")

    def __str__(self):
        """
        Представление курса в виде строки.

        :return: строка с информацией о курсе
        """
        return f"Курс дизайна: {self.title}, Инструменты: {', '.join(self._tools)}"

    def to_dict(self):
        """
        Преобразует курс в словарь (например, для сериализации).

        :return: словарь с информацией о курсе
        """
        base = super().to_dict()
        base["tools"] = self._tools
        return base
