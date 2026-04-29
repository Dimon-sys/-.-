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

events = [
    ('День рождения сосиски', '13.11.1805'),
    ('Национальный день похмелья', '01.01.2067'),
    ('День домового', '10.02.6666'),
    ('День пельменей','18.02.0123'),
    ('День профессионального алкоголика','20.02.0000')
]
cursor.executemany('''
INSERT INTO events (title, date) VALUES (?, ?)
''', events)


cursor.execute('''
CREATE TABLE IF NOT EXISTS participants (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
name TEXT NOT NULL
)
''')

participants = [
    ('Иван Иванов',),
    ('Данил Колбасенко',),
    ('Угадай Кто',),
    ('Хороший Человек',),
    ('Тохрипо Товизго',),
    ('Томимо Токосо',),
    ('Тояма Токанава',),
    ('Никита Макаров',),
    ('Билл ДеБилл',),
    ('Дмитрий Пучков',)
]
cursor.executemany("INSERT INTO participants (name) VALUES (?)", participants)

cursor.execute('''
CREATE TABLE IF NOT EXISTS registration (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
event_id INTEGER,
participant_id INTEGER,
FOREIGN KEY (event_id) REFERENCES events(id),
FOREIGN KEY (participant_id) REFERENCES participants(id)
)
''')


registration = [
    (1, 5),
    (1, 6),
    (1, 8),
    (1, 7),
    (2, 4),
    (1, 1),
    (3, 2),
    (3, 9),
    (4, 8),
    (5, 10),
    (5, 3),
    (5, 5),
]
cursor.executemany('''
INSERT INTO registration (event_id, participant_id) VALUES (?, ?)
''', registration)


print('Задание 1\n---------------')
result_one = cursor.execute(
"""
SELECT title, date FROM events
"""
).fetchall()
for elem in result_one:
    print(elem)
print('---------------')


print('Задание 2\n---------------')
event_id = 1
cursor.execute(
"""
SELECT participants.id, participants.name FROM participants INNER JOIN registration ON participants.id = registration.participant_id WHERE registration.event_id = ?
""", (event_id,))
result_two = cursor.fetchall()
for elem in result_two:
    print(elem)
print('---------------')


print('Задание 3\n---------------')
event_id = 1
cursor.execute(
"""
SELECT events.id, events.title, COUNT(registration.participant_id)
FROM events
LEFT JOIN registration ON events.id = registration.event_id
GROUP BY events.id, events.title
ORDER BY events.id;
""")
result_three = cursor.fetchall()
print("ID события | Название события                  | Количество участников")
print("-" * 60)
for event_id, title, count in result_three:
    print(f"{event_id:<10} | {title:<33} | {count}")
print('---------------')


base.commit()
base.close()