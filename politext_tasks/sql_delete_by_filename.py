import sqlite3

# Подключение к базе данных
conn = sqlite3.connect(r'D:\###TASKS\newproject\politext_tasks\db.sqlite3')
cursor = conn.cursor()

# Значение, которое вы хотите использовать в качестве условия
file_name_to_delete = '775-635_16_ISHONCH_2980 - SAKATA KATALOG.pdf'

# Удаление строк из таблицы
delete_query = """
DELETE FROM tasks_politext_tabletask
WHERE file_name = ?
"""

cursor.execute(delete_query, (file_name_to_delete,))
conn.commit()

# Закрытие соединения с базой данных
conn.close()