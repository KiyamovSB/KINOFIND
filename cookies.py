import sqlite3

sqlite_connection = sqlite3.connect('Cookies')
cursor = sqlite_connection.cursor()
print("База данных создана и успешно подключена к SQLite")

sqlite_select_query = "select sqlite_version();"
cursor.execute(sqlite_select_query)
record = cursor.fetchall()
print("Версия базы данных SQLite: ", record)

sqlite_select_query = """SELECT name FROM sqlite_schema"""
cursor.execute(sqlite_select_query)
total_rows = cursor.fetchall()
print("Всего строк:  ", total_rows)

sqlite_select_query = """PRAGMA table_info(cookies)"""
cursor.execute(sqlite_select_query)
total_rows = cursor.fetchall()
print("Всего строк:  ", total_rows)

sqlite_select_query = """select substr(encrypted_value,2,length(encrypted_value)-2) from cookies where host_key = '.kinopoisk.ru'"""
cursor.execute(sqlite_select_query)
total_rows = cursor.fetchall()
for el in total_rows:
    print("Всего строк:  ", (el))
    # decode('latin1').decode(utf)

cursor.close()



