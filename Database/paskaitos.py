import sqlite3

conn = sqlite3.connect("Database\\univeras.db")
c = conn.cursor()

#SUKURIAM LENTELE

with conn:
    c.execute("""CREATE TABLE IF NOT EXISTS
    paskaita (  
    ID integer PRIMARY KEY AUTOINCREMENT,
    PAVADINIMAS text,
    DESTYTOJAS text,
    TRUKME INTEGER
    )""")

    c.execute("DELETE FROM paskaita") #kiekviena karta paleidziant issitrinam (jeigu norim)

#Paskaitu pridejimas

with conn:
    c.execute("INSERT INTO paskaita (PAVADINIMAS, DESTYTOJAS, TRUKME) VALUES ('Vadyba', 'Domantas', 40)") #JEI NAUDOJAM ID PRIMARY KEY, IKELDAMI NAUJA IRASA NURODOM KOKIU VALUES TIKIMES
    c.execute("INSERT INTO paskaita (PAVADINIMAS, DESTYTOJAS, TRUKME) VALUES ('Python', 'Donatas', 80)")
    c.execute("INSERT INTO paskaita (PAVADINIMAS, DESTYTOJAS, TRUKME) VALUES ('Java', 'Tomas', 80)")

# Tukme ilgesne nei 50

with conn:
    c.execute("SELECT * FROM paskaita WHERE TRUKME > 50")
    paskaitos = c.fetchall()

    print(f"\nPaskaitos kurios vyksta ilgiau nei 50min: {paskaitos}")
    

# # pakeiciau paskaitos pavadinima 

with conn:
    c.execute("UPDATE paskaita SET PAVADINIMAS = 'Python programavimas' WHERE PAVADINIMAS = 'Python'")
    
# # trinam toma

with conn:
    c.execute ("DELETE FROM paskaita WHERE DESTYTOJAS = 'Tomas'")
    c.execute("SELECT * FROM paskaita")
    tomless = c.fetchall()
    for paskait in tomless:
        print(f"\nLike paskaitos pasalinus Toma: {paskait}")

# #spausdinam
with conn:
    c.execute("SELECT * FROM paskaita")
    result = c.fetchall()
    for paskaita in result:
        print(paskaita)


#dadesim is githubo
#dar damesim
