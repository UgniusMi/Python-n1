# def atspausdink(vardas):
#     print("-+-+-+-+-+-+-///////////////+-+-+-+-+-+-+")
#     print()
#     print(vardas)
#     print()
#     print("-+-+-+-+-+-+-//////////////+-+-+-+-+-+-+")


# atspausdink("      *********$Ramuniukas$*********")
# atspausdink("      *********$Vygantas$*********")

# def kvadrato_plotas(krastine1, krastine2):
#     Plotas = krastine1 * krastine2
#     print("###############################\n")
#     print()
#     print(Plotas)
#     print()
#     print("\n###############################")
#     #print("\U0001F643\U0001F643\U0001F643\U0001F643\U0001F643\U0001F643\U0001F643\U0001F643\U0001F643")
#     # print(" \U0001F47D \U0001F600")

# kvadrato_plotas(7, 9)
# kvadrato_plotas(9,9)

# 2 UZDAVINYS

# def kvadrato_plotas(krastine1, krastine2):
#     Plotas = krastine1 * krastine2

#     if Plotas > 10:
#         print("###############################\n")
#         print()
#         print(f"Jusu krastiniu plotas yra: {Plotas}")
#         print()
#         print("\n###############################")
#         return Plotas
#     else:
#         print("Plotas yra per mazas, kad apskaiciuotume turi. Pasirinkite ilgesnes krastines.")
#         return #0    #cia naudojant 0 naudojam ziamiau esancias eilutes 47 & 48

# kv_plotas = kvadrato_plotas(4, 1)
# if kv_plotas:
#     Turis = kv_plotas * 3
#     print(f"\n\nJusu kvadrato Turis yra: {Turis}\n\n\n###############################")

    
# #Turis = kvadrato_plotas(4, 1) * 3    
# #print(Turis)

#------paprastesnis

# def teksto_ilgis(tekstas):
#     return len(tekstas)
# Vardas = input('Iveskite norima varda: ')

# vardo_ilgis = teksto_ilgis(Vardas)
# print(f"\nJusu vardo ilgis yra: {vardo_ilgis} raidziu.\n")

# bandau kitaip__________


# def daugyba(skaicius1, skaicius2):
#     sandauga = skaicius1*skaicius2
#     if sandauga % 2 == 0:
#         return "sudauginus jusu skaicius atsakymas yra: lyginis"
#     else:
#         return "sudauginus jusu skaicius atsakymas yra: nelyginis arba lygus nuliui"                #pasiziuret kas blogai

# skaiciai = input("Iveskite norimus skaicius: ")
# rezultatas = daugyba(4, 3)
# print(rezultatas)





# _______________________ 3 uzdavinys



# def skaiciai(sk1, sk2, sk3=1, sk4=2, sk5=3):
#     daugyba = sk1*sk2*sk3*sk4*sk5
#     return daugyba

# rezultatas = skaiciai(1, 3, 1 )
# print(rezultatas)

# 2 dalis: nebaigtas

# def vardai(vd1 = "bevardis",vd2 = "bevardis", vd3 = "bevardis",vd4 = "bevardis",vd5 = "bevardis"):  ##cia bevardis kaip ir nieko nereiskia
#            visi_vardai = (f"{vd1} {vd2} {vd3} {vd4} {vd5} ")
#            return visi_vardai

# # vd1 = input('Iveskite norima varda: ')
# # if vd1 == '':
# #         vd1 = "bevardis"
# # vd2 = input('Iveskite norima varda: ')                    
# # vd3 = input('Iveskite norima varda: ')                         #jei naudojam sita
# # vd4 = input('Iveskite norima varda: ')
# # vd5 = input('Iveskite norima varda: ')
# # spausdinam = vardai(vd1, vd2, vd3, vd4, vd5)
# # print(spausdinam)

# vardu_listas = input("Iveskite 5 vardu ir po kiek vieno padekite zenkla ,: ")
# vardai2 = vardu_listas.split(',')
# spausdinam = vardai2()
# print(spausdinam)

# 3dalis



# # Uzdavinys su args ir kwargs

# def dalyba_is2(*args):
#     for skaiciai in args:
#         print(f"Padalinus is 2=  {skaiciai / 2}")

# dalyba_is2(42,684,65,100,200)

# __________

# def spausdinam_zodyna(**kwargs):
#     for raktas, reiksme in kwargs.items():
#         print(raktas,reiksme)

# spausdinam_zodyna(Vardas =":Jonas", Pavarde=":Petraitis", Amzius=":18")


# lanmda

# tu_paciu_skaiciu_suma = lambda skaicius : skaicius+skaicius

# print(tu_paciu_skaiciu_suma(5))

# ----------------

# skaiciai = [5,9,8,4,6,3]
# skaiciai2 = map(lambda a: a+a, skaiciai)

# for suma in skaiciai2:
#     print(f"Tu paciu skaiciu suma yra lygi: {suma}")

# ----------------------------------------------------------------------------------------


## 1 Uzdavinys:
## 1

# def skaiciai(skaicius1, skaicius2, skaicius3):
#     suma = skaicius1+skaicius2+skaicius3
#     return suma

# rezultatas = skaiciai(4, 8, 6)
# print(rezultatas)

# #2

# def saraso_suma(sarasas):
#     suma = 0
#     for skaicius in sarasas:
#         suma += skaicius
#     return suma
# skaiciai = [5, 2, 2, 4, 8]
# print(saraso_suma(skaiciai))

# #3

# def didziausias_skaicius(*skaiciai):
#     if not skaiciai:
#         print("nepateikta jokiu skaiciu")
#         return
#     didziausias = max(skaiciai)
#     print("Didziausias is pateiktu skaiciu yra: ", didziausias)

# didziausias_skaicius(8,5,6,999,58)

# #4

# def zodis("Lakunas")            #  padaryt su def
# print(zodis[::-1])

# 5

# sakinys = "Lakunas skrido per Europa 1999 metais"

# zodziai = len(sakinys.split())

# 6



# 7

# def ar_pirminis(skaicius):
#     if skaicius == 1:
#         return False
#     if skaicius == 2:
#         return True
#     else:
#         for x in range(2, skaicius):
#             if (skaicius % x) == 0:
#                 return False
#         return True
                
# rezultatas = ar_pirminis(2)  
# print(rezultatas)              

# 8

# 10

ivesta_data = input("iveskite gimimo data ir laika formatu 'YYYY-MM-DD HH:MM:SS': ")

gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
today = datetime.datetime.now()

#Apskaiciuoti skirtuma nuo dabar ir nuo ivestos datos

skirtumas = (datetime.datetime.now() - gimimo_data)

# Apskaicuoti visus skirtumus



def 
metai = (skirtumas.days // 365)   # papildomas / kad liekanos neapvalintu i metus
menesiai = (skirtumas.days / 30)
dienos = (skirtumas.days)
valandos = (skirtumas.total_seconds() / 3600)
minutes = (skirtumas.total_seconds() / 60)
sekundes = (skirtumas.total_seconds())

#Atspausdinti visus skirtumus

print(f"nuo gimtadienio praejo: ")
print(f"{round(metai)} metu")
print(f"{round(menesiai)} menesiu")
print(f"{dienos} dienu")
print(f"{round(valandos)} valandu")
print(f"{round(minutes)} minuciu")
print(f"{round(sekundes)} sekundziu")















