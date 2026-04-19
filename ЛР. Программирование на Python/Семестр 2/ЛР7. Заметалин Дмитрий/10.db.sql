BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "departments" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL UNIQUE,
	"floor"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "merch" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"measure"	INTEGER NOT NULL,
	"measure_type"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "sellers" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT NOT NULL,
	"age"	INTEGER NOT NULL,
	"gender"	TEXT NOT NULL,
	"department_id"	INTEGER NOT NULL,
	FOREIGN KEY("department_id") REFERENCES "departments"("id"),
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "sales" (
	"merch_id"	INTEGER NOT NULL,
	"seller_id"	INTEGER NOT NULL,
	"amount"	REAL NOT NULL,
	"date"	TEXT NOT NULL,
	FOREIGN KEY("merch_id") REFERENCES "merch"("id"),
	FOREIGN KEY("seller_id") REFERENCES "sellers"("id")
);
INSERT INTO "departments" VALUES (1,'Молочные продукты',1);
INSERT INTO "departments" VALUES (2,'Хлебобулочные изделия',1);
INSERT INTO "departments" VALUES (3,'Сыры и масло',2);
INSERT INTO "departments" VALUES (4,'Фрукты и чай',2);
INSERT INTO "merch" VALUES (1,'Молоко «Веселая буренка»',89,'литр');
INSERT INTO "merch" VALUES (2,'Хлеб «Дарницкий»',42,'штука');
INSERT INTO "merch" VALUES (3,'Сыр «Российский» 50%',650,'кг');
INSERT INTO "merch" VALUES (4,'Яблоки «Голден»',120,'кг');
INSERT INTO "merch" VALUES (5,'Чай «Лисма» черный',180,'пачка (100 г)');
INSERT INTO "merch" VALUES (6,'Сахар песок',78,'кг');
INSERT INTO "merch" VALUES (7,'Масло сливочное «Крестьянское»',320,'кг');
INSERT INTO "merch" VALUES (8,'Печенье «Юбилейное»',95,'кг');
INSERT INTO "sellers" VALUES (1,'Иванова Анна Петровна',28,'Ж',1);
INSERT INTO "sellers" VALUES (2,'Смирнов Олег Иванович',35,'М',1);
INSERT INTO "sellers" VALUES (3,'Петрова Мария Сергеевна',42,'Ж',2);
INSERT INTO "sellers" VALUES (4,'Кузнецов Дмитрий Алексеевич',31,'М',3);
INSERT INTO "sellers" VALUES (5,'Васильева Елена Владимировна',26,'Ж',3);
INSERT INTO "sellers" VALUES (6,'Попов Андрей Николаевич',47,'М',4);
INSERT INTO "sellers" VALUES (7,'Соколова Татьяна Юрьевна',33,'Ж',2);
INSERT INTO "sellers" VALUES (8,'Михайлов Алексей Дмитриевич',29,'М',4);
INSERT INTO "sales" VALUES (1,1,5.0,'2025-03-01');
INSERT INTO "sales" VALUES (1,2,3.0,'2025-03-02');
INSERT INTO "sales" VALUES (2,3,10.0,'2025-03-01');
INSERT INTO "sales" VALUES (2,7,7.0,'2025-03-03');
INSERT INTO "sales" VALUES (3,4,2.0,'2025-03-01');
INSERT INTO "sales" VALUES (3,5,1.5,'2025-03-02');
INSERT INTO "sales" VALUES (4,8,8.0,'2025-03-01');
INSERT INTO "sales" VALUES (4,6,5.0,'2025-03-03');
INSERT INTO "sales" VALUES (5,6,4.0,'2025-03-02');
INSERT INTO "sales" VALUES (5,8,6.0,'2025-03-03');
INSERT INTO "sales" VALUES (6,1,12.0,'2025-03-01');
INSERT INTO "sales" VALUES (6,2,9.0,'2025-03-03');
INSERT INTO "sales" VALUES (7,4,2.5,'2025-03-02');
INSERT INTO "sales" VALUES (7,5,3.0,'2025-03-03');
INSERT INTO "sales" VALUES (8,3,15.0,'2025-03-02');
COMMIT;
