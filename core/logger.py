import logging

logger = logging.getLogger("edu_platform")
"""
logger: Объект логгера, используемый для записи логов.
"""
logger.setLevel(logging.INFO)
"""
setLevel(logging.INFO): Устанавливает минимальный уровень логирования.
INFO означает, что будут записываться сообщения с уровня INFO и выше (например, WARNING, ERROR, CRITICAL).
"""

for handler in logger.handlers[:]:
    logger.removeHandler(handler)
"""
Удаляет все предыдущие обработчики логирования, чтобы избежать дублирования сообщений в файле или консоли.
"""

file_handler = logging.FileHandler("logfile.log", encoding="utf-8")
"""
file_handler: Обработчик, который будет записывать логи в файл "logfile.log".
Файл будет создан в текущей директории, если он еще не существует.
encoding="utf-8" указывает на использование кодировки UTF-8 для записи в файл.
"""

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
"""
formatter: Форматтер, который определяет формат записи в лог.
%(asctime)s — временная метка сообщения.
%(levelname)s — уровень логирования (например, INFO, ERROR).
%(message)s — текст самого сообщения.
"""
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
"""
addHandler(file_handler): Добавляет обработчик к логгеру. 
Теперь логи будут записываться в файл "logfile.log" с указанным форматом.
"""
