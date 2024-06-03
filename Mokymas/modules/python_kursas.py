# from . import kursas     

# class PythonKursas(kursas.Kursas):  
#     def destyti(self):
#       print("Vyksta programavimas")
     

############# Budas 2


if __name__ == "__main__":            # importinam pirma faila jei turetume kita faila imtume is sito failo su main.
    from kursas import Kursas
else:
    from modules.kursas import Kursas


class PythonKursas(Kursas):  
    def destyti(self):
      print("Vyksta programavimas")
     