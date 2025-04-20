from abc import ABC, abstractmethod

class ChangeRequest:
    """
    Представляет запрос на изменение, который должен быть обработан в цепочке обязанностей.

    :param description: Описание изменения, предлагаемого в курсе.
    :param level: Уровень, на котором должно быть принято решение ('instructor', 'methodology', 'management').
    """
    def __init__(self, description: str, level: str):
        self.description = description
        self.level = level


class Handler(ABC):
    """
    Абстрактный обработчик в цепочке обязанностей. Каждый обработчик решает,
    может ли он обработать запрос, и если нет — передает его следующему в цепочке.
    """
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler: 'Handler') -> 'Handler':
        """
        Устанавливает следующий обработчик в цепочке.

        :param handler: Экземпляр обработчика
        :return: Возвращает следующий обработчик для цепочки вызовов
        """
        self._next_handler = handler
        return handler

    def handle(self, request: ChangeRequest):
        """
        Обрабатывает запрос, если текущий обработчик не может — передает дальше по цепочке.

        :param request: Запрос на изменение
        :return: Результат обработки запроса
        """
        if self._next_handler:
            return self._next_handler.handle(request)
        return f"Запрос '{request.description}' не может быть обработан"

    @abstractmethod
    def can_handle(self, request: ChangeRequest) -> bool:
        """
        Метод должен быть реализован в подклассах. Определяет, может ли обработчик взять на себя запрос.
        """
        pass


class InstructorHandler(Handler):
    """
    Обработчик для уровня 'instructor'. Этот обработчик проверяет, может ли преподаватель одобрить запрос на изменение.
    """
    def can_handle(self, request: ChangeRequest) -> bool:
        """
        Проверяет, соответствует ли уровень запроса 'instructor'.

        :param request: Запрос на изменение
        :return: True, если запрос может быть обработан на уровне преподавателя
        """
        return request.level == "instructor"

    def handle(self, request: ChangeRequest):
        """
        Обрабатывает запрос на изменение. Если преподаватель может одобрить запрос, возвращает сообщение,
        иначе передает запрос дальше по цепочке.

        :param request: Запрос на изменение
        :return: Результат обработки запроса
        """
        if self.can_handle(request):
            return f"Преподаватель одобрил: {request.description}"
        return super().handle(request)


class MethodologyDepartmentHandler(Handler):
    """
    Обработчик для уровня 'methodology'. Этот обработчик проверяет, может ли методический отдел одобрить запрос на изменение.
    """
    def can_handle(self, request: ChangeRequest) -> bool:
        """
        Проверяет, соответствует ли уровень запроса 'methodology'.

        :param request: Запрос на изменение
        :return: True, если запрос может быть обработан на уровне методического отдела
        """
        return request.level == "methodology"

    def handle(self, request: ChangeRequest):
        """
        Обрабатывает запрос на изменение. Если методический отдел может одобрить запрос, возвращает сообщение,
        иначе передает запрос дальше по цепочке.

        :param request: Запрос на изменение
        :return: Результат обработки запроса
        """
        if self.can_handle(request):
            return f"Методический отдел одобрил: {request.description}"
        return super().handle(request)


class ManagementHandler(Handler):
    """
    Обработчик для уровня 'management'. Этот обработчик проверяет, может ли руководство одобрить запрос на изменение.
    """
    def can_handle(self, request: ChangeRequest) -> bool:
        """
        Проверяет, соответствует ли уровень запроса 'management'.

        :param request: Запрос на изменение
        :return: True, если запрос может быть обработан на уровне руководства
        """
        return request.level == "management"

    def handle(self, request: ChangeRequest):
        """
        Обрабатывает запрос на изменение. Если руководство может одобрить запрос, возвращает сообщение,
        иначе передает запрос дальше по цепочке.

        :param request: Запрос на изменение
        :return: Результат обработки запроса
        """
        if self.can_handle(request):
            return f"Руководство одобрило: {request.description}"
        return super().handle(request)