import sqlite3

conn = sqlite3.connect("Ugniaus_library\\data\\library_data.db")
c = conn.cursor()

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS "User" (
	"id" INTEGER,
	"name" TEXT NOT NULL,
	"surname" TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
    )""")


with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS "Book" (
	"id"	INTEGER,
	"title"	TEXT NOT NULL,
	"author"	TEXT NOT NULL,
	"year"	INTEGER NOT NULL,
	"genre"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)""")


with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS "Borrow_book" (
	"id"	INTEGER,
	"borrow_date"	DATE NOT NULL DEFAULT (date('now')),
	"return_date"	DATE,
	"due_date"	DATE NOT NULL,
	"user_id"	INTEGER NOT NULL,
	"book_id"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("book_id") REFERENCES "Book"("id"),
	FOREIGN KEY("user_id") REFERENCES "User"("id")
)""")