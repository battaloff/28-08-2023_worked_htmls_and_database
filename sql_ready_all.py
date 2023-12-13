import sqlite3
from datetime import datetime

# Подключение к базе данных
conn = sqlite3.connect(r'D:\###TASKS\newproject\politext_tasks\db.sqlite3')
cursor = conn.cursor()

# Получение текущей даты и времени
current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

# Обновление строк в таблице
update_query = """
UPDATE tasks_politext_tabletask
SET stage = 'Готов', user_id = '1', ready_date_time = ?
WHERE stage = 'На выводе'
"""

cursor.execute(update_query, (current_datetime,))
conn.commit()

# Закрытие соединения с базой данных
conn.close()
