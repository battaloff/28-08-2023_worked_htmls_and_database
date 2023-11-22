import sqlite3

# Подключение к базе данных
conn = sqlite3.connect(r'D:\###TASKS\newproject\politext_tasks\db.sqlite3')
cursor = conn.cursor()

# SQL-запрос для обновления значений
update_query = """
    UPDATE tasks_politext_tabletask
    SET user_id = '1'
    WHERE user_id = 'admin';
"""

# Выполнение запроса
cursor.execute(update_query)

# Подтверждение изменений в базе данных
conn.commit()

# Закрытие соединения
conn.close()
