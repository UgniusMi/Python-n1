# Skyliu uzkamsymas

# my_tuple = (1,2,7)
# my_list = [my_tuple, 8,9]  #
# print(my_list)


# for i in range(0,50):
#     print('-'*30)
#     print(f"{i:>{10}.5f}|{i+1:<{10}.5f}")
#     print('-'*30)

# my_list = [5,7,9,8,9,4,2,4,5,1,1,1,2,2,2,3,3,3]
# tekstas = "Sveiki, mano vardas Sveiki, kaip jums Vardas sekasi, Justas, Man MAN Man Man Man Man"
# my_set = set(tekstas.split())
 
# print(my_set)

####

# mano_tuple_sarasas = [(4,6,8),(1,7,9),(9,4,4),(5,15,8),(10,19,9)]
 
# for a,b,c in mano_tuple_sarasas: # a = mano_tuple_sarasas[0][0] b = mano_tuple_sarasas[0][1] ... a = mano_tuple_sarasas[1][0] b = mano_tuple_sarasas[1][1]...
#     print(f"{a}+{b}+{c}={sum((a,b,c))}")

# for ind, skaicius in enumerate(skaiciai2):  #pasitikrint kas ne taip
#     print(f"skaicius {skaicius} yra {ind} sarase")

# ## su zodynais zip 

# skaiciai2 = [4,9,5,1,2,3]
# skaiciai3 = [5,7,8,5,4,2,8]
# for skai in zip(skaiciai,skaiciai2):
#     print(skai)
 
# vardai = ["Jonas","antanas","Mantas","Karolis"]
 
# amziai = [15,54,21,23]
 
# zodynas = dict(zip(vardai,amziai))
 
# print(zodynas)
 
# antano_amzius = zodynas["antanas"]


# a,b,c = ["Stalas","kede","lova"]
 
# print(a)

# mano_sarasas = [num for num in range(0,6)] # num = 0 mano_sarasas.append(0)... num = 1 mano_sarasas.append(1)
 
# for num in range(0,6):
#     mano_sarasas.append(num)
 
# print(mano_sarasas)


##############

# skaiciai = [5,7,9,10]
# mano_sarasas = [num*2 for num in skaiciai if num % 2 ==0] # num = 0 mano_sarasas.append(0)... num = 1 mano_sarasas.append(1)
 
# # ta pati reiskia kitas budas

# for num in skaiciai:
#     if num % 2 ==0:
#         mano_sarasas.append(num*2)
 
# print(mano_sarasas)


# #######

# class MyClass():
#     def __init__(self) -> None:
#         pass
#     def suma(self):
#         raise NotImplementedError("Dar neigyvendinta")
   
#     def dalyba(self,a,b):
#         if(b == 0):
#             raise ZeroDivisionError("DALYBA IS NULIO")
#         else:
#             return a/b
        
# klase = MyClass()
 
 
# try:
#     print(klase.dalyba(7,0)) # 7 ir 0 kaip pvz
   
#     print("Suveikiau tinkamai")
 
# except Exception as e:
#     print(f"ivyko klaida {e}")

################################################################ LAmbda

# skaiciai = [8,4,3]

# skaiciai_3 = map(lambda x: x**3, skaiciai)

# print(list(skaiciai_3)) #

# suma3 = map(lambda a: a+a ,skaiciai)

# print(list(suma3))


##################

# skaiciai = [8,4,3]
 
# def cubed(x):
#     return x **3
 
# skaiciai_3 = map(cubed,skaiciai) # x = skaiciai[0].... return result = x ** 3 skaiciai_3 append(result) (Pakartojama len(skaiciai))
# skaiciai_3 = map(lambda x: x**3,skaiciai) # x = skaiciai[0].... return result = x ** 3 skaiciai_3 append(result) (Pakartojama len(skaiciai))
 
# print(list(skaiciai_3))
 
# def suma(a,b):
#     return a+b
 
# print(suma(4,9))
 
# lambda a,b: a+b # - suma
 
# mano_metodas = lambda a,b: a+b
 
# print(mano_metodas(5,9))

################### FILTRAI ##################






##########

from statistics import mean, median

# sarasas = [2, 4, 10, 22, 40, 15]

# print(mean(sarasas))
# print(median(sarasas))  # Išdėstytas sąrašas pasidaro didejimo tvarka [2, 4, 10, 15, 22, 40] ir is to (10+15)/2

##################

# 1uzdavinys


# tekstas = "Ejo karta ejo voras. Petras buvo, bet nestoras. Ir ilindo i kito voro teritorija."

# def programa(tekstas):
#     sakinys = tekstas.split(".")
#     naujas_sakiniai = map(lambda x: x + "!", sakinys)
#     naujas_sakinys = ''.join(naujas_sakiniai)
#     return naujas_sakinys

# print(programa(tekstas))







#2 uzd 



# from functools import reduce

# skaiciai = list(range(0, 50))

# daugyba = map(lambda x: x*10, skaiciai)
# dalinasi_is7 = filter(lambda x: x% 7 == 0 ,skaiciai)
# # pakelti_kvadratu =  map(lambda x: x**2, skaiciai)

# pakeltas_kvadratu = []
# for skaicius in skaiciai:
#     pakeltas_kvadratu.append(skaicius **2)

# suma = reduce(lambda x, y: x+y,pakeltas_kvadratu)


# print(F"Daugybos sarasas: {list(daugyba)}")
# print(list(dalinasi_is7))
# print(F"Pakeltu kvadratu sarasas: {pakeltas_kvadratu}")
# # print(list(pakelti_kvadratu))    # kitas budas
# print(sum(pakeltas_kvadratu))
# print(f"Kvadratu: {suma}")

# maziausias = min(pakeltas_kvadratu)
# print(f"Maziausias is pakeltu kvadratu saraso: {maziausias}")

# didziausias = max(pakeltas_kvadratu)
# print(f"Didziausias is pakeltu kvadratu saraso: {didziausias}")

# print(mean(pakeltas_kvadratu))
# print(median(pakeltas_kvadratu))

# # atbulai

# atbulai = sorted(pakeltas_kvadratu, reverse=True)
# print(atbulai)

################ 3 uzdavinys




# sarasas = [2.5,2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]


# # skaiciu_suma = sum(x for x in sarasas if ((isinstance(x, int)) or (isinstance(x,float))) and not (isinstance(x,bool)))  #1 variantas
# skaiciu_suma = sum(x for x in sarasas if ((isinstance(x, (int, float)) and not (isinstance(x,bool)))))     # 2 variantas

# skaiciai = [s for s in sarasas if type(s) == float or type(s) == int]          # 3variantas
# y = sum(skaiciai)
# print(f'Skaiciu suma {y}')

# zodziai= (x for x in sarasas if isinstance(x, str))
# sudeti_zodziai = " ".join(zodziai)

# bool_kiekis = sum(type(x) is bool for x in sarasas)
# print(skaiciu_suma)
# print(sudeti_zodziai)

# print(bool_kiekis)



# ####### 4

# from operator import attrgetter
 
# # Turėtų klasę Zmogus, su savybėmis vardas ir amzius
# # Klasėje būtų __repr__ metodas, kuris atvaizduotų vardą ir amžių
 
# class Zmogus:
#     def __init__(self, vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
 
#     def __repr__(self):
#         return (f"({self.vardas}, {self.amzius})")
 
# # Inicijuoti kelis Zmogus objektus su vardais ir amžiais
# # Įdėti sukurtus Zmogus objektus į naują sąrašą
 
# z1 = Zmogus("Domas", 22)
# z2 = Zmogus("Antanas", 30)
# z3 = Zmogus("Jonas", 45)
 
# sarasas = [z1, z2, z3]
 
# # Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą
 
# surusiuotas = sorted(sarasas, key=lambda z: (z.vardas, z.amzius))
# print(surusiuotas)
 
# # arba
 
# surusiuotas = sorted(sarasas, key=attrgetter("vardas"))
# print(surusiuotas)
 
# # Surūšiuotų ir atspausdintų sąrašo objektus pagal vardą atbulai
 
# surusiuotas = sorted(sarasas, key=attrgetter("vardas"), reverse=True)
# print(surusiuotas)
 
# # Surūšiuotų ir atspausdintų sąrašo objektus pagal amžių
 
# surusiuotas = sorted(sarasas, key=attrgetter("amzius","vardas"))
# print(surusiuotas)
 
# # Surūšiuotų ir atspausdintų sąrašo objektus pagal amžių atbulai
 
# surusiuotas = sorted(sarasas, key=attrgetter("amzius"), reverse=True)
# print(surusiuotas)