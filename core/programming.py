from .base import Course
from .interfaces import Teachable, Assessable
from .metaclass import CourseMeta
from .mixins import LoggingMixin, NotificationMixin

class ProgrammingCourse(LoggingMixin, NotificationMixin, Course, Teachable, Assessable):
    """
    Класс для представления курса программирования.

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
        Список тем, которые будут покрыты в курсе.
    languages : list
        Список языков программирования, изучаемых на курсе.

    """

    def __init__(self, title, start_date, end_date, instructor, students, topics, languages):
        """
        Инициализирует курс программирования с указанными параметрами.

        :param title: Название курса.
        :param start_date: Дата начала курса.
        :param end_date: Дата окончания курса.
        :param instructor: Преподаватель курса.
        :param students: Список студентов.
        :param topics: Список тем.
        :param languages: Список языков программирования.
        """
        super().__init__(title, start_date, end_date, instructor, students, topics)
        self._languages = languages

    def calculate_completion_rate(self) -> float:
        """
        Вычисляет процент завершения курса.
        :return: Процент завершения (количество тем умножается на 10).
        """
        return len(self.topics) * 10

    def teach(self):
        """
        Проводит лекции по курсу программирования.
        """
        print("Провожу лекции по алгоритмам.")

    def assess_progress(self):
        """
        Оценивает выполнение лабораторных и тестов по программированию.
        """
        print("Оцениваю выполнение лабораторных и тестов по программированию.")

    def __str__(self):
        """
        Возвращает строковое представление курса.

        :return: Строка с названием курса и языками программирования.
        """
        return f"Курс программирования: {self.title}, Языки: {', '.join(self._languages)}"

    def to_dict(self):
        """
        Преобразует объект курса в словарь для сериализации.

        :return: Словарь с аттрибутами курса.
        """
        base = super().to_dict()
        base["languages"] = self._languages
        return base