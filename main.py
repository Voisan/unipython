from core.logger import logger
from core.platform import Address, Platform
from core.factory import CourseFactory
from core.handlers import ChangeRequest, InstructorHandler, MethodologyDepartmentHandler, ManagementHandler
from core.programming import ProgrammingCourse
from core.design import DesignCourse
from core.science import ScienceCourse
from core.database import init_db, insert_course, fetch_all
# Создание платформы
address = Address("Россия", "Москва", "Пушкина", "1","sdamnamaximum.ru")
platform = Platform(address)
logger.info("Платформа создана с адресом: %s", address)

# Создание курсов через фабрику
logger.info("Создание курсов через фабрику...")
course1 = CourseFactory.create_course(
    course_type="programming",
    title="Python 101",
    start_date="2025-04-01",
    end_date="2025-06-01",
    instructor="Муллошараф Курбонович",
    students=["Иван", "Мария"],
    topics=["Основы", "ООП", "Функции"],
    languages=["Python"]
)

course2 = CourseFactory.create_course(
    course_type="design",
    title="Графический дизайн для начинающих",
    start_date="2025-05-01",
    end_date="2025-07-01",
    instructor="Сергей",
    students=["Елена", "Олег"],
    topics=["Цвет", "Композиция"],
    tools=["React", "Figma"]
)

course3 = CourseFactory.create_course(
    course_type="science",
    title="Физика для начинающих",
    start_date="2025-03-01",
    end_date="2025-06-01",
    instructor="Марина",
    students=["Никита", "Светлана", "Антон"],
    topics=["Кинематика", "Динамика", "МКТ"],
    field=["Физика"]
)

# Установка пользователя
logger.info("Установка текущего пользователя: %s как %s", "Муллошараф Курбонович", "instructor")
course1.set_current_user("Муллошараф Курбонович", "instructor")

# Добавление курсов на платформу
logger.info("Курс добавлен на платформу: %s", course1.title)
platform.add_course(course1)

logger.info("Курс добавлен на платформу: %s", course2.title)
platform.add_course(course2)

logger.info("Курс добавлен на платформу: %s", course3.title)
platform.add_course(course3)


# Логирование и уведомление
for course in platform.get_courses():
    course.log_action("Курс стартовал!")
    course.notify_students("Начинаем изучать материал, время пролетит незаметно :)")

# Работа с оценками (с проверкой прав)
logger.info("Обновление оценки: Иван -> 90")
course1.update_score("Иван", 90)

logger.info("Обновление оценки: Мария -> 85")
course1.update_score("Мария", 85)

# Получение всех курсов и топ-N
logger.info("Получение списка всех курсов на платформе.")
print("Все курсы на платформе:")
for course in platform.get_courses():
    print(course)

logger.info("Получение топ-2 курсов по числу студентов.")
print("\nТоп-2 курса по числу студентов:")
for course in platform.get_top_courses(2):
    print(course)

# Удаление курса
logger.info("Удаление курса с платформы: %s", "Графический дизайн для начинающих")
platform.remove_course("Графический дизайн для начинающих")

# Обработка изменения программы курса через цепочку обязанностей
logger.info("Создание цепочки обязанностей")
instructor = InstructorHandler()
methodology = MethodologyDepartmentHandler()
management = ManagementHandler()

instructor.set_next(methodology).set_next(management)

request = ChangeRequest("Изменить структуру модуля ООП", "methodology")
logger.info("Обработка запроса на изменение: %s для %s", request.description, request.level)
result = instructor.handle(request)
logger.info("Результат обработки запроса: %s", result)
print("\nРезультат обработки запроса на изменение:", result)

conn = init_db()
data = course1.to_dict()
insert_course(conn, 'programming_course', **data)
data = course2.to_dict()
insert_course(conn, 'design_course', **data)
data = course3.to_dict()
insert_course(conn, 'science_course', **data)