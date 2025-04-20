from .base import Course
from .interfaces import Teachable, Assessable
from .mixins import LoggingMixin, NotificationMixin

class ScienceCourse(LoggingMixin, NotificationMixin, Course, Teachable, Assessable):
    """
    Класс для представления научного курса.

    Атрибуты:
    ---------
    title : str
        Название курса.
    start_date : str
        Дата начала курса.
    end_date : str
        Дата окончания курса.
    instructor : str
        Преподаватель курса.
    students : list
        Список студентов, участвующих в курсе.
    topics : list
        Список тем, которые будут охвачены в курсе.
    field : str
        Область науки, изучаемая на курсе (например, физика, химия и т.д.).

    """

    def __init__(self, title, start_date, end_date, instructor, students, topics, field):
        """
        Инициализирует курс науки с указанными параметрами.

        :param title: Название курса.
        :param start_date: Дата начала курса.
        :param end_date: Дата окончания курса.
        :param instructor: Преподаватель курса.
        :param students: Список студентов.
        :param topics: Список тем.
        :param field: Область науки, изучаемая на курсе.
        """
        super().__init__(title, start_date, end_date, instructor, students, topics)
        self._field = field

    def calculate_completion_rate(self) -> float:
        """
        Вычисляет процент завершения курса на основе количества студентов.

        :return: Процент завершения (количество студентов умножается на 5).
        """
        return len(self.students) * 5

    def teach(self):
        """
        Проводит лабораторные работы по курсу.
        """
        print("Провожу лабораторные работы.")

    def assess_progress(self):
        """
        Оценивает результаты лабораторных экспериментов и тестов.
        """
        print("Проверяю результаты лабораторных экспериментов и тестов.")

    def __str__(self):
        """
        Возвращает строковое представление курса.

        :return: Строка с названием курса и областью науки.
        """
        return f"Курс наук: {self.title}, Область: {self._field}"

    def to_dict(self):
        """
        Преобразует объект курса в словарь для сериализации.

        :return: Словарь с аттрибутами курса.
        """
        base = super().to_dict()
        base["field"] = self._field
        return base
