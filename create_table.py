import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute ('CREATE TABLE students (name TEXT, address TEXT ,age TEXT)')
print("Executed Sccessfully")

conn.close()