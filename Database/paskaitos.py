import sqlite3

conn = sqlite3.connect("Database\\univeras.db")
c = conn.cursor()

#SUKURIAM LENTELE

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS
    paskaita (  
    PAVADINIMAS text,
    DESTYTOJAS text,
    TRUKME INTEGER
    )""")


#Paskaitu pridejimas

with conn:
    c.execute("INSERT INTO paskaita VALUES ('Vadyba', 'Domantas', 40)")
    c.execute("INSERT INTO paskaita VALUES ('Python', 'Donatas', 80)")
    c.execute("INSERT INTO paskaita VALUES ('Java', 'Tomas', 80)")

# Tukme ilgesne nei 50

with conn:
    c.execute("SELECT * FROM paskaita WHERE TRUKME > 50")
    paskaitos = c.fetchall()

    print(f"\nPaskaitos kurios vyksta ilgiau nei 50min: {paskaitos}")
    

# pakeiciau paskaitos pavadinima 

with conn:
    c.execute("UPDATE paskaita SET PAVADINIMAS = 'Python programavimas' WHERE PAVADINIMAS = 'Python'")

# trinam toma

with conn:
    c.execute ("DELETE FROM paskaita WHERE DESTYTOJAS = 'Tomas'")
    c.execute("SELECT * FROM paskaita")
    print(c.fetchall())

#spausdinam
with conn:
    c.execute("SELECT * FROM paskaita")
    result = c.fetchall()
    for paskaita in result:
        print(paskaita)


#dadesim is githubo
#dar damesim
