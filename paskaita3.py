#destytojo
# skaicius = int(input("Iveskite skaiciu "))

# ar_skaicius_teigiamas = bool() # NEBUTINAS
# if skaicius > 0:
#     ar_skaicius_teigiamas = True
# else:
#     ar_skaicius_teigiamas = False
# print(ar_skaicius_teigiamas)


import datetime
# siandien = datetime.datetime.today()
# print(siandien)

# data = datetime.datetime(2022,10,15, 10,15,10)
# print(data)
# print(data.strftime("%d %y")) #%H {}

#data = datetime.datetime(2022,10,15, 10,15,10)

# print(data - datetime.timedelta(days=30))
# print(data - datetime.timedelta(hours=30))
# print(data + datetime.timedelta(hours=30, days=3))

# ivesta_data = input("Iveskite gimimo data: ")
# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
# print("Jusu gimimo data yra: ", gimimo_data)


# ivesta_data = input("Iveskite gimimo data: ")
# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
# skirtumas = (datetime.datetime.now() - gimimo_data)
# print(skirtumas.days)
# print("jums yra: ",skirtumas.days / 365)
# # print("Jusu gimimo data yra: ", gimimo_data)

# galima trumpini pasidaryt kaip                                               pvz: import datetime as dt

# Calculate the difference between today and the birthdate

# age = today.year - gimimo_data.year - ((today.month, today.day) < (gimimo_data.month, gimimo_data.day)) # True - 1 False - 0

# print(age)

# 2 uzd.

# laikas_dabar = datetime.datetime.now()
# print(laikas_dabar)
# print(laikas_dabar - datetime.timedelta(days=5))
# print(laikas_dabar + datetime.timedelta(hours=8)) 
# print(laikas_dabar.strftime("%Y %m %d, %H:%M:%S"))

# pvz kitaip:

# # Dabartinė data ir laikas
# dabar = datetime.now()
# print("Dabartinė data ir laikas: ", dabar)
 
# # Atimti 5 dienas nuo dabartinės datos ir laiko
# penkios_dienos_atgal = dabar - timedelta(days=5)
# print("Penkios dienos atgal: ", penkios_dienos_atgal)


#3 uzd pavyzdys-------------------------------------------------------------------------------------------------

#Prasome vartotojo ivesti data ir laika

# ivesta_data = input("iveskite gimimo data ir laika formatu 'YYYY-MM-DD HH:MM:SS': ")

# #Konvertuojama vartotojo ivestis

# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")

# #Dabartinis laikas

# today = datetime.datetime.now()

# #Apskaiciuoti skirtuma nuo dabar ir nuo ivestos datos

# skirtumas = (datetime.datetime.now() - gimimo_data)

# # Apskaicuoti visus skirtumus

# metai = (skirtumas.days / 365)
# menesiai = (skirtumas.days / 30)
# dienos = (skirtumas.days)
# valandos = (skirtumas.total_seconds() / 3600)
# minutes = (skirtumas.total_seconds() / 60)
# sekundes = (skirtumas.total_seconds())

# #Atspausdinti visus skirtumus

# print(f"nuo gimtadienio praejo: ")
# print(f"{round(metai)} metu")
# print(f"{round(menesiai)} menesiu")
# print(f"{dienos} dienu")
# print(f"{round(valandos)} valandu")
# print(f"{round(minutes)} minuciu")
# print(f"{round(sekundes)} sekundziu")

# 3 uzd. -------------------------------------------------------------------


# from dateutil.relativedelta import relativedelta
# #  metu skirtumas
# ivesta_data = input("Iveskite gimimo diena ir laika ")
# gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d, %H:%M:%S")
# skirtumas = relativedelta(datetime.datetime.today(), gimimo_data)
# # print(skirtumas.months)
# print(skirtumas.years*12+skirtumas.months)

#----------------



# while True:
#     try:
#         x = int(input("Iveskite skaiciu: "))
#         print(f"Jusu ivestas skaicius:  {x}" )  #bandymai
#         break
#     except ValueError:
#         print("Ivedete ne skaiciu. Bandykite dar karta")

# _______________________________ Namu darbai  __________________________________

#  1 UZDAVINYS:

# skaicius = int(input("Iveskite skaiciu "))

# while True:
#     try:
#         if skaicius > 0:
#             ar_skaicius_teigiamas = True
#         else:
#             ar_skaicius_teigiamas = False
#         print(ar_skaicius_teigiamas)
#         break
#     except ValueError:
#         print("Ivedete ne skaiciu. Bandykite dar karta")

# 3 UZDAVINYS:



while True:
    try:
        ivesta_data = input("iveskite gimimo data ir laika formatu 'YYYY-MM-DD HH:MM:SS': ")
        gimimo_data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d %H:%M:%S")
        today = datetime.datetime.now()
        skirtumas = (datetime.datetime.now() - gimimo_data)
        metai = (skirtumas.days / 365)
        menesiai = (skirtumas.days / 30)
        dienos = (skirtumas.days)
        valandos = (skirtumas.total_seconds() / 3600)
        minutes = (skirtumas.total_seconds() / 60)
        sekundes = (skirtumas.total_seconds())
        print(f"nuo gimtadienio praejo: ")
        print(f"{round(metai)} metu")
        print(f"{round(menesiai)} menesiu")
        print(f"{dienos} dienu")
        print(f"{round(valandos)} valandu")
        print(f"{round(minutes)} minuciu")
        print(f"{round(sekundes)} sekundziu")
        break
    except ValueError:
        print("Jusu ivesta data ir laikas neatitinka formato. Pabandykite dar karta")




