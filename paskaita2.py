import numpy
print("hello")

#namu darbai

#organization_Name = "Microsoft"

#est_year = 1985



#print('-'*45)

#print(f'|\tOrg_Name\t|\test_Year    |')

#print('-'*45)

#print(f'|\t{organization_Name}\t|\t{est_year}\t    |')

#print('-'*45)

#print(f'|\t{organization_Name}\t|\t{est_year}\t    |')

#print('-'*45)

#amzius = 51



# if amzius > 20:

#     print("Tu vyresnis nei 20")

#     if amzius > 80:

#         print("Tu esi ne tik vyresnis nei 20, tu esi senas")

#         if amzius >= 100:

#             print("tu ne tik senas bet ir rekoridininkas")

#         print('Taip pamirsau pamineti tu esi senjoras')

#     print("Tu galimai nesi toks senas")

# if amzius > 18 and amzius <= 20:

#     print('Tu gali pirkti gerimus')

# elif amzius > 20 and amzius < 45:

#     print('Tu gali nusipirkti alkoholio')

# elif amzius > 45:

#     print("Tu gali buti prezidentas")

# else:

#     print("Tu dar per jaunas")

#pirmas uzdavinys

#a = int(input("Jusu pirmas skaicius "))
#b = int(input("Jusu antras skaicius "))
#if a < b:
    #print("a mazesnis uz b")
#elif a == b:
   # print("a lygu b")
#else:
    #print("a didesnis uz b")

# antras uzdavinys

#zodis = "Zen of Python"
#print(zodis[5])
#print(zodis[-6])
#print(zodis.split()[0])
#print(zodis.split()[2])
#print(zodis[::-1])
#print(zodis.split())
#print(zodis.replace('Python', 'Programming'))

#print(zodis.upper())

# zodis = "Zen of Python"



# atskirti_zodziai = zodis.split()


# print(atskirti_zodziai[1][-1])

#trecias uzdavinys

#skaicius1 = int(input("Iveskite pirma skaiciu "))
#skaicius2 = int(input("Iveskite antra skaiciu "))
#print("koki veiksma norite atlikti: ")
#print("1. sudetis")
#print("2. atimtis")
#print("3. daugyba")
#Veiksmas = input("Iveskite pasirinkto veiksmo numeri: ")

#if Veiksmas=='1':
  #  print("Jusu pasirinktu skaiciu sudetis yra ", skaicius1+skaicius2)
#if Veiksmas=='2':
  #  print("Jusu pasirinktu skaiciu atimtis yra ", skaicius1-skaicius2)
#if Veiksmas=='3':
   # print("Jusu pasirinktu skaiciu sandauga yra ", skaicius1-skaicius2)

#skaiciai = [9,8,7,4]
#print(skaiciai[-1])

# suma = 0
 
# for skaicius in skaiciai:
#     suma += skaicius
#     print("Dabartine suma: ", suma)
# print("Galutinis vidurkis",suma/len(skaiciai))
 
# for raktas, reiksme in kompanijos.items():
#     print(f"{raktas} darbuotojai yra: {reiksme}")
 
# for skaicius in range(50):
#     print(skaicius)
 
# limitas = 100
# i = 1
# while i < limitas:
#     print(i)
#     i +=1
 
# Input 15....
 
# for skaicius in range(10):
#     print("Pirmas spausdinimas", skaicius)
#     if(skaicius >= 3):
#         continue
#     print(skaicius)
 
 
# for skaicius in range(10):
#     print(skaicius)
# else:
#     print("Pabaiga")

#import random
#random_integer = random.randint(1,50)
#print(random_integer)


# amzius = int("20")

# amzius = int(input("Iveskite savo amziu "))







# if (amzius < 21):

#     print("POLICIJA")

# elif amzius > 18:

#     print("Gali nusipirkti energetini")

# else:

#     print("Ifas nesuveike")

#     print("Labai nesuveike")



# if(amzius > 20):

#     print("Gali nusipirkti alkoholio")



# if(amzius > 65):

#     print("Tu esi senjoras")





# pinigai = 20



# if pinigai >= 500 and pinigai < 1500:

#     print("Dar pinigu pakanka")

# elif pinigai > 1500 and pinigai < 5000:

#     print("Turi daug pinigu")

# elif pinigai > 5000:

#     print("Tu esi turtingas")

# else:

#     print("Tu esi vargsas")


#ciklai 

# kiekis_vid = 0

# while kiekis < 10:

#     print("Isorinio ciklo kiekis: ", kiekis)

#     while kiekis_vid < 5:

#         print(f"Vidinio ciklo kiekis: {kiekis_vid}")

#         kiekis_vid += 1

#     kiekis = kiekis + 1

#     kiekis_vid = 0

#---------------- su break

# kiekis_vid = 0

# while kiekis < 10:

#     print("Isorinio ciklo kiekis: ", kiekis)

#     while kiekis_vid < 5:

#         print(f"Vidinio ciklo kiekis: {kiekis_vid}")

#         kiekis_vid += 1

#         if kiekis_vid == 3:

#             break

#     kiekis = kiekis + 1

#     kiekis_vid = 0

# 1 sarasai ir zodynai

# sarasas = [4,9,55]
# print(sarasas)
# sarasas.append(33)
# print(sarasas[-1])
# sarasas.pop(1)
# print(sarasas)
# sarasas[0] = 88
# print(sarasas)

# krepsinio_komandos = {"Lietuvos": ["Lietuvs rytas", "Zalgiris", "Lietkabelis"], "NBA": ["Bulls", "Lakers", "Spurs"] }
# print(krepsinio_komandos["Lietuvos"])
# krepsinio_komandos["LKL komandos"] = "Neptunas", "Siauliai" 
# print(krepsinio_komandos)
# del krepsinio_komandos["NBA"]
# print(krepsinio_komandos)
# krepsinio_komandos["Lietuvos"] = "Zalgiris", "Lietkabelis"
# print(krepsinio_komandos)
 
 

# my_tuple = (1, 2, 3) - kaip sarasai tik greiciau sukasi bet neina nieko keisti

# print(my_tuple[0])


# user = "Johnny"
# privileged_users = ["Tom", "Albert", "Stephen"]
# if user in privileged_users:
#     print(f"Welcome home {user}")else:
#     print("INTRUDER ALLERT. Silently calling police...")

#zodyno raktu priskyrimas reiksmei

# test_keys = ["Albert", "Tom", "Stephen"]
# test_values = [1, 4, 5]
# my_dictionary= dict(zip(test_keys, test_values))
# print(my_dictionary)

#  vieno  zodyno atnaujinimas, jei kazkas sutampa(b)  -pakeiciama 
# dict_one = {'a': 10, 'b': 20, 'c': 30}
# dict_two = {'b': 200, 'd': 400}
# dict_one .update(dict_two )
# print(dict_one )

# kiekis = 0

# whilie 
# Skaicius = int(input("Iveskite norima skaiciu "))


skaicius = int(input("Iveskite norima skaiciu: "))

if skaicius > 0:
    print(True)


#destytojo
# skaicius = int(input("Iveskite skaiciu "))

# ar_skaicius_teigiamas = bool() # NEBUTINAS
# if skaicius > 0:
#     ar_skaicius_teigiamas = True
# else:
#     ar_skaicius_teigiamas = False
# print(ar_skaicius_teigiamas)