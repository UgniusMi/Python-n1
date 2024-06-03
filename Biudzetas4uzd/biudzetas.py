from islaidu_irasas import IslaiduIrasas
from pajamu_irasas import PajamuIrasas

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
    