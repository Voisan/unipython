import json
from typing import List


def save_courses(courses: List['Course'], filename="courses.json"):
    """
    Сохраняет список курсов в файл в формате JSON.

    :param courses: Список объектов курса для сохранения.
    :param filename: Имя файла для сохранения данных (по умолчанию "courses.json").
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump([course.to_dict() for course in courses], f, ensure_ascii=False, indent=2)


def load_courses(factory: 'CourseFactory', filename="courses.json") -> List['Course']:
    """
    Загружает курсы из файла JSON и создает объекты с помощью фабрики.

    :param factory: Фабрика для создания объектов курса.
    :param filename: Имя файла для загрузки данных (по умолчанию "courses.json").
    :return: Список объектов курсов.
    """
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [factory.create_course(**course) for course in data]


class Serializer:
    """
    Класс для сериализации и десериализации объектов курсов в/из файлов.
    """

    @staticmethod
    def save_to_file(course: 'Course', filename: str):
        """
        Сохраняет объект курса в файл в формате JSON.

        :param course: Объект курса для сохранения.
        :param filename: Имя файла для сохранения данных.
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(course.to_dict(), f, ensure_ascii=False, indent=4)

    @staticmethod
    def load_from_file(cls: 'Course', filename: str) -> 'Course':
        """
        Загружает объект курса из файла JSON и создает его с помощью метода from_dict.

        :param cls: Класс курса, который будет создан из файла.
        :param filename: Имя файла для загрузки данных.
        :return: Объект курса, созданный из данных файла.
        """
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return cls.from_dict(data)
