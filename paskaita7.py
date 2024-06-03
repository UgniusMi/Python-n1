#                       DARBAS SU KATALOGAIS

import os

# current_directory = os.getcwd()
# print("Dabartinis katalogas:", current_directory)

# items = os.listdir(current_directory)
# print("Katalogo turinys:", items)

# os.mkdir("Naujas") pakuria
# os.rmdir("Naujas") pašalina

# os.makedirs("Naujas/Jonas/tomas")
# os.removedirs("Naujas/Jonas/tomas")

# with open("naujas_failas.txt", "w") as file:
#     for skaicius in range(1, 100):
#         file.write(f"{skaicius}. naujas failas, labas\n")

# with open("naujas_failas.txt", "a") as file:
#     for skaicius in range(1, 100):
#         file.write(f"{skaicius}. pridedamas textas\n")

# with open("naujas_failas.txt", "r") as file:
#         print(file.readlines())

# os.rename("naujas_failas.txt", "PVZ_failas.txt")

# os.remove("PVZ_failas.txt")

# items = os.listdir(current_directory)

# for item in items:
#     if os.path.isfile(item):
#         print(f"Failas: {item}")
#     elif os.path.isdir(item):
#         print(f"Aplankas: {item}")

# PVZ


# file = open("masinos.txt")
# read_text = file.read()
# print(read_text)
# file.close()

# with open("zuvu_sarasas.txt","r+") as abc:
#     read_text = abc.read()
#     print(read_text)
#     abc.write("Kolkas tiek")


# 1 uzd.

# Zen_of_Python = """The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!"""


# with open("tekstas2.txt", 'w') as file:
#     file.write(Zen_of_Python)

# from datetime import datetime
# siandienos_data = datetime.today()

# # perskaitom failo turini ir ji atspausdinam

# with open("tekstas2.txt", 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line, end='')

# # pridedam siandienos data

# with open("tekstas2.txt", 'a') as file:
#     file.write(f"\n{siandienos_data}")

# #  Numeruojam eilutes ir keiciam specifine eilute

# with open('Tekstas2.txt', 'r') as file:
#     lines = file.readlines()

# with open('Tekstas2.txt', 'w', encoding="utf-8") as file:
#     for i, line in enumerate(lines, 1):
#         if line.strip() == "Beautiful is better than ugly.":
#             line = "Gražu yra geriau nei bjauru.\n"
#         file.write(f"{i}. {line}")

# #  atbulai

# with open("tekstas2.txt", 'r', encoding="utf-8") as file:
#     lines = file.readlines()
#     tekstas_atbulai = ''.join(lines[::-1])
#     print(tekstas_atbulai)

# #  Skaičiuojame žodžius, skaičius, didžiąsias ir mažąsias raides

# with open('Tekstas2.txt', 'r', encoding="utf-8") as file:
#     text = file.read()

# word_count = len(text.split())
# digit_count = sum(c.isdigit() for c in text)
# upper_case_count = sum(c.isupper() for c in text)
# lower_case_count = sum(c.islower() for c in text)

# print(f"Žodžių kiekis: {word_count}")
# print(f"Skaičių kiekis: {digit_count}")
# print(f"Didžiųjų raidžių kiekis: {upper_case_count}")
# print(f"Mažųjų raidžių kiekis: {lower_case_count}")

# # didziosiom raidem

# with open('Naujas_Tekstas.txt', 'w', encoding="utf-8") as new_file:
#     new_file.write(text.upper())

####################################

# 2 uzdavinys

# # Leisti vartotojui įvesti norimą failo pavadinimą
# file_name = input("Įveskite norimą failo pavadinimą (su .txt priesaga): ")

# # Atidaryti failą rašymo režimu
# with open(file_name, 'w') as file:
#     print("Įveskite tekstą eilutėmis. Norėdami baigti įvestį, palikite eilutę tuščią ir paspauskite ENTER.")
    
#     while True:
#         line = input("Įveskite eilutę: ")
#         if line == "":
#             break
#         file.write(line + '\n')

# print(f"Jūsų tekstas buvo sėkmingai įrašytas į failą {file_name}.")


#  3 uzdavinys

# 3.1

os.mkdir("C:\\Users\\Fatalas\\Desktop\\Naujas Katalogas")

# 3.2
from datetime import datetime
siandienos_data = datetime.today()


with open("C:\\Users\\Fatalas\\Desktop\\Naujas Katalogas\\tekstas.txt", 'w+') as tekstas:
    tekstas.write(f"Siandienos data yra:\n{siandienos_data}\nGeros dieneles!")  #sukuriam teksta viduje
    tekstas.seek(0)              # grystam i pradzia
    print(tekstas.read())        # ir nuskaitom teksta nuo pradziu

# 3.3
sukurimo_data = os.stat("C:\\Users\\Fatalas\\Desktop\\Naujas Katalogas\\tekstas.txt").st_ctime
dydis_baitais = os.stat("C:\\Users\\Fatalas\\Desktop\\Naujas Katalogas\\tekstas.txt").st_size

failo_sukurimo_data = datetime.fromtimestamp(sukurimo_data) # kadangi is st_ctime gauname sekundes del skirtingu datu skaiciavimo, isivedam data(datetime) is POSIX timestampo

print(f"Sukurimo data yra: {failo_sukurimo_data}\nTekstinio failo dydis: {dydis_baitais}")

# 4 uzdavinys