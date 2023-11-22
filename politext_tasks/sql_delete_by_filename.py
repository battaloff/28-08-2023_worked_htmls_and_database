import sqlite3

# Подключение к базе данных
conn = sqlite3.connect(r'D:\###TASKS\newproject\politext_tasks\db.sqlite3')
cursor = conn.cursor()

# Удаление строк из таблицы
delete_query = """
DELETE FROM tasks_politext_tabletask
WHERE file_name = '1030-790_4_DAVR P_P+Z_ALMAZ-ISNUR_960x600_4+0_5000+100tir.pdf'
"""

cursor.execute(delete_query)
conn.commit()

# Закрытие соединения с базой данных
conn.close()