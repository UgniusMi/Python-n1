

# class Transportas:
#     def __init__(self, ratai, metai, greitis = None):
#         self.ratai = ratai
#         self.metai = metai
#         if greitis:
#             self.greitis = greitis

#     def __str__(self):
#         return f"Ratai: {self.ratai}, Greitis: {self.greitis}, Metai: {self.metai}"

#     def vaziuoju(self):
#         print("Wrromm wromm")

# class Motociklas(Transportas):
#     def vaziuoju(self):
#         print("DZIIUMMM")

# class Masina(Transportas):
#     def __init__(self, ratai, metai, spalva):
#         self.spalva = spalva
#         super().__init__(ratai, metai)

#     # def __init__(self, transportas, spalva):
#     #     super().__init__(transportas.ratai, transportas.greitis, transportas.metai)
#     #     self.spalva = spalva

#     def __str__(self):
#         return f"Ratai: {self.ratai}, Metai: {self.metai}, Spalva: {self.spalva}"


# transporto_priemones = []

# transportas = Transportas(4, 1998,120)
# motociklas = Motociklas(2, 2005, 280)
# masina = Masina(4, 2005, "Juoda")
# # masina = Masina(transportas, "Juoda")

# transporto_priemones.append(transportas)
# transporto_priemones.append(motociklas)
# transporto_priemones.append(masina)

# for transporto_priemone_viena in transporto_priemones:
#     print(transporto_priemone_viena)
#     transporto_priemone_viena.vaziuoju()
#     print()

# # transportas.vaziuoju()
# # motociklas.vaziuoju()
# # masina.vaziuoju()


# 1 Uzduotis



# class Automobilis:
#     def __init__(self, metai, modelis, kuro_tipas):
#         self.metai = metai
#         self.modelis = modelis
#         self.kuro_tipas =kuro_tipas
#         print(self)
    
#     def __str__(self):
#         return f"Metai: {self.metai}, Modelis: {self.modelis}, Kuro tipas: {self.kuro_tipas}"
    
#     def vaziuoti(self):
#         print("Vaziuoja")

#     def stoveti(self):
#         print("Priparkuota")

#     def pildyti_degalu(self):
#         print("Degalai ipilti")



# class Elektromobilis(Automobilis):
#     def pildyti_degalu(self):
#         print(f"{self.metai} metų {self.modelis} baterija įkrauta.")

#     def vaziuoti_autonomiskai(self):
#         print(f"{self.metai} metų {self.modelis} važiuoja autonomiškai.")

#     # def __init__(self, metai, modelis, kuro_tipas, vaziuoja_autonomiskai):
#     #     self.vaziuoja_autonomiskai = vaziuoja_autonomiskai
#     #     super().__init__(metai, modelis, kuro_tipas)


    
# automobiliai = []

# automobilis1 = Automobilis(2000, "BMW", "dyzelinis" )
# automobilis1.vaziuoti()
# automobilis1.stoveti()
# automobilis1.pildyti_degalu()
# print()
# elektromobilis1 = Elektromobilis( 2010, "Tesla", "Elektra")
# elektromobilis1.vaziuoti()
# elektromobilis1.stoveti()
# elektromobilis1.pildyti_degalu()
# elektromobilis1.vaziuoti_autonomiskai()


# 2 Uzduotis

# from datetime import datetime, timedelta

# class Darbuotojas:
#     def __init__(self, vardas, valandos_ikainis, dirba_nuo):
#         self.vardas= vardas
#         self.valandos_ikainis = valandos_ikainis
#         self.dirba_nuo = dirba_nuo
        
        
#     def nudirbtos_dienos(self):
#         dabar = datetime.now()
#         dirba_nuo_data = datetime.strptime(self.dirba_nuo, "%Y-%m-%d")
#         skirtumas = dabar - dirba_nuo_data
#         darbo_dienos = skirtumas.days
#         return darbo_dienos

#     def paskaiciuoti_atlyginima(self):
#         valandu_skaicius = self.nudirbtos_dienos() * 8
#         atlyginimas = valandu_skaicius * self.valandos_ikainis
#         return atlyginimas



# class NormalusDarbuotojas(Darbuotojas):
    
#     def nudirbtos_dienos(self):
        
#         dabar = datetime.now()
#         dirba_nuo_data = datetime.strptime(self.dirba_nuo, "%Y-%m-%d")
#         darbo_dienos = 0
#         current_date = dirba_nuo_data

#         while current_date <= dabar:

#             if current_date.weekday() < 5:
#                 darbo_dienos += 1

#             current_date += timedelta(days=1)

#         return darbo_dienos

        

    
# darbuotojas1 = Darbuotojas("Rimas", 10, "2024-03-20")
# darbuotojas2 = NormalusDarbuotojas("Arimas",14, "2022-03-20") 

# print("Darbuotojo atlyginimas: ", darbuotojas1.paskaiciuoti_atlyginima())
# print()
# print("Normalaus darbuotojo atlyginimas: ", darbuotojas2.paskaiciuoti_atlyginima())


# 3 Uzdavinys 

class Irasas:
    def __init__(self, suma):
        self.suma = suma
 
    def __str__(self):
        return f"Suma: {self.suma} EUR"
 
class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_informacija = papildoma_informacija
 
class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga
 
class Biudzetas:
    def __init__(self):
        self.zurnalas = []
        self.balansas = 0
   
    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_informacija):
        irasas = PajamuIrasas(suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(irasas)
        self.balansas += suma
   
    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        irasas = IslaiduIrasas(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)
        self.balansas -= suma
 
    def gauti_balansa(self):
        return self.balansas
   
    def gauti_ataskaita(self):
        ataskaita = []
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                ataskaita.append(f"Pajamos: {irasas.suma} EUR, Siuntėjas: {irasas.siuntejas}, Papildoma informacija: {irasas.papildoma_informacija}")
            elif isinstance(irasas, IslaiduIrasas):
                ataskaita.append(f"Išlaidos: {irasas.suma} EUR, Atsiskaitymo būdas: {irasas.atsiskaitymo_budas}, Įsigyta prekė/paslauga: {irasas.isigyta_preke_paslauga}")
        return "\n".join(ataskaita)
 
biudzetas = Biudzetas()
 
while True:
    pasirinkimas = input("Pasirinkite veiksma:\n1. Prideti pajamas\n2. Prideti islaidas\n3. Parodyti balansa\n4. Ataskaita\n5. Baigti\n")
   
    if pasirinkimas == "1":
        pajamos = float(input("Iveskite pajamas: "))
        siuntejas = input("Iveskite siunteja: ")
        papildoma_informacija = input("Iveskite papildoma informacija: ")
        biudzetas.prideti_pajamu_irasa(pajamos, siuntejas, papildoma_informacija)
   
    elif pasirinkimas == "2":
        islaidos = float(input("Iveskite islaidas: "))
        atsiskaitymo_budas = input("Iveskite atsiskaitymo buda: ")
        isigyta_preke_paslauga = input("Iveskite isigyta preke paslauga: ")
        biudzetas.prideti_islaidu_irasa(islaidos, atsiskaitymo_budas, isigyta_preke_paslauga)
 
    elif pasirinkimas == "3":
        print(f"Balansas: {biudzetas.gauti_balansa()} EUR")
 
    elif pasirinkimas == "4":
        print("Ataskaita:")
        print(biudzetas.gauti_ataskaita())
 
 
    elif pasirinkimas == "5":
        print("Programa baige darba.")
        break
 
    else:
        print("Netinkamas pasirinkimas. Bandykite dar karta.")