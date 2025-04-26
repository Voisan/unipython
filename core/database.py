import sqlite3
import json


# файл базы данных
DB_FILE = 'courses.db'

# создание базы данных и создание таблиц для каждого типа курса
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    # таблица для курсов программирования
    c.execute('''
        CREATE TABLE IF NOT EXISTS programming_course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            start_date TEXT,
            end_date TEXT,
            instructor TEXT,
            students TEXT,    
            topics TEXT,      
            languages TEXT    
        )
    ''')
    # таблица для курсов дизайна
    c.execute('''
        CREATE TABLE IF NOT EXISTS design_course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            start_date TEXT,
            end_date TEXT,
            instructor TEXT,
            students TEXT,   
            topics TEXT,      
            tools TEXT        
        )
    ''')
    # таблица для научных курсов
    c.execute('''
        CREATE TABLE IF NOT EXISTS science_course (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            start_date TEXT,
            end_date TEXT,
            instructor TEXT,
            students TEXT,    
            topics TEXT,      
            field TEXT        
        )
    ''')
    conn.commit()
    return conn

#функция для вставки записи о курсе
def insert_course(conn, table, **kwargs):
    c = conn.cursor()
    if 'course_type' in kwargs:
        kwargs.pop('course_type')
    fields = ', '.join(kwargs.keys())
    placeholders = ', '.join('?' for _ in kwargs)
    values = []
    for v in kwargs.values():
        if isinstance(v, (list, dict)):
            values.append(json.dumps(v, ensure_ascii=False))
        else:
            values.append(v)
    c.execute(f"INSERT INTO {table} ({fields}) VALUES ({placeholders})", values)
    conn.commit()
    return c.lastrowid  # ID вставленной записи

#  функция для получения всех записей из таблицы
def fetch_all(conn, table):
    c = conn.cursor()
    c.execute(f"SELECT * FROM {table}")
    cols = [col[0] for col in c.description]
    rows = c.fetchall()
    results = []
    for row in rows:
        record = dict(zip(cols, row))
        # преобразуем строки JSON обратно в Python-объекты
        for key, val in record.items():
            if key in ('students', 'topics', 'languages', 'tools', 'field') and val is not None:
                try:
                    record[key] = json.loads(val)
                except json.JSONDecodeError:
                    pass
        results.append(record)
    return results  # Возвращаем список всех записей
