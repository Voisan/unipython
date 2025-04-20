from .metaclass import CourseMeta

class CourseFactory:
    """
    Фабрика курсов, использующая метакласс CourseMeta для динамического создания объектов курсов.

    Позволяет создавать курсы на основе строки `course_type`, которая соответствует ключу в реестре метакласса.
    Это избавляет от необходимости вручную указывать, какой именно класс использовать.
    """

    @staticmethod
    def create_course(course_type: str, **kwargs):
        """
        Создает экземпляр курса заданного типа.

        :param course_type: тип курса (например, "programming", "design", "science")
        :param kwargs: параметры конструктора курса
        :return: объект соответствующего подкласса Course
        :raises ValueError: если указанный тип курса не зарегистрирован
        """
        course_cls = CourseMeta.registry.get(course_type.lower())
        if not course_cls:
            available = list(CourseMeta.registry.keys())
            raise ValueError(
                f"Тип курса '{course_type}' не найден. "
                f"Доступные: {available}"
            )
        return course_cls(**kwargs)
