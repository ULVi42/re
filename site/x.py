import sqlite3

connection = sqlite3.connect("database.db")  # Adjust the path if necessary
cursor = connection.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(tables)  # Should show the list of tables in the database
connection.close()
