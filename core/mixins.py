from core.logger import logger

class LoggingMixin:
    """
    Миксин для логирования действий, связанных с курсом.
    Этот класс добавляет возможность логировать действия курса, такие как начало курса или другие события.
    """

    def log_action(self, action: str):
        """
        Логирует действие курса, например, 'Курс стартовал', и выводит его в консоль.
        :param action: Описание действия (строка).
        """
        message = f"Курс [{self.title}]: {action}"
        logger.info(message)
        print(message)


class NotificationMixin:
    """
    Миксин для отправки уведомлений студентам.
    Этот класс добавляет возможность уведомлять студентов о событиях в курсе.

    """
    def notify_students(self, message: str):
        """
        Отправляет уведомление всем студентам, включенным в курс.
        :param message: Сообщение для уведомления (строка).
        """
        for student in self.students:
            full_message = f"Уведомление для {student}: {message}"
            logger.info(full_message)
            print(full_message)
