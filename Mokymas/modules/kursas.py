
class Kursas:
    def __init__(self, destytojas, trukme):
        self.destytojas = destytojas
        self.trukme = trukme
    def __str__(self):
        return f"Destytojas: {self.destytojas}, Trukme: {self.trukme}"

    def destyti(self):
        print("Vyksta Mokymas!")
        
#Kursas.destyti('')
