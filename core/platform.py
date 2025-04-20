from typing import List
from .exceptions import CourseNotFoundError
from core.logger import logger

class Address:
    """
    Класс для представления адреса платформы.
    Содержит информацию о стране,городе, улице, здании организации и ссылку на сайт

    Атрибуты:
    ---------
    country : str
        Название страны
    city : str
        Название города.
    street : str
        Название улицы.
    building : str
        Номер здания.
    site : str
        Ссылка на сайт платформы
    """

    def __init__(self, country:str,city: str, street: str, building: str,site: str):
        """
        Инициализирует объект Address.
        :param country: Название страны.
        :param city: Название города.
        :param street: Название улицы.
        :param building: Номер здания.
        :param site: ссылка на платформу

        """
        self.country= country
        self.city = city
        self.street = street
        self.building = building
        self.site = site


    def __str__(self):
        """
        Возвращает строковое представление адреса.

        :return: Строка с адресом.
        """
        return f"{self.country},{self.city}, {self.street}, {self.building}.Ссылка: {self.site}."


class Platform:
    """
    Класс для представления образовательной платформы.
    Содержит информацию о платформе, её адресе и курсы, доступные на платформе.

    Атрибуты:
    ---------
    address : Address
        Адрес платформы.
    _courses : list
        Список курсов, добавленных на платформу.
    """

    def __init__(self, address: Address):
        """
        Инициализирует платформу с адресом и пустым списком курсов.

        :param address: Адрес платформы.
        """
        self.address = address
        self._courses = []

    def add_course(self, course):
        """
        Добавляет курс на платформу и уведомляет студентов о добавлении курса.

        :param course: Курс, который будет добавлен на платформу.
        """
        self._courses.append(course)
        course.log_action("добавлен на платформу")  # Логируем добавление курса
        course.notify_students("Курс добавлен на платформу.")  # Уведомляем студентов

    def remove_course(self, title: str):
        """
        Удаляет курс с платформы по названию. Если курс не найден, возбуждает ошибку.

        :param title: Название курса для удаления.
        :raises CourseNotFoundError: Если курс не найден.
        """
        course = next((c for c in self._courses if c.title == title), None)
        if not course:
            raise CourseNotFoundError(f"Курс '{title}' не найден.")
        self._courses.remove(course)
        print(f"Курс '{title}' удален.")

    def get_courses(self) -> List:
        """
        Возвращает список всех курсов на платформе.

        :return: Список курсов.
        """
        return self._courses

    def get_top_courses(self, n=3):
        """
        Возвращает топ-N курсов на платформе по числу студентов.

        :param n: Количество курсов в топе (по умолчанию 3).
        :return: Список топ-N курсов.
        """
        return sorted(self._courses, key=lambda c: len(c.students), reverse=True)[:n]
