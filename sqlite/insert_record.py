import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute("""
	INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL)
	VALUES(?,?,?) 
	""", ('WILL KAWAMOTO', '408-398-2263', 'kawamotowill@gmail.com'))

id = cursor.lastrowid
print(id)

cursor.execute("""
	INSERT INTO PHONEBOOK (NAME, PHONE, EMAIL)
	VALUES(?, ?, ?)
	""", ('YIYEON KIM', '408-680-4242', 'kimyiyun302@gmail.com'))

id = cursor.lastrowid
print(id)

conn.commit()

cursor.close()
conn.close()
