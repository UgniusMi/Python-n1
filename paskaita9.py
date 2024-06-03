################# PVZ 

# class Darbuotojas:
#     def __init__(self, name) -> None:
#         self.name = name
 
#     def __repr__(self) -> str:
#         return self.name
   
#     def __str__(self) -> str:
#         return self.name
 
# darb1 = Darbuotojas("Justas")
# darb2 = Darbuotojas("Antanas")
# darb3 = Darbuotojas("Mantas")
 
# darbuotojai = [darb1,darb2,darb3]
 
# surikiuoti = sorted(darbuotojai,key= lambda darbuotojas: darbuotojas.name)
 
# # print(surikiuoti)
 
# zodynas = {"Lukas":15,"Jonas":20,"Antanas":5}
# print(zodynas)
# surikiuotas_zod = sorted(zodynas.items(), key= lambda key_value_pair: key_value_pair[1] )
 
# print(surikiuotas_zod)


##########################################################

# if __name__ == '__main__': # šitas suveiks tik tada, kai šis failas bus leidžiamas tiesiogiai, bet ne importuojamas
#     # print("Sveiki as esu modulis")
#     # print("Failo pabaiga")
#     # svarbus_kintamasis = 15
#     print(__name__) # '__main__'
# else:
#     # print("Aš nesu pagrindinis failas")
#     print(__name__) # modulis_paskaita9
# 

# import modulis_paskaita9
 
 
# print("Paskaita9.py dabartinis vardas: " +__name__)
 
 
 
# if __name__ == '__main__': # šitas suveiks tik tada, kai šis failas bus leidžiamas tiesiogiai, bet ne importuojamas
#     print("Aš esu pagrindinis failas, ir mano nepakeistas pavadinimas yra Paskaita9")
 
########################       1



# #1.1

# import datetime as dt

# data_ir_laikas = dt.datetime.now()
# data = dt.date.today()
# laikas_dabar = data_ir_laikas.time()

# print(f"Data ir laikas: {data_ir_laikas}")
# print(f"Data: {data}")
# print(f"laikas: {laikas_dabar}")


## 1.2

# from datetime import date 

# print(date.today())

## 1.3

# from datetime import date as data

# print(data.today())


########################       2

# import 