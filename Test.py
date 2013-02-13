import sqlite3

conn = sqlite3.connect("Engines.db")
cursor = conn.cursor()

for row in cursor.execute("Select * FROM Engine"):
	print row
