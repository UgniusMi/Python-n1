if __name__ == "__main__":           
    from python_kursas import PythonKursas
else:
    from modules.python_kursas import PythonKursas


class Kiti_kursai(PythonKursas):  
    def destyti(self):
      print("Vyksta testavimas")