from functools import wraps

class InvalidDateError(Exception):
    """
    Исключение, вызываемое при попытке создать курс, у которого
    дата окончания раньше даты начала.
    """
    pass

class PermissionDeniedError(Exception):
    """
    Исключение, вызываемое при попытке выполнить действие без необходимых прав доступа.
    """
    pass

class CourseNotFoundError(Exception):
    """
    Исключение, вызываемое, если указанный курс не найден на платформе.
    """
    pass

def check_permissions(required_role):
    """
    Декоратор для проверки прав пользователя перед выполнением метода.

    Применяется к методам, которые должны выполняться только пользователями с определенной ролью.
    Например, только преподаватель может выставлять оценки.

    :param required_role: роль, необходимая для выполнения метода (например, "instructor")
    :return: обёрнутый метод с проверкой прав
    """
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            user = getattr(self, "current_user", None)
            if not user or user.get("role") != required_role:
                raise PermissionDeniedError(f"Доступ запрещен. Требуется роль: {required_role}")
            return func(self, *args, **kwargs)
        return wrapper
    return decorator
