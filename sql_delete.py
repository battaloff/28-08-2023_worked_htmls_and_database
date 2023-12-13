import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('db.sqlite3')

# Выполнение запроса
cur = conn.cursor()
cur.execute('DELETE FROM tasks_politext_tabletask WHERE file_name like ?', ('Thumbs%',))
conn.commit()

# Закрытие соединения с базой данных
conn.close()