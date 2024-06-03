# class person:
#     def __init__(self, vardas, metus, asmens_kodas):
#         self.vardas = vardas
#         self.metus = metus
#         self.asmens_kodas = asmens_kodas
    
#     def vardas_didziosiomis(self):
#         return self.vardas.upper()


#     def __str__(self):
#         return f"Vardas: {self.vardas} Metai: {self.metus} Asmens Kodas: {self.asmens_kodas}"

# zmogus1 = person("Rokas", 1988, 23123132456)
# zmogus2 = person("Jonas", 1956, 4564564545)
# zmogus3 = person("John", 2001, 456456)

# print(zmogus1)
# print(zmogus2)
# print(zmogus3)

# print(zmogus2.vardas_didziosiomis())
# print(zmogus2.metus)


# ---------------------------------------------------------------
# UZDAVINYS NR1


# class Sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas

#     def tekstas_atbulai(self):
#         return self.tekstas[::-1]
    
#     def tekstas_mazosiomis(self):
#         return self.tekstas.lower()
    
#     def tekstas_didziosiomis(self):
#         return self.tekstas.upper()
    
#     def tekstas_pagal_eiles_nuemri(self, numeris):
#         return self.tekstas.split()[numeris]
    
#     def tekstas_kiek_zodziu(self):
#         zodziai = self.tekstas.split(' ')  
#         word_count = len(zodziai)
#         return word_count    #  len(self.tekstas.split())
#         #return len(self.tekstas.split())  #galima ir taip

#     def tekstas_kiek_zodziu_pagal_simboli(self, simbolis):
#         return self.tekstas.count(simbolis)    

#     def pakeist_zody(self, senas_zodis, naujas_zodis):
#         pakeistas_tekstas = self.tekstas.replace(senas_zodis, naujas_zodis)
#         return pakeistas_tekstas
    
#     def zodziu_skaicius(self):
#         zodziai = self.tekstas.split()
#         return len(zodziai)
    
#     def skaiciu_skaicius(self):
#         skaiciai = sum(c.isdigit() for c in self.tekstas)
#         return skaiciai
    
#     def didziuju_raidziu_skaicius(self):
#         didziosios_raides = sum(c.isupper() for c in self.tekstas)
#         return didziosios_raides
    
#     def mazuju_raidziu_skaicius(self):
#         mazosios_raides = sum(c.islower() for c in self.tekstas)
#         return mazosios_raides
#     def spausdinti(self):
#         print(self.tekstas_kiek_zodziu())

        
    
# senas_zodis = "galetu"    
# naujas_zodis = "turetu"

# sakinys1 = Sakinys("Cia galetu buti jusu REKLAMA 2000")
# print(sakinys1.tekstas_atbulai())
# print(sakinys1.tekstas_mazosiomis())
# print(sakinys1.tekstas_didziosiomis())
# print(sakinys1.tekstas_pagal_eiles_nuemri(4))
# print(sakinys1.tekstas_kiek_zodziu())
# print(sakinys1.pakeist_zody(senas_zodis, naujas_zodis))
# print(sakinys1.zodziu_skaicius())
# print(sakinys1.skaiciu_skaicius())
# print(sakinys1.didziuju_raidziu_skaicius())
# print(sakinys1.mazuju_raidziu_skaicius())
# print(sakinys1.tekstas_kiek_zodziu_pagal_simboli('a'))



# UZDAVINYS 2

# from datetime import datetime, timedelta

# class Sukaktis:
#     def __init__(self, metai, menuo, diena, valanda=0, minute=0, sekunde=0):
#         self.data = datetime(metai, menuo, diena, valanda, minute, sekunde)
    
#     def praejo_nuo_sukakties(self):
#         dabar = datetime.now()
#         skirtumas = dabar - self.data
#         metai = skirtumas.days // 365
#         savaites = skirtumas.days // 7
#         dienos = skirtumas.days
#         valandos = skirtumas.total_seconds() // 3600
#         minutes = skirtumas.total_seconds() // 60
#         sekundes = skirtumas.total_seconds()
#         return {
#             "metai": metai,
#             "savaites": savaites,
#             "dienos": dienos,
#             "valandos": valandos,
#             "minutes": minutes,
#             "sekundes": sekundes }
#         # return f"metai - {metai}, savaites - {savaites}, dienos - {dienos}, valandos - {valandos}, minutes - {minutes}, sekundes - {sekundes}"    #galima ir taip
    
#     def ar_keliamieji_metai(self):
#         metai = self.data.year
#         return metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0)
    
#     def atimti_dienas(self, kiek_dienu):
#         nauja_data = self.data - timedelta(days=kiek_dienu)
#         return nauja_data
    
#     def prideti_dienas(self, kiek_dienu):
#         nauja_data = self.data + timedelta(days=kiek_dienu)
#         return nauja_data

# sukaktis = Sukaktis(2012, 1, 1)

# # Praėjo nuo sukakties
# praejo = sukaktis.praejo_nuo_sukakties()
# print(f"Praėjo nuo sukakties: {praejo}")

# # Ar sukakties metai buvo keliamieji
# keliamieji = sukaktis.ar_keliamieji_metai()
# print(f"Ar metai buvo keliamieji: {keliamieji}")

# # Atimti dienas
# nauja_data_atemus = sukaktis.atimti_dienas(30)
# print(f"Nauja data atėmus 30 dienų: {nauja_data_atemus}")

# # Pridėti dienas
# nauja_data_pridejus = sukaktis.prideti_dienas(30)
# print(f"Nauja data pridėjus 30 dienų: {nauja_data_pridejus}")

# 3 UZDAVINYS 1

# class Sakinys:
#     def __init__(self, tekstas = "default tekstas"):
#         self.tekstas = tekstas

#     def tekstas_atbulai(self):
#         return self.tekstas[::-1]
    
#     def tekstas_mazosiomis(self):
#         return self.tekstas.lower()
    
#     def tekstas_didziosiomis(self):
#         return self.tekstas.upper()
    
#     def tekstas_pagal_eiles_nuemri(self):
#         return self.tekstas.split()[0]
    
#     def tekstas_kiek_zodziu(self):
#         zodziai = self.tekstas.split(' ')  
#         word_count = len(zodziai)
#         return word_count    #  len(self.tekstas.split())


#     def pakeist_zody(self, senas_zodis, naujas_zodis):
#         pakeistas_tekstas = self.tekstas.replace(senas_zodis, naujas_zodis)
#         return pakeistas_tekstas
    
#     def zodziu_skaicius(self):
#         zodziai = self.tekstas.split()
#         return len(zodziai)
    
#     def skaiciu_skaicius(self):
#         skaiciai = sum(c.isdigit() for c in self.tekstas)
#         return skaiciai
    
#     def didziuju_raidziu_skaicius(self):
#         didziosios_raides = sum(c.isupper() for c in self.tekstas)
#         return didziosios_raides
    
#     def mazuju_raidziu_skaicius(self):
#         mazosios_raides = sum(c.islower() for c in self.tekstas)
#         return mazosios_raides
    
# senas_zodis = "galetu"    
# naujas_zodis = "turetu"

# sakinys1 = Sakinys()
# print(sakinys1.tekstas_atbulai())
# print(sakinys1.tekstas_mazosiomis())
# print(sakinys1.tekstas_didziosiomis())
# print(sakinys1.tekstas_pagal_eiles_nuemri())
# print(sakinys1.tekstas_kiek_zodziu())
# print(sakinys1.pakeist_zody(senas_zodis, naujas_zodis))
# print(sakinys1.zodziu_skaicius())
# print(sakinys1.skaiciu_skaicius())
# print(sakinys1.didziuju_raidziu_skaicius())
# print(sakinys1.mazuju_raidziu_skaicius())

# 3 UZDAVINYS 2

# from datetime import datetime, timedelta

# class Sukaktis:
#     def __init__(self, metai=1989, menuo=9 , diena=8, valanda=0, minute=0, sekunde=0):
#         self.data = datetime(metai, menuo, diena, valanda, minute, sekunde)
    
#     def praejo_nuo_sukakties(self):
#         dabar = datetime.now()
#         skirtumas = dabar - self.data
#         metai = skirtumas.days // 365
#         savaites = skirtumas.days // 7
#         dienos = skirtumas.days
#         valandos = skirtumas.total_seconds() // 3600
#         minutes = skirtumas.total_seconds() // 60
#         sekundes = skirtumas.total_seconds()
#         return {
#             "metai": metai,
#             "savaites": savaites,
#             "dienos": dienos,
#             "valandos": valandos,
#             "minutes": minutes,
#             "sekundes": sekundes }
#         # return f"metai - {metai}, savaites - {savaites}, dienos - {dienos}, valandos - {valandos}, minutes - {minutes}, sekundes - {sekundes}"    #galima ir taip
    
#     def ar_keliamieji_metai(self):
#         metai = self.data.year
#         return metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0)
    
#     def atimti_dienas(self, kiek_dienu):
#         nauja_data = self.data - timedelta(days=kiek_dienu)
#         return nauja_data
    
#     def prideti_dienas(self, kiek_dienu):
#         nauja_data = self.data + timedelta(days=kiek_dienu)
#         return nauja_data

# sukaktis = Sukaktis()

# # Praėjo nuo sukakties
# praejo = sukaktis.praejo_nuo_sukakties()
# print(f"Praėjo nuo sukakties: {praejo}")

# # Ar sukakties metai buvo keliamieji
# keliamieji = sukaktis.ar_keliamieji_metai()
# print(f"Ar metai buvo keliamieji: {keliamieji}")

# # Atimti dienas
# nauja_data_atemus = sukaktis.atimti_dienas(30)
# print(f"Nauja data atėmus 30 dienų: {nauja_data_atemus}")

# # Pridėti dienas
# nauja_data_pridejus = sukaktis.prideti_dienas(30)
# print(f"Nauja data pridėjus 30 dienų: {nauja_data_pridejus}")

# 4.1 UZDAVINYS

# class Sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas

#     def tekstas_atbulai(self):
#         return self.tekstas[::-1]
    
#     def tekstas_mazosiomis(self):
#         return self.tekstas.lower()
    
#     def tekstas_didziosiomis(self):
#         return self.tekstas.upper()
    
#     def tekstas_pagal_eiles_nuemri(self):
#         return self.tekstas.split()[4]
    
#     def tekstas_kiek_zodziu(self):
#         zodziai = self.tekstas.split(' ')  
#         word_count = len(zodziai)
#         return word_count    #  len(self.tekstas.split())
#         #return len(self.tekstas.split())  #galima ir taip

#     def pakeist_zody(self, senas_zodis, naujas_zodis):
#         pakeistas_tekstas = self.tekstas.replace(senas_zodis, naujas_zodis)
#         return pakeistas_tekstas
    
#     def zodziu_skaicius(self):
#         zodziai = self.tekstas.split()
#         return len(zodziai)
    
#     def skaiciu_skaicius(self):
#         skaiciai = sum(c.isdigit() for c in self.tekstas)
#         return skaiciai
    
#     def didziuju_raidziu_skaicius(self):
#         didziosios_raides = sum(c.isupper() for c in self.tekstas)
#         return didziosios_raides
    
#     def mazuju_raidziu_skaicius(self):
#         mazosios_raides = sum(c.islower() for c in self.tekstas)
#         return mazosios_raides
    
# senas_zodis = "galetu"    
# naujas_zodis = "turetu"

# tekstas1 = input("Parasykite savo varda: ")

# sakinys1 = Sakinys("Cia galetu buti jusu REKLAMA 2000")
# print(sakinys1.tekstas_atbulai())
# print(sakinys1.tekstas_mazosiomis())
# print(sakinys1.tekstas_didziosiomis())
# print(sakinys1.tekstas_pagal_eiles_nuemri())
# print(sakinys1.tekstas_kiek_zodziu())
# print(sakinys1.pakeist_zody(senas_zodis, naujas_zodis))
# print(sakinys1.zodziu_skaicius())
# print(sakinys1.skaiciu_skaicius())
# print(sakinys1.didziuju_raidziu_skaicius())
# print(sakinys1.mazuju_raidziu_skaicius())




# 5 UZDAVINYS

# class Irasas:
#     def __init__(self, tipas, suma):
#         self.tipas = tipas
#         self.suma = suma
#     def __str__(self):
#         return f"suma: {self.suma}, tipas: {self.tipas}"

# class Biudzetas:
#     def __init__(self):
#         self.zurnalas = []

#     def prideti_pajamu_irasa(self, suma):
#         irasas = Irasas("pajamos", suma)
#         self.zurnalas.append(irasas)


# biudzetas = Biudzetas()


# while True:
#     pajamos = int(input("Iveskite pajamas: "))
#     biudzetas.prideti_pajamu_irasa(pajamos)