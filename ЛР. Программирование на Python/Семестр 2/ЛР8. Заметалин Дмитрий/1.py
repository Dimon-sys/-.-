import sqlite3

shop = sqlite3.connect('10.db')
cursor = shop.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Hotel (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
address TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Rooms (
               id INTEGER PRIMARY KEY,
               number INTEGER NOT NULL,
               type TEXT NOT NULL
               )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Reservation (
               id INTEGER PRIMARY KEY,
               hotel_id INTEGER NOT NULL,
               room_id INTEGER NOT NULL,
               date TEXT NOT NULL,
               FOREIGN KEY (
                            hotel_id
               )
               REFERENCES Hotel (id),
               FOREIGN KEY (
                            room_id
               )
               REFERENCES Room (id)
               )
''')

shop.close()
