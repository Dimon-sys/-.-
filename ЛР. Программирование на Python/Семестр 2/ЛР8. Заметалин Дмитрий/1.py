from sqlite3 import *

base = connect('1.db')
cursor = base.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS events (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
title TEXT NOT NULL,
date TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS participants (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS registration (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
event_id INTEGER,
participant_id INTEGER,
FOREIGN KEY (event_id) REFERENCES events(id),
FOREIGN KEY (participant_id) REFERENCES participants(id)
)
''')

result_one = cursor.execute(
"""
SELECT title, date FROM events
"""
).fetchall()
for elem in result_one:
    print(elem)


event_id = 1
cursor.execute(
"""
SELECT p.id, p.name FROM participants p
INNER JOIN registration r ON p.id = r.participant_id WHERE r.event_id = ?
""", (event_id,))
result_two = cursor.fetchall()
for elem in result_two:
    print(elem)


cursor.execute(
"""
SELECT e.id, e.title, COUNT(r.participant_id) AS participant_count
FROM events e
LEFT JOIN registration r ON e.id = r.event_id
GROUP BY e.id, e.title
ORDER BY e.id;
""")
result_three = cursor.fetchall()
print("ID события | Название события                  | Количество участников")
print("-" * 60)
for event_id, title, count in result_three:
    print(f"{event_id:<10} | {title:<33} | {count}")

base.commit()
base.close()